import logging
import struct

from typing_extensions import override, final, TYPE_CHECKING

from NetUtils import ClientStatus
import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

from .addresses import RAM, menu_lookup
from .locations import location_name_to_id
from .items import item_id_to_name

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

    ap_unlocked_worlds: list[bool] = [False, False, False, False, False]
    boss_items: list[bool] = [False, False, False, False, False]

    gem_counts: dict[int, int] = {}
    """Keeps track of gem counts, indexed by level ID"""

    for hub in RAM.hub_environments:
        gem_counts[hub.internal_id] = 0
        for level in hub.child_environments:
            gem_counts[level.internal_id] = 0

    @override
    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        spyro_id: bytes = struct.pack("<17s", b"BASCUS-94228SPYRO")
        spyro_id_ram_address: int = 0xBA92
        try:
            # Check ROM name
            # Hopefully this keeps the encoding right on big endian machines
            read_bytes: bytes = ((await bizhawk.read(ctx.bizhawk_ctx, [(
                spyro_id_ram_address, len(spyro_id), "MainRAM"
            )])))[0]
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
            match item_id_to_name[item.item]:
                case "Victory":
                    await ctx.send_msgs([{
                        "cmd": "StatusUpdate",
                        "status": ClientStatus.CLIENT_GOAL
                    }])
                case "Artisans":
                    self.ap_unlocked_worlds[0] = True
                case "Peace Keepers":
                    self.ap_unlocked_worlds[1] = True
                case "Magic Crafters":
                    self.ap_unlocked_worlds[2] = True
                case "Beast Makers":
                    self.ap_unlocked_worlds[3] = True
                case "Dream Weavers":
                    self.ap_unlocked_worlds[4] = True
                case "Toasty's Stilts":
                    self.boss_items[0] = True
                case "Shemp's Staff":
                    self.boss_items[1] = True
                case "Blowhard's Beard":
                    self.boss_items[2] = True
                case "Metalhead's Mohawk":
                    self.boss_items[3] = True
                case "Jacques' Ribbon":
                    self.boss_items[4] = True
                case _:
                    pass
        if self.slot_data_spyro_color is None:
            color_string = ctx.slot_data["spyro_color"]
            if color_string is not None:
                color_value: int = int(color_string, 16)
                self.slot_data_spyro_color = color_value.to_bytes(
                    4, byteorder="big"
                )
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
            temp_translation_info: dict[int, int] = {}
            for level_id in self.gem_counts:
                temp_translation_info[level_id] = len(to_read_list)
                for hub in RAM.hub_environments:
                    if hub.internal_id == level_id:
                        to_read_list.append((hub.gem_counter, 2))
                    for level in hub.child_environments:
                        if level.internal_id == level_id:
                            to_read_list.append((level.gem_counter, 2))
            for address, size in to_read_list:
                batched_reads.append((address, size, "MainRAM"))
            ram_data = await bizhawk.read(ctx.bizhawk_ctx, batched_reads)

            recv_index = int.from_bytes(ram_data[0], byteorder="little")
            cur_game_state = int.from_bytes(ram_data[1], byteorder="little")
            cur_level_id = int.from_bytes(ram_data[2], byteorder="little")
            spyro_color = int.from_bytes(ram_data[3], byteorder="little")
            gnasty_anim_flag = int.from_bytes(ram_data[4], byteorder="little")
            unlocked_worlds = ram_data[5]
            balloonist_choice = int.from_bytes(ram_data[6], byteorder="little")
            for level_id, gem_count_index in temp_translation_info.items():
                self.gem_counts[level_id] = int.from_bytes(
                    ram_data[gem_count_index], byteorder="little"
                )
            if cur_game_state == RAM.GameStates.GAMEPLAY:
                for hub in RAM.hub_environments:
                    for level in hub.child_environments:
                        if (
                            (level.name == "Gnasty Gnorc")
                            and (cur_level_id == level.internal_id)
                            and (gnasty_anim_flag == RAM.GNASTY_DEFEATED)
                        ):
                            await self.send_location_once(
                                "Defeated Gnasty Gnorc", ctx
                            )
            for hub in RAM.hub_environments:
                quarter_count: int = int(hub.total_gems / 4)
                if self.gem_counts[hub.internal_id] >= quarter_count:
                    await self.send_location_once(
                        f"{hub.name} 25% Gems", ctx
                    )
                if self.gem_counts[hub.internal_id] >= (quarter_count * 2):
                    await self.send_location_once(
                        f"{hub.name} 50% Gems", ctx
                    )
                if self.gem_counts[hub.internal_id] >= (quarter_count * 3):
                    await self.send_location_once(
                        f"{hub.name} 75% Gems", ctx
                    )
                if self.gem_counts[hub.internal_id] >= hub.total_gems:
                    await self.send_location_once(
                        f"{hub.name} 100% Gems", ctx
                    )

            to_write_ingame: list[tuple[int, bytes]] = []
            to_write_menu: list[tuple[int, bytes]] = []
            to_write_balloonist: list[tuple[int, bytes]] = []

            if (cur_game_state == RAM.GameStates.GAMEPLAY.value) and (
                self.slot_data_spyro_color is not None
            ) and (
                spyro_color.to_bytes(4, "little") != self.slot_data_spyro_color
            ):
                spyro_color = int.from_bytes(
                    self.slot_data_spyro_color, "little"
                )
                to_write_ingame.append(
                    (RAM.spyro_color_filter, spyro_color.to_bytes(4, "little"))
                )
            if (
                (cur_game_state == RAM.GameStates.GAMEPLAY.value)
                and (unlocked_worlds.count(bytes([0])) > 1)
            ):
                to_write_ingame.append(
                    (RAM.unlocked_worlds, bytes([2, 2, 2, 2, 2, 2]))
                )
            if cur_game_state == RAM.GameStates.GAMEPLAY.value:
                # Overwrite head checking code
                for hub in RAM.hub_environments:
                    if (
                        (hub.internal_id == cur_level_id)
                        and (len(hub.statue_head_checks) > 0)
                    ):
                        for address in hub.statue_head_checks:
                            # NOP out the conditional branches
                            # This forces the statue heads to always open
                            to_write_ingame.append(
                                (address, bytes(4))
                            )
            if cur_game_state == RAM.GameStates.TITLE_SCREEN.value:

                starting_world_value = ctx.slot_data["starting_world"]
                if starting_world_value is not None:
                    starting_world_value += 1
                    starting_world_value *= 10
                    to_write_menu.append(
                        (RAM.starting_level_id, starting_world_value.to_bytes(1, "little"))
                    )
            if (cur_game_state == RAM.GameStates.GAMEPLAY.value) and (
                cur_level_id == 10
            ):
                to_write_ingame.append(
                    (RAM.nestor_unskippable, 0x0.to_bytes(1, "little"))
                )
            if cur_game_state == RAM.GameStates.BALLOONIST.value:
                # Hide world names if inaccessible
                for index, hub in enumerate(RAM.hub_environments):
                    byte_val = hub.name[:1].encode("ASCII")
                    if index != 5:
                        if not self.ap_unlocked_worlds[index]:
                            byte_val = b'\x00'
                        to_write_balloonist.append((
                            hub.text_offset, byte_val
                        ))
                    else:
                        if not self.boss_items.count(True) == 5:
                            byte_val = b'x00'
                        to_write_balloonist.append((
                            hub.text_offset, byte_val
                        ))
                # Prevent access to inaccessible worlds
                for index, hub in enumerate(RAM.hub_environments):
                    if cur_level_id == hub.internal_id:
                        # Rewrite level data pointers to point at mod's area of memory
                        to_write_balloonist.append((
                            hub.balloon_pointers[0], b'\x01'
                        ))
                        to_write_balloonist.append((
                            hub.balloon_pointers[1], b'\x08\xf0'
                        ))
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
                        for item in self.set_balloonist_unlocks(
                            mapped_choice, balloonist_choice
                        ):
                            to_write_balloonist.append(item)

            await self.write_on_state(
                to_write_ingame,
                RAM.GameStates.GAMEPLAY.value.to_bytes(1, "little"),
                ctx
            )
            await self.write_on_state(
                to_write_menu,
                RAM.GameStates.TITLE_SCREEN.value.to_bytes(1, "little"),
                ctx
            )
            await self.write_on_state(
                to_write_balloonist,
                RAM.GameStates.BALLOONIST.value.to_bytes(1, "little"),
                ctx
            )

        except bizhawk.RequestFailedError:
            pass

    def balloonist_helper(self, allow: bytes, choice: bytes) -> list[tuple[int, bytes]]:
        result: list[tuple[int, bytes]] = []
        result.append((RAM.fake_timer, allow))
        result.append((RAM.last_selected_valid_choice, choice))
        return result

    def set_balloonist_unlocks(
        self, mapped_choice: int, raw_choice: int
    ) -> list[tuple[int, bytes]]:
        result: list[tuple[int, bytes]] = []
        if (mapped_choice != -1) and (mapped_choice < 5):
            if self.ap_unlocked_worlds[mapped_choice]:
                for item in self.balloonist_helper(
                    b'\x1f', raw_choice.to_bytes(
                        1, byteorder="little"
                    )
                ):
                    result.append(item)
            else:
                for item in self.balloonist_helper(
                    b'\x00', b'\x00'
                ):
                    result.append(item)
        elif mapped_choice == 5:
            if self.boss_items.count(True) == 5:
                for item in self.balloonist_helper(
                    b'\x1f', raw_choice.to_bytes(
                        1, byteorder="little"
                    )
                ):
                    result.append(item)
            else:
                for item in self.balloonist_helper(
                    b'\x00', b'\x00'
                ):
                    result.append(item)
        else:
            for item in self.balloonist_helper(
                b'\x1f', b'\x00'
            ):
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
        """
        to_write_list: list[tuple[int, bytes, str]] = []
        for item in write_list:
            to_write_list.append((item[0], item[1], "MainRAM"))
        if len(write_list) > 0:
            _ = await bizhawk.guarded_write(
                ctx.bizhawk_ctx,
                to_write_list,
                [
                    (
                        RAM.cur_game_state, state, "MainRAM"
                    )
                ]
            )

    async def send_location_once(
        self,
        location_name: str,
        ctx: "BizHawkClientContext"
    ) -> None:
        """Send a location to the server, but only if it hasn't been sent
        before

        Args:
            location_name: The name of the location to send
        """
        location_id = location_name_to_id[location_name]
        if location_id not in ctx.checked_locations:
            logger.info("Sending location")
            await ctx.send_msgs([{
                        "cmd": "LocationChecks",
                        "locations": [location_id]
                    }])

    def __init__(self) -> None:
        pass
