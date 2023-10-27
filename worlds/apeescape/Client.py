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
    gamestateaddr = 0x0F4470 #0B in level, 0A loading, 09 Menu
    levelunlockaddr = 0x0DFC70

    monkeyaddrs = {
        1: {
            1: 0x0DFE00,
            2: 0x0DFE02,
            3: 0x0DFE01,
            4: 0x0DFE03
        },
        2: {
            1: 0x0DFE00,
            2: 0x0DFE01,
            3: 0x0DFE03,
            4: 0x0DFE04,
            5: 0x0DFE05,
            6: 0x0DFE02
        },
        3: {
            1: 0x0DFE00,
            2: 0x0DFE01,
            7: 0x0DFE03,
            3: 0x0DFE02
        },
        4: { #3 sub area
            4: 0x0DFE19,
            5: 0x0DFE18
        },
        5: { #3 sub area
            6: 0x0DFE30
        },
        6: {
            1: 0x0DFE00,
            2: 0x0DFE01,
            3: 0x0DFE02
        },
        7: { #6 sub area
            12: 0x0DFE18,
            13: 0x0DFE1A,
            14: 0x0DFE19
        },
        8: { #6 sub area
            6: 0x0DFE32,
            4: 0x0DFE30,
            5: 0x0DFE31
        },
        9: { #6 sub area
            7: 0x0DFE49,
            8: 0x0DFE48,
            9: 0x0DFE4A
        },
        10: { #6 sub area
            10: 0x0DFE61,
            11: 0x0DFE60
        },
        11: {
            1: 0x0DFE04,
            2: 0x0DFE00,
            3: 0x0DFE03,
            6: 0x0DFE01,
            11: 0x0DFE02
        },
        12: { #sub area of 11
            4: 0x0DFE18,
            5: 0x0DFE19
        },
        13: { #sub area of 11
            7: 0x0DFE32,
            10: 0x0DFE30,
            12: 0x0DFE31
        },
        14: { #sub area of 11
            8: 0x0DFE48,
            9: 0x0DFE49,
            13: 0x0DFE4A
        },
        15: {
            5: 0x0DFE01,
            7: 0x0DFE00
        },
        16: { #sub area of 15
            1: 0x0DFE18
        },
        17: { #sub area of 15
            2: 0x0DFE30,
            3: 0x0DFE32,
            6: 0x0DFE31
        },
        18: { #sub area of 16
            4: 0x0DFE48,
            8: 0x0DFE49
        },
        20: {
            1: 0x0DFE00,
            2: 0x0DFE01,
            3: 0x0DFE02,
            4: 0x0DFE03
        },
        21: { #sub area of 20
            5: 0x0DFE18,
            6: 0x0DFE1A,
            7: 0x0DFE1B,
            8: 0x0DFE19
        },
        22: {
            1: 0x0DFE00,
            2: 0x0DFE01,
            7: 0x0DFE02, #doesn't match ign
            4: 0x0DFE03
        },
        23: { #sub area 22
            5: 0x0DFE18,
            3: 0x0DFE19, #doesn't match ign
            6: 0x0DFE1B,
            8: 0x0DFE1A
        }
    }


    def __init__(self) -> None:
        super().__init__()
        self.game = "Ape Escape"

        self.local_checked_locations = set()
        self.local_set_events = {}
        self.local_found_key_items = {}

    async def validate_rom(self, ctx: BizHawkClientContext) -> bool:
        from CommonClient import logger
        ctx.game = self.game
        ctx.items_handling = 0b011
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
                        monkeys_to_send.add(x+self.offset-decrement+1)
                    elif val == 0:
                        decrement = decrement + 1
                if monkeys_to_send is not None:
                    levelbase = 0
                    if level == 1:
                        levelbase = 0
                    elif level == 2:
                        levelbase = 4
                    elif level == 3:
                        levelbase = 10
                    elif level == 6:
                        levelbase = 17
                    elif level == 11:
                        levelbase = 31
                    elif level == 15:
                        levelbase = 44
                    elif level == 20:
                        levelbase = 52
                    elif level == 22:
                        levelbase = 60
                    elif level == 24:
                        levelbase = 68
                    elif level == 29:
                        levelbase = 79
                    elif level == 30:
                        levelbase = 85
                    elif level == 33:
                        levelbase = 94
                    elif level == 37:
                        levelbase = 103
                    elif level == 40:
                        levelbase = 115
                    elif level == 45:
                        levelbase = 125
                    elif level == 53:
                        levelbase = 145
                    elif level == 56:
                        levelbase = 158
                    elif level == 63:
                        levelbase = 168
                    elif level == 69:
                        levelbase = 180


                    await ctx.send_msgs([{
                        "cmd": "LocationChecks",
                        "locations": list(x+levelbase for x in monkeys_to_send)
                    }])






        except bizhawk.RequestFailedError:
            # Exit handler and return to main loop to reconnect
            pass
