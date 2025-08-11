import logging
import struct

from typing import TYPE_CHECKING

import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext

logger = logging.getLogger("Client")


class SpyroClient(BizHawkClient):
    game = "Spyro the Dragon"
    system = "PSX"

    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        spyro_id = struct.pack("<17s", b"BASCUS-94228SPYRO")
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

    async def game_watcher(self, ctx: "BizHawkClientContext") -> None:
        pass

    def __init__(self) -> None:
        pass
