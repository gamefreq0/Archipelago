from collections.abc import Sequence
import logging
import struct

from typing import TYPE_CHECKING
from typing import override
from typing import final

from Utils import int32_as_bytes
import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

from .Addresses import RAM

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
        batched_reads: list[tuple[int, int, str]] = []
        batched_writes: list[tuple[int, int, str]] = []
        # Detect if AP connection made, bail early if not
        if ctx.server is None or ctx.server.socket.closed or ctx.slot_data is None or ctx.auth is None:
            return
        if self.slot_data_spyro_color is None:
            color_string = ctx.slot_data["spyro_color"]
            if color_string is not None:
                color_value: int = int(f"0x{color_string}")
                self.slot_data_spyro_color = color_value.to_bytes(4, "little")
        try:
            to_read_list: list[tuple[int, int]] = [
                (RAM.lastReceivedArchipelagoID, 4),
                (RAM.curGameState, 1),
                (RAM.curLevelID, 1),
                (RAM.spyroColorFilter, 4)
            ]
            for address, size in to_read_list:
                batched_reads.append((address, size, "MainRAM"))
            ram_data = await bizhawk.read(ctx.bizhawk_ctx, batched_reads)

            recv_index = int.from_bytes(ram_data[0], byteorder="little")
            cur_game_state = int.from_bytes(ram_data[1], byteorder="little")
            cur_level_id = int.from_bytes(ram_data[2], byteorder="little")
            spyro_color = int.from_bytes(ram_data[3], byteorder="little")

            to_write_ingame: list[tuple[int, bytes]] = []
            to_write_menu: list[tuple[int, bytes]] = []
            to_write_balloonist: list[tuple[int, bytes]] = []

            if (cur_game_state == RAM.GameStates.GAMEPLAY) and (
                self.slot_data_spyro_color is not None
            ) and (
                spyro_color.to_bytes(4, "little") != self.slot_data_spyro_color
            ):
                spyro_color = int.from_bytes(
                    self.slot_data_spyro_color, "little"
                )
                to_write_ingame.append(
                    (RAM.spyroColorFilter, spyro_color.to_bytes(4, "little"))
                )
            if (cur_game_state == RAM.GameStates.TITLE_SCREEN):
                starting_world_value = ctx.slot_data["starting_world"]
                if starting_world_value is not None:
                    starting_world_value += 1
                    starting_world_value *= 10
                    to_write_menu.append(
                        (RAM.startingLevelID, starting_world_value)
                    )
            if (cur_game_state == RAM.GameStates.GAMEPLAY) and (
                cur_level_id == 10
            ):
                to_write_ingame.append(
                    (RAM.nestorUnskippable, 0x0.to_bytes(1, "little"))
                )

            await self.WriteOnState(
                to_write_ingame,
                RAM.GameStates.GAMEPLAY.value.to_bytes(1, "little"),
                ctx
            )
            await self.WriteOnState(
                to_write_menu,
                RAM.GameStates.TITLE_SCREEN.value.to_bytes(1, "little"),
                ctx
            )

        except bizhawk.RequestFailedError:
            pass

    async def WriteOnState(
        self,
        write_list: list[tuple[int, bytes]],
        state: bytes,
        ctx: BizHawkClientContext
    ) -> None:
        """Does a guarded write based on the current game state.
        write_list: a list of tuples in the form of (address, bytes)
        state: the byte representing the game state to check for
        ctx: the BizHawkClientContext, needed for the guarded write
        """
        to_write_list: list[tuple[int, bytes, str]] = []
        for item in write_list:
            to_write_list.append((item[0], item[1], "MainRAM"))
        if len(write_list) > 0:
            _ = await bizhawk.guarded_write(
                ctx.bizhawk_ctx, to_write_list, [
                    (
                        RAM.curGameState, state, "MainRAM"
                    )
                ]
            )

    def __init__(self) -> None:
        pass
