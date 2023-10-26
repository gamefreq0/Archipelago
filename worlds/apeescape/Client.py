from typing import TYPE_CHECKING, Optional, Dict, Set, ClassVar

from NetUtils import ClientStatus
import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext
else:
    BizHawkClientContext = object


EXPECTED_ROM_NAME = "ape escape / AP 2"

# These flags are communicated to the tracker as a bitfield using this order.
# Modifying the order will cause undetectable autotracking issues.

class ApeEscapeClient(BizHawkClient):
    game = "Ape Escape"
    system = "PSX"
    local_checked_locations: Set[int]
    local_set_events: Dict[str, bool]
    local_found_key_items: Dict[str, bool]
    goal_flag: int

    offset = 128000000

    gadgetaddr = 0x0F51C4
    trainingroomaddr = 0x0DFDCC
    leveladdr = 0x0F4476
    levelsavebankaddr = 0x0DFC98
    monkeystatesaddr = 0x0DFE00

    def __init__(self) -> None:
        super().__init__()
        self.game = "Ape Escape"
        self.local_checked_locations = set()
        self.local_set_events = {}
        self.local_found_key_items = {}

    async def validate_rom(self, ctx: BizHawkClientContext) -> bool:
        from CommonClient import logger

        return True

    async def set_auth(self, ctx: BizHawkClientContext) -> None:
        x = 3

    async def game_watcher(self, ctx: BizHawkClientContext) -> None:
        try:
            await bizhawk.write(ctx.bizhawk_ctx, [
                (self.trainingroomaddr, (0xFF).to_bytes(1, "little"), "MainRAM")
            ])

            gadgets_to_give = ctx.items_received


            readresult = ((await bizhawk.read(ctx.bizhawk_ctx,[
                (self.monkeystatesaddr, 1, "MainRAM"),
                (self.leveladdr, 1, "MainRAM")
                ])))

            monkeystates = int.from_bytes(readresult[0], byteorder='little')
            level = int.from_bytes(readresult[1], byteorder='little')

            if monkeystates == 4 or monkeystates == 2:
                #level exited, check all monkeys
                readmonkeys = ((await bizhawk.read(ctx.bizhawk_ctx,[
                    (self.monkeystatesaddr, 1, "MainRAM"),
                    (self.monkeystatesaddr+1, 1, "MainRAM"),
                    (self.monkeystatesaddr+2, 1, "MainRAM"),
                    (self.monkeystatesaddr+3, 1, "MainRAM"),
                    (self.monkeystatesaddr+4, 1, "MainRAM"),
                    (self.monkeystatesaddr+5, 1, "MainRAM"),
                    (self.monkeystatesaddr+6, 1, "MainRAM"),
                    (self.monkeystatesaddr+7, 1, "MainRAM"),
                    (self.monkeystatesaddr+8, 1, "MainRAM"),
                    (self.monkeystatesaddr+9, 1, "MainRAM"),
                    (self.monkeystatesaddr+10, 1, "MainRAM"),
                    (self.monkeystatesaddr+11, 1, "MainRAM"),
                    (self.monkeystatesaddr+12, 1, "MainRAM"),
                    (self.monkeystatesaddr+13, 1, "MainRAM"),
                    (self.monkeystatesaddr+14, 1, "MainRAM"),
                    (self.monkeystatesaddr+15, 1, "MainRAM"),
                    (self.monkeystatesaddr+16, 1, "MainRAM"),
                    (self.monkeystatesaddr+17, 1, "MainRAM"),
                    (self.monkeystatesaddr+18, 1, "MainRAM"),
                    (self.monkeystatesaddr+19, 1, "MainRAM")
                    ])))
                monkeys_to_send = set()
                decrement = 0
                for x in range(20):
                    val = int.from_bytes(readmonkeys[x], byteorder='little')
                    if val == 2:
                        monkeys_to_send.add(x+self.offset-decrement)
                    elif val == 0:
                        decrement = decrement + 1
                if monkeys_to_send is not None:
                    await ctx.send_msgs([{
                        "cmd": "LocationsChecks",
                        "locations": list(monkeys_to_send)
                    }])






        except bizhawk.RequestFailedError:
            # Exit handler and return to main loop to reconnect
            pass
