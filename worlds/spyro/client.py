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
from .world import SlotDataTypes

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext

logger: logging.Logger = logging.getLogger("Client")
CLIENT_VERSION: str = "v0.3.5"  # TODO: Remove before PR to main


class RamReads():
    """Class for holding data related to reads from BizHawk memory
    """

    def __init__(self, address: int, byte_count: int) -> None:
        self.address: int = address
        self.byte_count: int = byte_count
        self.raw_data: bytes = b''
        return

    def value(self) -> int:
        """Return the value of the read data intrepreted as an int from a little-endian representation

        Returns:
            Little-endian int representation of the raw data
        """
        return int.from_bytes(self.raw_data, byteorder="little")


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

    recv_index: RamReads = RamReads(RAM.last_received_archipelago_id, 4)
    """Index of last processed AP item"""

    cur_game_state: RamReads = RamReads(RAM.cur_game_state, 1)
    cur_level_id: RamReads = RamReads(RAM.cur_level_id, 1)
    spyro_color: RamReads = RamReads(RAM.spyro_color_filter, 4)
    gnasty_anim_flag: RamReads = RamReads(RAM.gnasty_anim_flag, 1)
    unlocked_worlds: RamReads = RamReads(RAM.unlocked_worlds, 6)
    balloonist_menu_choice: RamReads = RamReads(RAM.balloonist_menu_choice, 1)
    total_gems_collected: RamReads = RamReads(RAM.total_gem_count, 4)
    did_portal_switch: RamReads = RamReads(RAM.switched_portal_dest, 1)
    spyro_anim: RamReads = RamReads(RAM.spyro_cur_animation, 1)
    last_whirlwind_pointer: RamReads = RamReads(RAM.last_touched_whirlwind, 3)

    gem_counts: list[RamReads] = []
    """Keeps track of gem counts"""

    portal_accesses: dict[str, bool] = {}
    """Keeps track of portal access, indexed by level name"""

    to_write_lists: dict[int, list[tuple[int, bytes]]] = {}
    """A dict of lists of (address, bytes) to write, indexed by the gamestate to guard the writes against"""

    portal_shuffle: bool = False
    """Whether portal shuffle is on"""

    goal: str = ""
    """The name of the current goal"""

    starting_world: int
    """The index of the starting homeworld"""

    did_setup: bool = False
    """Whether we've processed slot data"""

    def __init__(self) -> None:
        for env in self.env_by_id.values():
            self.gem_counts.append(RamReads(env.gem_counter, 2))
            if not env.is_hub():
                self.portal_accesses[env.name] = False

        return

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
            ctx.watcher_timeout = 0.125

        if not self.did_setup:
            self.do_init(ctx)

        # Reset and/or init write lists here
        for game_state in RAM.GameStates:
            self.to_write_lists[game_state] = []

        await self.process_received_items(ctx.items_received, ctx)

        try:
            to_read_list: list[RamReads] = []
            to_read_list.append(self.recv_index)
            to_read_list.append(self.cur_game_state)
            to_read_list.append(self.cur_level_id)
            to_read_list.append(self.spyro_color)
            to_read_list.append(self.gnasty_anim_flag)
            to_read_list.append(self.unlocked_worlds)
            to_read_list.append(self.balloonist_menu_choice)
            to_read_list.append(self.total_gems_collected)
            to_read_list.append(self.did_portal_switch)
            to_read_list.append(self.spyro_anim)
            to_read_list.append(self.last_whirlwind_pointer)
            to_read_list.extend(self.gem_counts)

            for ram_item in to_read_list:
                batched_reads.append((ram_item.address, ram_item.byte_count, "MainRAM"))

            ram_data: list[bytes] = await bizhawk.read(ctx.bizhawk_ctx, batched_reads)

            for ram_item in to_read_list:
                ram_item.raw_data = ram_data.pop(0)

            await self.process_locations(self.cur_game_state.value(), self.cur_level_id.value(), ctx)
            self.update_spyro_color(self.spyro_color.value(), self.cur_game_state.value())
            self.set_internal_worlds_unlocked(self.unlocked_worlds.raw_data)
            self.adjust_level_names(self.cur_game_state.value(), ctx)
            self.reset_portal_switch(self.did_portal_switch.value(), self.cur_level_id.value())

            if self.cur_level_id.value() == 0:  # We're on the title screen or in early load
                self.set_starting_world()
            else:  # We're hopefully in a valid level here

                await self.do_portal_shuffle_changes(
                    self.did_portal_switch.value(),
                    self.spyro_anim.value(),
                    self.cur_level_id.value(),
                    self.last_whirlwind_pointer.value(),
                    ctx
                )

                env: Environment = self.env_by_id[self.cur_level_id.value()]

                # Make Nestor skippable
                if env.name == "Artisans":
                    self.to_write_lists[RAM.GameStates.GAMEPLAY].append((RAM.nestor_unskippable, b'\x00'))

                # Prevent Tuco's warp-to-level shenanigans by setting egg minimum to -1
                if env.name == "Magic Crafters":
                    self.to_write_lists[RAM.GameStates.GAMEPLAY].append((RAM.tuco_egg_minimum, b'\xff\xff'))

                if env.is_hub():
                    self.override_head_checks(env)
                    self.do_hub_portal_mods(env)
                    self.do_balloonist_mods(env, self.balloonist_menu_choice.value())

            for game_state, write_list in self.to_write_lists.items():
                await self.write_on_state(write_list, game_state.to_bytes(1, byteorder="little"), ctx)

        except bizhawk.RequestFailedError:
            # If we don't swallow this exception, we get an ugly exit when BizHawk disconnects from the client
            # Mostly noticeable if we close BizHawk or the connector before the client. Yes, I'm not enthused about this
            # No, I'm not dealing with bug reports from people if we do this the "proper way"
            pass

        return

    def do_init(self, ctx: "BizHawkClientContext") -> None:
        """Do first time setup stuff, like read in slot data into class vars

        Args:
            ctx: BizHawkClientContext
        """
        logger.info("Spyro Client version %s loaded", CLIENT_VERSION)  # TODO: Remove this before PR to main
        if ctx.slot_data is not None:
            slot_data: SlotDataTypes = {
                "goal": "invalid",
                "starting_world": -1,
                "entrances": [],
                "portal_shuffle": -1,
                "spyro_color": 0xffffff00
            }
            for key, value in ctx.slot_data.items():
                slot_data[key] = value
            # Read in Spyro color from slot data
            # TODO: Add in datastorage bit here so the color can be modified during gameplay
            color_value: int
            color_value = slot_data["spyro_color"]
            self.slot_data_spyro_color = color_value.to_bytes(4, byteorder="big")

            # Read in goal from slot data
            self.goal = slot_data["goal"]

            # If portal shuffle is on, read in entrance mappings from slot data and store locally
            entrance_data: list[tuple[str, str]] = slot_data["entrances"]
            if len(entrance_data) > 0:
                self.portal_shuffle = True

                for item in entrance_data:
                    if "Fly-in" in item[0]:  # Skip every other, two-way mapping makes half of it redundant
                        self.slot_data_mapped_entrances.append(item)
            else:
                self.portal_shuffle = False

            # Read in starting homeworld from slot data
            self.starting_world = slot_data["starting_world"]

        self.did_setup = True
        return

    def balloonist_helper(self, should_allow: bool, choice: int) -> list[tuple[int, bytes]]:
        """Build up a list of bytes to write in order to allow/deny the ability to choose the selected choice in the
        balloonist menu

        Args:
            should_allow: Whether the selected option should be allowed to be chosen
            choice: The numeric index of the selected choice in the menu

        Returns:
            The list of bytes to be written in the format (address, bytes)
        """
        # The game checks to see if the timer is above a certain value before allowing a selection. We can abuse this
        # in order to allow/deny choosing an option based on access requirements instead
        fake_timer: bytes = b'\x1f' if should_allow else b'\x00'
        choice_byte: bytes = choice.to_bytes(1, byteorder="little")
        result: list[tuple[int, bytes]] = []
        result.append((RAM.fake_timer, fake_timer))
        result.append((RAM.last_selected_valid_choice, choice_byte))
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
        stay_here: int = 0
        if mapped_choice != -1:
            hub_id = (mapped_choice + 1) * 10
            hub_name = self.env_by_id[hub_id].name

        should_allow_choice: bool
        last_selected_valid_choice: int

        if hub_name == "Stay Here":
            should_allow_choice = True
            last_selected_valid_choice = stay_here
        else:
            if hub_name == "Gnasty's World":
                if len(self.boss_items) == 5:
                    should_allow_choice = True
                    last_selected_valid_choice = raw_choice
                else:
                    should_allow_choice = False
                    last_selected_valid_choice = stay_here
            else:
                if hub_name in self.ap_unlocked_worlds:
                    should_allow_choice = True
                    last_selected_valid_choice = raw_choice
                else:
                    should_allow_choice = False
                    last_selected_valid_choice = stay_here

        for item in self.balloonist_helper(should_allow_choice, last_selected_valid_choice):
            result.append(item)

        return result

    async def write_on_state(
        self,
        write_list: list[tuple[int, bytes]],
        state: bytes,
        ctx: "BizHawkClientContext"
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
        location_id: int = location_name_to_id[location_name]

        if location_id not in ctx.checked_locations:
            await ctx.send_msgs([{"cmd": "LocationChecks", "locations": [location_id]}])

    def from_little_bytes(self, bytes_in: bytes) -> int:
        """Returns an int from the given little-endian bytes

        Args:
            bytes_in: the sequence of bytes to interpret

        Returns:
            Little-endian-interpreted int
        """
        return int.from_bytes(bytes_in, byteorder="little")

    def lookup_portal_leads_to(self, portal_entering: str) -> str:
        """Given the name of a portal a player is entering, return the level the portal should lead to

        Args:
            portal_entering: The portal being walked into

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
            if self.goal == "gnasty":
                stripped_flyin_name = "Gnasty Gnorc"
            elif self.goal == "loot":
                stripped_flyin_name = "Gnasty's Loot"

        return stripped_flyin_name

    def lookup_portal_exit(self, level_exiting_from: str) -> str:
        """Given the name of a level exiting from, return the corresponding name of the entrance portal

        Args:
            level_exiting_from: The name of the level being exited from

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
            if self.goal == "gnasty":
                stripped_portal_name = "Gnasty Gnorc"
            elif self.goal == "loot":
                stripped_portal_name = "Gnasty's Loot"

        return stripped_portal_name

    def show_access(self, game_state: int, ctx: "BizHawkClientContext") -> list[tuple[int, bytes]]:
        """Returns a list of writes to be performed to edit level/hub names to show on portals or in the inventory
        screen that they are accessible and whether they have unchecked locations within

        Args:
            game_state: The current game state
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
                    level_name = self.lookup_portal_leads_to(level_name)

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

                # Ensure vanilla name in loading screens
                if game_state == RAM.GameStates.LOADING:
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
            item_name: str = item_id_to_name[item.item]

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

        return

    async def process_locations(self, game_state: int, cur_level_id: int, ctx: "BizHawkClientContext") -> None:
        """Check the memory of the game and send completed locations based on inventory as needed

        Args:
            game_state: The current state of the game
            cur_level_id: The internal ID of the current level
            ctx: BizHawkClientContext
        """
        if cur_level_id != 0:  # Hopefully prevents weirdness early in game load
            if game_state == RAM.GameStates.GAMEPLAY:
                # Send location on defeating Gnasty
                if self.env_by_id[cur_level_id].name == "Gnasty Gnorc":
                    if self.gnasty_anim_flag.value() == RAM.GNASTY_DEFEATED:
                        await self.send_location_once("Defeated Gnasty Gnorc", ctx)

                # Send 1/4 gem threshold checks
                for env_id, env in self.env_by_id.items():
                    quarter_count: int = int(env.total_gems / 4)

                    for index in range(1, 5):
                        if self.gem_counts[internal_id_to_offset(env_id)].value() >= (quarter_count * index):
                            await self.send_location_once(f"{env.name} {25 * index}% Gems", ctx)

                # Send 500 increment total gem threhshold checks
                for gem_threshold in range(500, total_treasure + 1, 500):
                    if self.total_gems_collected.value() >= gem_threshold:
                        await self.send_location_once(f"{gem_threshold} Gems", ctx)

        return

    def update_spyro_color(self, color: int, game_state: int) -> None:
        """Given an RGBA color as an int, update Spyro's color

        Args:
            color: RGBA value as int
            game_state: current game state
        """
        if self.slot_data_spyro_color != b'':
            if color.to_bytes(4, "little") != self.slot_data_spyro_color:
                new_color: int = self.from_little_bytes(self.slot_data_spyro_color)
                if game_state in (
                    RAM.GameStates.GAMEPLAY,
                    RAM.GameStates.BALLOONIST,
                    RAM.GameStates.DEATH,
                    RAM.GameStates.DRAGON_CUTSCENE,
                    RAM.GameStates.EXITING_LEVEL,
                    RAM.GameStates.FAIRY_TEXTBOX,
                    RAM.GameStates.FLY_IN,
                    RAM.GameStates.GAMEPLAY,
                    RAM.GameStates.TITLE_SCREEN
                ):
                    self.to_write_lists[game_state].append(
                        (RAM.spyro_color_filter, new_color.to_bytes(4, "little"))
                    )

        return

    def set_internal_worlds_unlocked(self, unlocked_worlds: bytes) -> None:
        """Check the game's internal value for unlocked worlds for the balloonist and set all to unlocked

        Args:
            unlocked_worlds: Sequence of bytes holding the game's internal worlds unlocked data
        """
        if unlocked_worlds.count(bytes([0])) > 1:
            self.to_write_lists[RAM.GameStates.GAMEPLAY].append((RAM.unlocked_worlds, bytes([2, 2, 2, 2, 2, 2])))

        return

    def adjust_level_names(self, game_state: int, ctx: "BizHawkClientContext") -> None:
        """Ensure all levels/hub are visible on the inventory screen and have names adjusted to indicate accessibility
        and whether there are checks left in the level/hub

        Args:
            game_state: The current game state
            ctx: BizHawkClientContext
        """
        # Force all levels and hubs to be visible on the inventory screen
        for index in range(len(self.env_by_id)):
            self.to_write_lists[RAM.GameStates.INVENTORY].append((RAM.show_on_inventory_array + index, b'\x01'))

        if game_state in (
            RAM.GameStates.GAMEPLAY,
            RAM.GameStates.INVENTORY,
            RAM.GameStates.LOADING,
        ):
            # Modify level/hub names to indicate accessibility and completion status
            write_list: list[tuple[int, bytes]] = self.show_access(game_state, ctx)
            for item in write_list:
                self.to_write_lists[game_state].append(item)

        return

    def reset_portal_switch(self, did_switch: int, cur_level_id: int):
        """Reset info for tracking whether portal swtich has been handled yet

        Args:
            did_switch: Internal tracking in RAM on whether we cleaned up after the switch
            cur_level_id: The internal ID of the current level
            ctx: BizHawkClientContext
        """
        # If exiting level from menu, and portal shuffle on,
        # change cur_level_id to portal's vanilla level's internal ID
        if (did_switch == 0) and (len(self.slot_data_mapped_entrances) > 0) and (cur_level_id != 0):
            # Turn flag on so we don't remap more than once
            self.to_write_lists[RAM.GameStates.EXITING_LEVEL].append((RAM.switched_portal_dest, b'\x01'))
            hub_entrance_portal_name: str = ""
            cur_level_env: Environment = self.env_by_id[cur_level_id]
            hub_entrance_portal_name = self.lookup_portal_exit(cur_level_env.name)
            id_of_entrance: int = self.env_by_name[hub_entrance_portal_name].internal_id
            self.to_write_lists[RAM.GameStates.EXITING_LEVEL].append(
                (RAM.cur_level_id, id_of_entrance.to_bytes(1, byteorder="little"))
            )

        return

    def set_starting_world(self) -> None:
        """While on the title screen, update the starting level ID to enter on completion of the intro cutscene

        Args:
            ctx: BizHawkClientContext
        """
        starting_world_value: int = self.starting_world
        starting_world_value += 1
        starting_world_value *= 10
        self.to_write_lists[RAM.GameStates.TITLE_SCREEN].append(
            (RAM.starting_level_id, starting_world_value.to_bytes(1, "little"))
        )

    async def do_portal_shuffle_changes(
        self,
        did_switch: int,
        spyro_anim: int,
        cur_level_id: int,
        last_whirlwind_pointer: int,
        ctx: "BizHawkClientContext"
    ) -> None:
        """Handles setting up quit from menu and exit vortexes for portal shuffle, and also sends vortex locations

        Args:
            did_switch: Whether we have handled switching the current level ID, as stored in game RAM
            spyro_anim: Spyro's current animation
            cur_level_id: The current reported internal level ID
            last_whirlwind_pointer: The pointer to the last touched whirlwind
            ctx: BizHawkClientContext
        """
        # Reset this for tracking on next level exit. Can't switch in whirlwind, might be exiting via vortex
        if (
            (did_switch == 1)
            and (spyro_anim != RAM.SpyroStates.WHIRLWIND)
            and not (self.env_by_id[cur_level_id].is_hub())
        ):
            self.to_write_lists[RAM.GameStates.GAMEPLAY].append((RAM.switched_portal_dest, b'\x00'))

        if (
            (spyro_anim == RAM.SpyroStates.WHIRLWIND)
            and (did_switch == 0)
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
                self.to_write_lists[RAM.GameStates.GAMEPLAY].append((RAM.switched_portal_dest, b'\x01'))
                hub_entrance_portal_name: str = ""
                cur_level_env: Environment = self.env_by_id[cur_level_id]
                hub_entrance_portal_name = self.lookup_portal_exit(cur_level_env.name)
                id_of_entrance: int = self.env_by_name[hub_entrance_portal_name].internal_id
                self.to_write_lists[RAM.GameStates.GAMEPLAY].append(
                    (RAM.cur_level_id, id_of_entrance.to_bytes(1, byteorder="little"))
                )

        return

    def override_head_checks(self, env: Environment):
        """Override the code that checks if a dragon head statue should open

        Args:
            env: The current game environment
        """
        if len(env.statue_head_checks) > 0:
            for address in env.statue_head_checks:
                # NOP out the conditional branches
                # This forces the statue heads to always open
                self.to_write_lists[RAM.GameStates.GAMEPLAY].append((address, bytes(4)))

        return

    def do_hub_portal_mods(self, env: Environment):
        """Lock/unlock portals and set portal destinations in a given homeworld

        Args:
            env: The current homeworld environment
            ctx: BizHawkClientContext
        """
        for index, level in enumerate(env.child_environments):
            # Lock inaccessible portals
            if self.portal_accesses[level.name]:
                self.to_write_lists[RAM.GameStates.GAMEPLAY].append(
                    (env.portal_surface_types[index], b'\x06')
                )
            else:
                self.to_write_lists[RAM.GameStates.GAMEPLAY].append(
                    (env.portal_surface_types[index], b'\x00')
                )

            # If portal shuffle is on
            if len(self.slot_data_mapped_entrances) > 0:
                # Modify portal destinations
                dest_level_name: str = self.lookup_portal_leads_to(level.name)
                portal_dest_id: int = self.env_by_name[dest_level_name].internal_id
                self.to_write_lists[RAM.GameStates.GAMEPLAY].append(
                    (env.portal_dest_level_ids[index], portal_dest_id.to_bytes(1, byteorder="little"))
                )

        return

    def do_balloonist_mods(self, env: Environment, balloonist_choice: int) -> None:
        """Show/hide world names in baloonist menu based on accessibility, and allow/deny choosing selected option

        Args:
            env: The current hub's environment
            balloonist_choice: The index of the currently selected option in the balloonist menu
        """
        # Hide world names if inaccessible
        for looped_env in self.env_by_id.values():
            if not looped_env.is_hub():
                continue

            byte_val: bytes = looped_env.name[:1].encode("ASCII")

            if looped_env.name != "Gnasty's World":
                if looped_env.name not in self.ap_unlocked_worlds:
                    byte_val = b'\x00'

                self.to_write_lists[RAM.GameStates.BALLOONIST].append((looped_env.text_offset, byte_val))
            else:
                if len(self.boss_items) != 5:
                    byte_val = b'\x00'

                self.to_write_lists[RAM.GameStates.BALLOONIST].append((looped_env.text_offset, byte_val))

        # Prevent access to inaccessible worlds

        # Rewrite level data pointers to point at mod's area of memory
        self.to_write_lists[RAM.GameStates.BALLOONIST].append((env.balloon_pointers[0], b'\x01'))
        self.to_write_lists[RAM.GameStates.BALLOONIST].append((env.balloon_pointers[1], b'\x0c\xf0'))

        # Turn menu selection number into world index number
        mapped_choice: int = menu_lookup((int(env.internal_id / 10) - 1), balloonist_choice)

        # Poke last valid selected choice number to RAM
        # as well as poking a value to what the game
        # thinks is a timer, which allows selecting a
        # choice when it is >= 0x1f
        # The code is normally meant to prevent a player
        # from choosing an option in the menu within a few
        # frames of the menu opening. We abuse it for
        # setting conditional access instead
        for item in self.set_balloonist_unlocks(mapped_choice, balloonist_choice):
            self.to_write_lists[RAM.GameStates.BALLOONIST].append(item)

        return
