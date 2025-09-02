import logging
import struct

from typing import TYPE_CHECKING

try:
    from typing import override, ClassVar
except ImportError:
    if TYPE_CHECKING:
        from typing import override, ClassVar
    else:
        from typing_extensions import override, ClassVar

from NetUtils import ClientStatus, NetworkItem
import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

from .addresses import RAM, menu_lookup, Environment, internal_id_to_offset
from .locations import location_name_to_id, total_treasure
from .items import item_id_to_name, boss_items, homeworld_access, goal_item

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext

logger = logging.getLogger("Client")


class SpyroClient(BizHawkClient):
    game: ClassVar[str] = "Spyro the Dragon"
    system: ClassVar[str | tuple[str]] = "PSX"

    local_checked_locations: set[int] = set()
    slot_data_spyro_color: bytes = b''
    slot_data_mapped_entrances: list[tuple[str, str]] = []

    env_by_id: dict[int, Environment] = {}
    env_by_name: dict[str, Environment] = {}

    hub: Environment
    level: Environment
    for hub in RAM.hub_environments:
        env_by_id[hub.internal_id] = hub
        env_by_name[hub.name] = hub

        for level in hub.child_environments:
            env_by_id[level.internal_id] = level
            env_by_name[level.name] = level

    ap_unlocked_worlds: set[str] = set()
    boss_items: set[str] = set()

    gem_counts: dict[int, int] = {}
    """Keeps track of gem counts, indexed by level ID"""

    vortexes_reached: dict[int, int] = {}
    """Keeps track of reached vortices, indexed by level ID"""

    portal_accesses: dict[str, bool] = {}
    """Keeps track of portal access, indexed by level name"""

    # Set up stuff for tracking later
    env: Environment
    for env in env_by_id.values():
        gem_counts[env.internal_id] = 0
        if not env.is_hub():
            portal_accesses[env.name] = False

    @override
    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        spyro_id: bytes = struct.pack("<17s", b"BASCUS-94228SPYRO")
        spyro_id_ram_address: int = 0xBA92
        try:
            # Check ROM name
            # Hopefully this keeps the encoding right on big endian machines
            read_bytes: bytes = (
                await bizhawk.read(ctx.bizhawk_ctx, [(spyro_id_ram_address, len(spyro_id), "MainRAM")])
            )[0]
            if read_bytes != spyro_id:
                # Do command processor cleanup here
                return False

        except bizhawk.RequestFailedError:
            # Do command processor cleanup here
            return False  # Not able to get a response, say no for now

        if self.game != "Spyro the Dragon":
            # Do command processor cleanup here
            return False

        ctx.game = self.game
        # We want to be able to receive items from ourselves, and others
        # Also handle starting inventory for initial level(s)
        ctx.items_handling = 0b111
        # Slot data will hold a lot of useful data for shuffling levels and etc
        ctx.want_slot_data = True
        # Setup command processor here

        return True

    @override
    async def game_watcher(self, ctx: "BizHawkClientContext") -> None:
        batched_reads: list[tuple[int, int, str]] = []
        # Detect if AP connection made, bail early if not
        if (
            (ctx.server is None) or (ctx.server.socket.closed)
            or (ctx.slot_data is None) or (ctx.auth is None)
        ):
            return

        if ctx.watcher_timeout != 0.125:
            # Hopefully this runs the first time. Good place for init stuff, if so
            # Might break in the future, even if it does.
            # TODO: replace with own bool
            ctx.watcher_timeout = 0.125

        await self.process_received_items(ctx.items_received, ctx)

        if self.slot_data_spyro_color == b'':
            color_value: int
            color_value = ctx.slot_data["spyro_color"]
            self.slot_data_spyro_color = color_value.to_bytes(4, byteorder="big")

        if (len(self.slot_data_mapped_entrances) == 0) and (len(ctx.slot_data["entrances"]) > 0):
            temp_list: list[tuple[str, str]] = []
            temp_list = ctx.slot_data["entrances"]
            for item in temp_list:
                if "Fly-in" in item[0]:
                    self.slot_data_mapped_entrances.append(item)

        try:
            to_read_list: list[tuple[int, int]] = [
                (RAM.last_received_archipelago_id, 4),
                (RAM.cur_game_state, 1),
                (RAM.cur_level_id, 1),
                (RAM.spyro_color_filter, 4),
                (RAM.gnasty_anim_flag, 1),
                (RAM.unlocked_worlds, 6),
                (RAM.balloonist_menu_choice, 1),
                (RAM.total_gem_count, 4),
                (RAM.switched_portal_dest, 1),
                (RAM.spyro_cur_animation, 1),
                (RAM.last_touched_whirlwind, 3),
            ]

            gem_counter_offset = len(to_read_list)

            for env in self.env_by_id.values():
                to_read_list.append((env.gem_counter, 2))

            vortex_offset = len(to_read_list)

            for env in self.env_by_id.values():
                to_read_list.append((env.vortex_pointer, 1))

            for address, size in to_read_list:
                batched_reads.append((address, size, "MainRAM"))

            ram_data = await bizhawk.read(ctx.bizhawk_ctx, batched_reads)

            recv_index = self.little_bytes(ram_data[0])
            cur_game_state = self.little_bytes(ram_data[1])
            cur_level_id = self.little_bytes(ram_data[2])
            spyro_color = self.little_bytes(ram_data[3])
            gnasty_anim_flag = self.little_bytes(ram_data[4])
            unlocked_worlds = ram_data[5]
            balloonist_choice = self.little_bytes(ram_data[6])
            total_gems_collected = self.little_bytes(ram_data[7])
            did_portal_switch = self.little_bytes(ram_data[8])
            spyro_anim = self.little_bytes(ram_data[9])
            last_whirlwind_pointer = self.little_bytes(ram_data[10])

            for env_id in self.env_by_id:
                ram_data_offset = gem_counter_offset + internal_id_to_offset(env_id)
                self.gem_counts[env_id] = self.little_bytes(ram_data[ram_data_offset])

            for env_id, env in self.env_by_id.items():
                if not env.is_hub():
                    ram_data_offset = vortex_offset + internal_id_to_offset(env_id)
                    self.vortexes_reached[env_id] = self.little_bytes(ram_data[ram_data_offset])

            if cur_game_state == RAM.GameStates.GAMEPLAY:
                if self.env_by_id[cur_level_id].name == "Gnasty Gnorc":
                    if gnasty_anim_flag == RAM.GNASTY_DEFEATED:
                        await self.send_location_once("Defeated Gnasty Gnorc", ctx)

            if cur_game_state == RAM.GameStates.GAMEPLAY:
                # Send 1/4 gem threshold checks
                for env in self.env_by_id.values():
                    quarter_count: int = int(env.total_gems / 4)

                    for index in range(1, 5):
                        if self.gem_counts[env.internal_id] >= (quarter_count * index):
                            await self.send_location_once(f"{env.name} {25 * index}% Gems", ctx)

                # Send 500 increment total gem threhshold checks
                for gem_threshold in range(500, total_treasure + 1, 500):
                    if total_gems_collected >= gem_threshold:
                        await self.send_location_once(f"{gem_threshold} Gems", ctx)

            to_write_ingame: list[tuple[int, bytes]] = []
            to_write_menu: list[tuple[int, bytes]] = []
            to_write_balloonist: list[tuple[int, bytes]] = []
            to_write_exiting: list[tuple[int, bytes]] = []
            to_write_inventory: list[tuple[int, bytes]] = []

            if (
                (cur_game_state == RAM.GameStates.GAMEPLAY)
                and (self.slot_data_spyro_color != b'')
                and (spyro_color.to_bytes(4, "little") != self.slot_data_spyro_color)
            ):
                spyro_color = self.little_bytes(self.slot_data_spyro_color)
                to_write_ingame.append((RAM.spyro_color_filter, spyro_color.to_bytes(4, "little")))

            if (
                (cur_game_state == RAM.GameStates.GAMEPLAY)
                and (unlocked_worlds.count(bytes([0])) > 1)
            ):
                to_write_ingame.append((RAM.unlocked_worlds, bytes([2, 2, 2, 2, 2, 2])))

            if cur_game_state in (RAM.GameStates.GAMEPLAY, RAM.GameStates.INVENTORY):
                # Force all levels and hubs to be visible on the inventory screen
                for index in range(len(self.env_by_id)):
                    to_write_inventory.append((RAM.show_on_inventory_array + index, b'\x01'))

                # Modify level/hub names to indicate accessibility and completion status
                write_list: list[tuple[int, bytes]] = self.show_access(ctx)
                for item in write_list:
                    if cur_game_state == RAM.GameStates.GAMEPLAY:
                        to_write_ingame.append(item)

                    else:
                        to_write_inventory.append(item)

            # If exiting level from menu, and portal shuffle on,
            # change cur_level_id to portal's vanilla level's internal ID
            if cur_game_state == RAM.GameStates.EXITING_LEVEL:
                if (did_portal_switch == 0) and (len(self.slot_data_mapped_entrances) > 0):
                    # Turn flag on so we don't remap more than once
                    to_write_exiting.append((RAM.switched_portal_dest, b'\x01'))
                    hub_entrance_portal_name: str = ""
                    cur_level_env: Environment = self.env_by_id[cur_level_id]
                    hub_entrance_portal_name = self.lookup_portal_exit(cur_level_env.name, ctx)
                    id_of_entrance = self.env_by_name[hub_entrance_portal_name].internal_id
                    to_write_exiting.append(
                        (RAM.cur_level_id, id_of_entrance.to_bytes(1, byteorder="little"))
                    )

            if cur_game_state == RAM.GameStates.GAMEPLAY:
                # Reset this for tracking on next level exit. Can't switch in whirlwind, might be exiting via vortex
                if (
                    (did_portal_switch == 1)
                    and (spyro_anim != RAM.SpyroStates.WHIRLWIND)
                    and not (self.env_by_id[cur_level_id].is_hub())
                ):
                    to_write_ingame.append((RAM.switched_portal_dest, b'\x00'))

                if (
                    (spyro_anim == RAM.SpyroStates.WHIRLWIND)
                    and (did_portal_switch == 0)
                    and (not self.env_by_id[cur_level_id].is_hub())
                    and (last_whirlwind_pointer == self.env_by_id[cur_level_id].vortex_moby_pointer)
                ):
                    # We're in a whirlwind, haven't modified the current level ID, we're in a level,
                    # and we're touching the vortex
                    # Send vortex location
                    await self.send_location_once(f"{self.env_by_id[cur_level_id].name} Vortex", ctx)

                    # If portal shuffle on, begin doing checks for setting vortex exit portal
                    if len(self.slot_data_mapped_entrances) > 0:
                        # Modify current level ID to point at portal's vanilla level, to make the game think we're
                        # leaving that other level, causing us to exit from that portal in that homeworld
                        to_write_ingame.append((RAM.switched_portal_dest, b'\x01'))
                        hub_entrance_portal_name: str = ""
                        cur_level_env: Environment = self.env_by_id[cur_level_id]
                        hub_entrance_portal_name = self.lookup_portal_exit(cur_level_env.name, ctx)
                        id_of_entrance = self.env_by_name[hub_entrance_portal_name].internal_id
                        to_write_ingame.append((RAM.cur_level_id, id_of_entrance.to_bytes(1, byteorder="little")))

                env = self.env_by_id[cur_level_id]

                # Overwrite head checking code
                if len(env.statue_head_checks) > 0:
                    for address in env.statue_head_checks:
                        # NOP out the conditional branches
                        # This forces the statue heads to always open
                        to_write_ingame.append((address, bytes(4)))

                # Make Nestor skippable
                if env.name == "Artisans":
                    to_write_ingame.append((RAM.nestor_unskippable, b'\x00'))

                # Prevent Tuco's warp-to-level shenanigans by setting egg minimum to -1
                if env.name == "Magic Crafters":
                    to_write_ingame.append((RAM.tuco_egg_minimum, b'\xff\xff'))

                if env.is_hub():
                    for index, level in enumerate(env.child_environments):
                        # Lock inaccessible portals
                        if self.portal_accesses[level.name]:
                            to_write_ingame.append((env.portal_surface_types[index], b'\x06'))
                        else:
                            to_write_ingame.append((env.portal_surface_types[index], b'\x00'))

                        # If portal shuffle is on
                        if len(self.slot_data_mapped_entrances) > 0:
                            # Modify portal destinations
                            dest_level_name = self.lookup_portal_leads_to(level.name, ctx)
                            portal_dest_id: int = self.env_by_name[dest_level_name].internal_id
                            to_write_ingame.append(
                                (env.portal_dest_level_ids[index], portal_dest_id.to_bytes(1, byteorder="little"))
                            )

            if cur_game_state == RAM.GameStates.TITLE_SCREEN:
                starting_world_value: int = ctx.slot_data["starting_world"]
                starting_world_value += 1
                starting_world_value *= 10
                to_write_menu.append((RAM.starting_level_id, starting_world_value.to_bytes(1, "little")))

            if cur_game_state == RAM.GameStates.BALLOONIST:
                env = self.env_by_id[cur_level_id]

                if env.is_hub():

                    # Hide world names if inaccessible
                    for looped_env in self.env_by_id.values():
                        if not looped_env.is_hub():
                            continue

                        byte_val = looped_env.name[:1].encode("ASCII")

                        if looped_env.name != "Gnasty's World":
                            if looped_env.name not in self.ap_unlocked_worlds:
                                byte_val = b'\x00'

                            to_write_balloonist.append((looped_env.text_offset, byte_val))
                        else:
                            if len(self.boss_items) != 5:
                                byte_val = b'\x00'

                            to_write_balloonist.append((looped_env.text_offset, byte_val))

                    # Prevent access to inaccessible worlds

                    # Rewrite level data pointers to point at mod's area of memory
                    to_write_balloonist.append((env.balloon_pointers[0], b'\x01'))
                    to_write_balloonist.append((env.balloon_pointers[1], b'\x0c\xf0'))

                    # Turn menu selection number into world index number
                    mapped_choice = menu_lookup((int(env.internal_id / 10) - 1), balloonist_choice)

                    # Poke last valid selected choice number to RAM
                    # as well as poking a value to what the game
                    # thinks is a timer, which allows selecting a
                    # choice when it is >= 0x1f
                    # The code is normally meant to prevent a player
                    # from choosing an option in the menu within a few
                    # frames of the menu opening. We abuse it for
                    # setting conditional access instead
                    for item in self.set_balloonist_unlocks(mapped_choice, balloonist_choice):
                        to_write_balloonist.append(item)

            await self.write_on_state(
                to_write_ingame,
                RAM.GameStates.GAMEPLAY.to_bytes(1, byteorder="little"),
                ctx
            )

            await self.write_on_state(
                to_write_exiting,
                RAM.GameStates.EXITING_LEVEL.to_bytes(1, byteorder="little"),
                ctx
            )

            await self.write_on_state(
                to_write_menu,
                RAM.GameStates.TITLE_SCREEN.to_bytes(1, byteorder="little"),
                ctx
            )

            await self.write_on_state(
                to_write_balloonist,
                RAM.GameStates.BALLOONIST.to_bytes(1, byteorder="little"),
                ctx
            )

            await self.write_on_state(
                to_write_inventory,
                RAM.GameStates.INVENTORY.to_bytes(1, byteorder="little"),
                ctx
            )

        except bizhawk.RequestFailedError:
            pass

    def balloonist_helper(self, allow: bytes, choice: bytes) -> list[tuple[int, bytes]]:
        result: list[tuple[int, bytes]] = []
        result.append((RAM.fake_timer, allow))
        result.append((RAM.last_selected_valid_choice, choice))
        return result

    def set_balloonist_unlocks(self, mapped_choice: int, raw_choice: int) -> list[tuple[int, bytes]]:
        """Given the index of the selected option in terms of homeworld indices, and the position of the selection in
        the balloonists' menu, builds a list of writes to perform in order to allow or deny access to choose the
        selected option

        Args:
            mapped_choice: The numeric index of the homeworld selected, or -1 for "Stay Here"
            raw_choice: The current index of the choice in the balloonist menu

        Returns:
            A list of writes in the format (adress, bytes)
        """
        result: list[tuple[int, bytes]] = []

        hub_name: str = "Stay Here"  # default in case it's -1, which is Stay Here anyway.
        hub_id: int = 0
        if mapped_choice != -1:
            hub_id = (mapped_choice + 1) * 10
            hub_name = self.env_by_id[hub_id].name

        if (hub_name != "Stay Here") and (hub_name != "Gnasty's World"):
            if hub_name in self.ap_unlocked_worlds:
                for item in self.balloonist_helper(b'\x1f', raw_choice.to_bytes(1, byteorder="little")):
                    result.append(item)
            else:
                for item in self.balloonist_helper(b'\x00', b'\x00'):
                    result.append(item)
        elif hub_name == "Gnasty's World":
            if len(self.boss_items) == 5:
                for item in self.balloonist_helper(b'\x1f', raw_choice.to_bytes(1, byteorder="little")):
                    result.append(item)
            else:
                for item in self.balloonist_helper(b'\x00', b'\x00'):
                    result.append(item)
        else:
            for item in self.balloonist_helper(b'\x1f', b'\x00'):
                result.append(item)

        return result

    async def write_on_state(
        self, write_list: list[tuple[int, bytes]], state: bytes, ctx: "BizHawkClientContext"
    ) -> None:
        """Does a guarded write based on the current game state.

        Args:
            write_list: entries in the form of (address, bytes to write)
            state: game state
            ctx: BizhawkClientContext
        """
        to_write_list: list[tuple[int, bytes, str]] = []

        for item in write_list:
            to_write_list.append((item[0], item[1], "MainRAM"))

        if len(write_list) > 0:
            _ = await bizhawk.guarded_write(
                ctx.bizhawk_ctx, to_write_list, [(RAM.cur_game_state, state, "MainRAM")]
            )

    async def send_location_once(self, location_name: str, ctx: "BizHawkClientContext") -> None:
        """Send a location to the server, but only if it hasn't been sent
        before

        Args:
            location_name: The name of the location to send
            ctx: BizhawkClientContext
        """
        location_id = location_name_to_id[location_name]

        if location_id not in ctx.checked_locations:
            await ctx.send_msgs([{"cmd": "LocationChecks", "locations": [location_id]}])

    def little_bytes(self, bytes_in: bytes) -> int:
        """Returns an int from the given little-endian bytes

        Args:
            bytes_in: the sequence of bytes to interpret

        Returns:
            Little-endian-interpreted int
        """
        return int.from_bytes(bytes_in, byteorder="little")

    def lookup_portal_leads_to(self, portal_entering: str, ctx: "BizHawkClientContext") -> str:
        """Given the name of a portal a player is entering, return the level the portal should lead to

        Args:
            portal_entering: The portal being walked into
            ctx: BizhawkClientContext

        Returns:
            The name of the level the portal should lead to
        """
        # Iterate through mapped entrances to find pairing for lookup
        flyin_level_name: str = ""
        for entrance in self.slot_data_mapped_entrances:
            if portal_entering in entrance[1]:
                flyin_level_name = entrance[0]

        stripped_flyin_name: str = ""
        # Find level name that matches part of the pairing's name
        for env_name in self.env_by_name:
            if env_name in flyin_level_name:
                stripped_flyin_name = env_name

        # At this point, if stripped flyin name is empty, it's the goal level. Set accordingly
        # TODO: remove this once it's in slot data
        if stripped_flyin_name == "":
            goal_option: str = ctx.slot_data["goal"]
            if goal_option == "gnasty":
                stripped_flyin_name = "Gnasty Gnorc"
            elif goal_option == "loot":
                stripped_flyin_name = "Gnasty's Loot"

        return stripped_flyin_name

    def lookup_portal_exit(self, level_exiting_from: str, ctx: "BizHawkClientContext") -> str:
        """Given the name of a level exiting from, return the corresponding name of the entrance portal

        Args:
            level_exiting_from: The name of the level being exited from
            ctx: BizhawkClientContext

        Returns:
            The name of the portal that led to this level, which is the name of the vanilla level it leads to
        """
        # Iterate through levels to find the fly-in entrance that contains the given level name
        # and set hub_entrance_portal_name to hold the corresponding portal for the next step
        hub_entrance_portal_name: str = ""
        for entrance in self.slot_data_mapped_entrances:
            if level_exiting_from in entrance[0]:
                hub_entrance_portal_name = entrance[1]

        # Iterate through levels to get the name of the portal that led to the current level
        # and return it
        stripped_portal_name: str = ""
        for env_name in self.env_by_name:
            if env_name in hub_entrance_portal_name:
                stripped_portal_name = env_name

        # At this point, if it's the goal level being looked up, stripped portal name will be empty (until properly
        # adding it to slot data, will do later)
        # TODO: remove once in slot data
        if stripped_portal_name == "":
            goal_option: str = ctx.slot_data["goal"]
            if goal_option == "gnasty":
                stripped_portal_name = "Gnasty Gnorc"
            elif goal_option == "loot":
                stripped_portal_name = "Gnasty's Loot"

        return stripped_portal_name

    def show_access(self, ctx: "BizHawkClientContext") -> list[tuple[int, bytes]]:
        """Returns a list of writes to be performed to edit level/hub names to show on portals or in the inventory
        screen that they are accessible and whether they have unchecked locations within

        Args:
            ctx: BizhawkClientContext

        Returns:
            List of writes to perform in the format (address, bytes to write)
        """
        write_list: list[tuple[int, bytes]] = []
        first_char: bytes
        # '.' is locked, '!' is unlocked and has unchecked locations, vanilla first character otherwise

        for env in self.env_by_id.values():
            first_char = b'.'  # Default this to locked, override further in as needed
            env_locations: list[str] = []

            if env.is_hub():
                # Compile a list of unchecked locations for the current hub
                env_locations = []
                for name, loc_id in location_name_to_id.items():
                    if (env.name in name) and (loc_id not in ctx.checked_locations):
                        env_locations.append(name)

                if env.name == "Gnasty's World":
                    if len(self.boss_items) == 5:
                        if len(env_locations) > 0:
                            first_char = b'!'
                        else:
                            first_char = env.name[:1].encode("ASCII")
                else:
                    if env.name in self.ap_unlocked_worlds:
                        if len(env_locations) > 0:
                            first_char = b'!'
                        else:
                            first_char = env.name[:1].encode("ASCII")

                write_list.append((env.text_offset, first_char))

            else:  # This is a level
                level_name: str = env.name

                # If portal shuffle is on, replace level name with the level the portal leads to
                if len(self.slot_data_mapped_entrances) > 0:
                    level_name = self.lookup_portal_leads_to(level_name, ctx)

                # Compile a list of unchecked locations behind the given portal
                env_locations = []
                for name, loc_id in location_name_to_id.items():
                    if (level_name in name) and (loc_id not in ctx.checked_locations):
                        env_locations.append(name)

                if self.portal_accesses[env.name]:
                    if len(env_locations) > 0:
                        first_char = b'!'
                    else:
                        first_char = env.name[:1].encode("ASCII")

                write_list.append((env.text_offset, first_char))

        return write_list

    async def process_received_items(self, received_list: list[NetworkItem], ctx: "BizHawkClientContext") -> None:
        """Processes items received from the Archipelago server.

        Args:
            received_list: Usually just ctx.items_received
            ctx: BizhawkClientContext
        """
        for item in received_list:
            item_name = item_id_to_name[item.item]

            if item_name in goal_item:
                await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
            elif item_name in homeworld_access:
                self.ap_unlocked_worlds.add(item_name)
            elif item_name in boss_items:
                self.boss_items.add(item_id_to_name[item.item])
            else:
                try:
                    env: Environment = self.env_by_name[item_name]
                    self.portal_accesses[env.name] = True
                except KeyError:
                    # Wasn't a level access item, do stuff here
                    pass
