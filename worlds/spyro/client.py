import logging
import struct

from typing import TYPE_CHECKING
try:
    from typing import final, override
except ImportError:
    if TYPE_CHECKING:
        from typing import final, override
    else:
        from typing_extensions import final, override

from NetUtils import ClientStatus
import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

from .addresses import RAM, menu_lookup, Environment, internal_id_to_offset
from .locations import location_name_to_id
from .items import item_id_to_name, boss_items, homeworld_access, goal_item

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext

logger = logging.getLogger("Client")


@final
class SpyroClient(BizHawkClient):
    game = "Spyro the Dragon"
    system = "PSX"
    patch_suffix = ""

    local_checked_locations: set[int] = set()
    slot_data_spyro_color: bytes | None = None

    ap_unlocked_worlds: set[str] = set()
    boss_items: set[str] = set()

    gem_counts: dict[int, int] = {}
    """Keeps track of gem counts, indexed by level ID"""

    vortexes_reached: dict[int, int] = {}
    """Keeps track of reached vortices, indexed by level ID"""

    portal_accesses: dict[str, bool] = {}
    """Keeps track of portal access, indexed by level name"""

    hub: Environment
    for hub in RAM.hub_environments:
        gem_counts[hub.internal_id] = 0
        level: Environment
        for level in hub.child_environments:
            portal_accesses[level.name] = False
            gem_counts[level.internal_id] = 0

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
        # TODO: Add helper function for sending locations, to prevent
        # DDOSing the AP server late game
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

        for item in ctx.items_received:
            item_name = item_id_to_name[item.item]

            if item_name in goal_item:
                await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
            elif item_name in homeworld_access:
                self.ap_unlocked_worlds.add(item_name)
            elif item_name in boss_items:
                self.boss_items.add(item_id_to_name[item.item])
            else:
                for hub in RAM.hub_environments:
                    for level in hub.child_environments:
                        if level.name == item_name:
                            self.portal_accesses[level.name] = True

        if self.slot_data_spyro_color is None:
            color_string = ctx.slot_data["spyro_color"]
            if color_string is not None:
                color_value: int = int(color_string, 16)
                self.slot_data_spyro_color = color_value.to_bytes(4, byteorder="big")

        try:
            to_read_list: list[tuple[int, int]] = [
                (RAM.last_received_archipelago_id, 4),
                (RAM.cur_game_state, 1),
                (RAM.cur_level_id, 1),
                (RAM.spyro_color_filter, 4),
                (RAM.gnasty_anim_flag, 1),
                (RAM.unlocked_worlds, 6),
                (RAM.balloonist_menu_choice, 1)
            ]

            gem_counter_offset = len(to_read_list)

            for hub in RAM.hub_environments:
                to_read_list.append((hub.gem_counter, 2))
                for level in hub.child_environments:
                    to_read_list.append((level.gem_counter, 2))

            vortex_offset = len(to_read_list)

            for hub in RAM.hub_environments:
                to_read_list.append((hub.vortex_pointer, 2))  # These never get set, but needed to keep offsets right
                for level in hub.child_environments:
                    to_read_list.append((level.vortex_pointer, 2))

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

            for hub in RAM.hub_environments:
                ram_data_offset = gem_counter_offset + internal_id_to_offset(hub.internal_id)
                self.gem_counts[hub.internal_id] = self.little_bytes(ram_data[ram_data_offset])

                for level in hub.child_environments:
                    ram_data_offset = gem_counter_offset + internal_id_to_offset(level.internal_id)
                    self.gem_counts[level.internal_id] = self.little_bytes(ram_data[ram_data_offset])

            for hub in RAM.hub_environments:
                for level in hub.child_environments:
                    ram_data_offset = vortex_offset + internal_id_to_offset(level.internal_id)
                    self.vortexes_reached[level.internal_id] = self.little_bytes(ram_data[ram_data_offset])

            if cur_game_state == RAM.GameStates.GAMEPLAY:
                for hub in RAM.hub_environments:
                    for level in hub.child_environments:
                        if (
                            (level.name == "Gnasty Gnorc")
                            and (cur_level_id == level.internal_id)
                            and (gnasty_anim_flag == RAM.GNASTY_DEFEATED)
                        ):
                            await self.send_location_once("Defeated Gnasty Gnorc", ctx)

            for hub in RAM.hub_environments:
                hub_quarter_count: int = int(hub.total_gems / 4)
                for index in range(1, 5):
                    if self.gem_counts[hub.internal_id] >= (hub_quarter_count * index):
                        await self.send_location_once(f"{hub.name} {25 * index}% Gems", ctx)

                for level in hub.child_environments:
                    if (level.has_vortex) and (self.vortexes_reached[level.internal_id] == 1):
                        await self.send_location_once(f"{level.name} Vortex", ctx)

                    quarter_count: int = int(level.total_gems / 4)

                    for index in range(1, 5):
                        if self.gem_counts[level.internal_id] >= (quarter_count * index):
                            await self.send_location_once(f"{level.name} {25 * index}% Gems", ctx)

            to_write_ingame: list[tuple[int, bytes]] = []
            to_write_menu: list[tuple[int, bytes]] = []
            to_write_balloonist: list[tuple[int, bytes]] = []

            if (
                (cur_game_state == RAM.GameStates.GAMEPLAY)
                and (self.slot_data_spyro_color is not None)
                and (spyro_color.to_bytes(4, "little") != self.slot_data_spyro_color)
            ):
                spyro_color = self.little_bytes(self.slot_data_spyro_color)
                to_write_ingame.append((RAM.spyro_color_filter, spyro_color.to_bytes(4, "little")))

            if (
                (cur_game_state == RAM.GameStates.GAMEPLAY)
                and (unlocked_worlds.count(bytes([0])) > 1)
            ):
                to_write_ingame.append((RAM.unlocked_worlds, bytes([2, 2, 2, 2, 2, 2])))

            if cur_game_state == RAM.GameStates.GAMEPLAY:
                # Overwrite head checking code
                for hub in RAM.hub_environments:
                    if (
                        (hub.internal_id == cur_level_id)
                        and (len(hub.statue_head_checks) > 0)
                    ):
                        for address in hub.statue_head_checks:
                            # NOP out the conditional branches
                            # This forces the statue heads to always open
                            to_write_ingame.append((address, bytes(4)))

            # Lock inaccessible portals
            if cur_game_state == RAM.GameStates.GAMEPLAY:
                for hub in RAM.hub_environments:
                    if cur_level_id == hub.internal_id:
                        for index, level in enumerate(hub.child_environments):
                            if self.portal_accesses[level.name]:
                                to_write_ingame.append((hub.portal_surface_types[index], b'\x06'))
                            else:
                                to_write_ingame.append((hub.portal_surface_types[index], b'\x00'))

            if cur_game_state == RAM.GameStates.TITLE_SCREEN:
                starting_world_value = ctx.slot_data["starting_world"]
                if starting_world_value is not None:
                    starting_world_value += 1
                    starting_world_value *= 10
                    to_write_menu.append((RAM.starting_level_id, starting_world_value.to_bytes(1, "little")))

            if (
                (cur_game_state == RAM.GameStates.GAMEPLAY)
                and (cur_level_id == 10)
            ):
                to_write_ingame.append((RAM.nestor_unskippable, 0x0.to_bytes(1, "little")))

            if cur_game_state == RAM.GameStates.BALLOONIST:
                # Hide world names if inaccessible
                for hub in RAM.hub_environments:
                    byte_val = hub.name[:1].encode("ASCII")

                    if hub.name != "Gnasty's World":
                        if hub.name not in self.ap_unlocked_worlds:
                            byte_val = b'\x00'

                        to_write_balloonist.append((hub.text_offset, byte_val))
                    else:
                        if len(self.boss_items) != 5:
                            byte_val = b'\x00'

                        to_write_balloonist.append((hub.text_offset, byte_val))

                # Prevent access to inaccessible worlds
                for index, hub in enumerate(RAM.hub_environments):
                    if cur_level_id == hub.internal_id:
                        # Rewrite level data pointers to point at mod's area of memory
                        to_write_balloonist.append((hub.balloon_pointers[0], b'\x01'))
                        to_write_balloonist.append((hub.balloon_pointers[1], b'\x08\xf0'))
                        # Turn menu selection number into world index number
                        mapped_choice = menu_lookup(index, balloonist_choice)
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
                RAM.GameStates.GAMEPLAY.to_bytes(1, "little"),
                ctx
            )

            await self.write_on_state(
                to_write_menu,
                RAM.GameStates.TITLE_SCREEN.to_bytes(1, "little"),
                ctx
            )

            await self.write_on_state(
                to_write_balloonist,
                RAM.GameStates.BALLOONIST.to_bytes(1, "little"),
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
        result: list[tuple[int, bytes]] = []

        hub_name: str = "Stay Here"  # default in case it's -1, which is Stay Here anyway.
        if mapped_choice != -1:
            hub_name = RAM.hub_environments[mapped_choice].name

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

    def __init__(self) -> None:
        pass
