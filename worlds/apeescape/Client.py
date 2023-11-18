from typing import TYPE_CHECKING, Optional, Dict, Set, ClassVar

from NetUtils import ClientStatus
import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

from worlds.apeescape.RAMAddress import RAM

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
    gamestateaddr = 0x0F4470 #0B in level, 0A loading, 09 Menu, 0C stage clear
    levelunlockaddr = 0x0DFC70
    levelglobal = 0
    worldkeycount = 0
    boss1flag = 0
    boss2flag = 0
    boss3flag = 0
    boss4flag = 0

    requiredmonkeyaddr = 0x0F44D8
    hundomonkeyaddr = 0x0F44D6

    monkeyaddrs = RAM.monkeyListLocal




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
        self.levelglobal = int.from_bytes(((await bizhawk.read(ctx.bizhawk_ctx, [
            (self.leveladdr, 1, "MainRAM")
        ])))[0],byteorder='little')

        return True

    async def set_auth(self, ctx: BizHawkClientContext) -> None:
        x = 3

    async def game_watcher(self, ctx: BizHawkClientContext) -> None:
        try:
            hundocount = ((await bizhawk.read(ctx.bizhawk_ctx,[
                (self.hundomonkeyaddr, 1, "MainRAM")
                ])))[0]

            await bizhawk.write(ctx.bizhawk_ctx, [
                (self.trainingroomaddr, (0xFF).to_bytes(1, "little"), "MainRAM"),
                (self.requiredmonkeyaddr, hundocount, "MainRAM")
            ])

            gadgetstate = int.from_bytes(((await bizhawk.read(ctx.bizhawk_ctx, [
                (self.gadgetaddr, 1, "MainRAM")
            ])))[0], byteorder="little")


            self.worldkeycount = 0
            self.boss1flag = 0
            self.boss2flag = 0

            bosses = ((await bizhawk.read(ctx.bizhawk_ctx, [
                (self.levelunlockaddr + 6, 1, "MainRAM"),
                (self.levelunlockaddr + 13, 1, "MainRAM")
            ])))

            if int.from_bytes(bosses[0], byteorder="little") == 1:
                self.boss1flag = 1
            if int.from_bytes(bosses[1], byteorder="little") == 1:
                self.boss2flag = 1


            for item in ctx.items_received:
                if (item.item-self.offset) >= 0x1 and (item.item-self.offset) <= 0x80:
                    if gadgetstate | (item.item-self.offset) != gadgetstate:
                        gadgetstate = gadgetstate | (item.item-self.offset)
                        gadgetstate = gadgetstate | 3
                elif item.item-self.offset == 0x100:
                    self.worldkeycount = self.worldkeycount + 1

            if self.worldkeycount == 0:
                await bizhawk.write(ctx.bizhawk_ctx, [
                    (self.levelunlockaddr, (0x030303).to_bytes(3, "little"), "MainRAM") #w1
                ])
            elif self.worldkeycount == 1:
                await bizhawk.write(ctx.bizhawk_ctx, [
                    (self.levelunlockaddr, (0x010101).to_bytes(3, "little"), "MainRAM"), #w1
                    (self.levelunlockaddr+3, (0x030303).to_bytes(3, "little"), "MainRAM") #w2
                ])
            #elif self.worldkeycount >= 2 and self.boss1flag == 0:
            #    #do a check that boss 1 complete
            #    await bizhawk.write(ctx.bizhawk_ctx, [
            #        (self.levelunlockaddr, (0x010101).to_bytes(3, "little"), "MainRAM"),
            #        (self.levelunlockaddr + 3, (0x010101).to_bytes(3, "little"), "MainRAM"),
            #        #(self.levelunlockaddr + 6, (0x03).to_bytes(1, "little"), "MainRAM")
            #    ])
            elif self.worldkeycount == 2:
                #do a check that boss 1 complete
                await bizhawk.write(ctx.bizhawk_ctx, [
                    (self.levelunlockaddr, (0x010101).to_bytes(3, "little"), "MainRAM"), #w1
                    (self.levelunlockaddr + 3, (0x010101).to_bytes(3, "little"), "MainRAM"), #w2
                    (self.levelunlockaddr + 6, (0x01).to_bytes(1, "little"), "MainRAM"), #w3
                    (self.levelunlockaddr + 7, (0x030303).to_bytes(3, "little"), "MainRAM") #w4
                ])
            elif self.worldkeycount == 3:
                await bizhawk.write(ctx.bizhawk_ctx, [
                    (self.levelunlockaddr, (0x010101).to_bytes(3, "little"), "MainRAM"), #w1
                    (self.levelunlockaddr + 3, (0x010101).to_bytes(3, "little"), "MainRAM"), #w2
                    (self.levelunlockaddr + 6, (0x01).to_bytes(1, "little"), "MainRAM"), #w3
                    (self.levelunlockaddr + 7, (0x010101).to_bytes(3, "little"), "MainRAM"), #w4
                    (self.levelunlockaddr + 10, (0x030303).to_bytes(3, "little"), "MainRAM") #w5
                ])
            #elif self.worldkeycount >= 4:
            #    await bizhawk.write(ctx.bizhawk_ctx, [
            #        (self.levelunlockaddr, (0x010101).to_bytes(3, "little"), "MainRAM"),
            #        (self.levelunlockaddr + 3, (0x010101).to_bytes(3, "little"), "MainRAM"),
            #        (self.levelunlockaddr + 6, (0x01).to_bytes(1, "little"), "MainRAM"),
            #        (self.levelunlockaddr + 7, (0x010101).to_bytes(3, "little"), "MainRAM"),
            #        (self.levelunlockaddr + 10, (0x010101).to_bytes(3, "little"), "MainRAM"),
            #        (self.levelunlockaddr + 13, (0x03).to_bytes(1, "little"), "MainRAM")
            #    ])
            elif self.worldkeycount == 4:
                await bizhawk.write(ctx.bizhawk_ctx, [
                    (self.levelunlockaddr, (0x010101).to_bytes(3, "little"), "MainRAM"),
                    (self.levelunlockaddr + 3, (0x010101).to_bytes(3, "little"), "MainRAM"),
                    (self.levelunlockaddr + 6, (0x01).to_bytes(1, "little"), "MainRAM"),
                    (self.levelunlockaddr + 7, (0x010101).to_bytes(3, "little"), "MainRAM"),
                    (self.levelunlockaddr + 10, (0x010101).to_bytes(3, "little"), "MainRAM"),
                    (self.levelunlockaddr + 13, (0x01).to_bytes(1, "little"), "MainRAM"),
                    (self.levelunlockaddr + 14, (0x030303).to_bytes(3, "little"), "MainRAM")
                ])
            elif self.worldkeycount == 5:
                await bizhawk.write(ctx.bizhawk_ctx, [
                    (self.levelunlockaddr, (0x010101).to_bytes(3, "little"), "MainRAM"),
                    (self.levelunlockaddr + 3, (0x010101).to_bytes(3, "little"), "MainRAM"),
                    (self.levelunlockaddr + 6, (0x01).to_bytes(1, "little"), "MainRAM"),
                    (self.levelunlockaddr + 7, (0x010101).to_bytes(3, "little"), "MainRAM"),
                    (self.levelunlockaddr + 10, (0x010101).to_bytes(3, "little"), "MainRAM"),
                    (self.levelunlockaddr + 13, (0x01).to_bytes(1, "little"), "MainRAM"),
                    (self.levelunlockaddr + 14, (0x010101).to_bytes(3, "little"), "MainRAM"),
                    (self.levelunlockaddr + 17, (0x03).to_bytes(1, "little"), "MainRAM"),
                    (self.levelunlockaddr + 20, (0x0303).to_bytes(2, "little"), "MainRAM")
                ])
            elif self.worldkeycount == 6:
                await bizhawk.write(ctx.bizhawk_ctx, [
                    (self.levelunlockaddr, (0x010101).to_bytes(3, "little"), "MainRAM"),
                    (self.levelunlockaddr + 3, (0x010101).to_bytes(3, "little"), "MainRAM"),
                    (self.levelunlockaddr + 6, (0x01).to_bytes(1, "little"), "MainRAM"),
                    (self.levelunlockaddr + 7, (0x010101).to_bytes(3, "little"), "MainRAM"),
                    (self.levelunlockaddr + 10, (0x010101).to_bytes(3, "little"), "MainRAM"),
                    (self.levelunlockaddr + 13, (0x01).to_bytes(1, "little"), "MainRAM"),
                    (self.levelunlockaddr + 14, (0x010101).to_bytes(3, "little"), "MainRAM"),
                    (self.levelunlockaddr + 17, (0x01).to_bytes(1, "little"), "MainRAM"),
                    (self.levelunlockaddr + 20, (0x0101).to_bytes(2, "little"), "MainRAM"),
                    (self.levelunlockaddr + 22, (0x03).to_bytes(1, "little"), "MainRAM")
                ])

            await bizhawk.write(ctx.bizhawk_ctx, [
                (self.gadgetaddr, (gadgetstate|3).to_bytes(1, "little"), "MainRAM")
            ])





            readresult = ((await bizhawk.read(ctx.bizhawk_ctx,[
                (self.gamestateaddr, 1, "MainRAM"),
                (self.leveladdr, 1, "MainRAM")
                ])))

            gamestate = int.from_bytes(readresult[0], byteorder='little')
            level = int.from_bytes(readresult[1], byteorder='little')

            if (gamestate == 0xC or gamestate == 0xD) and level == 86:
                victory = set()
                victory.add(205+self.offset)
                await ctx.send_msgs([{
                    "cmd": "LocationChecks",
                    "locations": list(x for x in victory)
                }])
                await ctx.send_msgs([{
                    "cmd": "StatusUpdate",
                    "status": ClientStatus.CLIENT_GOAL
                }])
            elif (gamestate == 0x09 and (level != 88 and level != 255)) or gamestate == 0x0C: #quitting level
                monkeyaddrs = self.monkeyaddrs[level]
                key_list = list(monkeyaddrs.keys())
                val_list = list(monkeyaddrs.values())

                addresses = [(1,1,""),(1,1,"")]

                for val in val_list:
                    tuple1 = (val, 1, "MainRAM")
                    addresses.append(tuple1)

                addresses.pop(0)
                addresses.pop(0)

                readmonkeys = ((await bizhawk.read(ctx.bizhawk_ctx, addresses)))
                monkeys_to_send = set()



                for i in range(len(readmonkeys)):
                    if int.from_bytes(readmonkeys[i], byteorder='little') == 0x02:
                        #position = val_list.index(monkeyaddrs[i])

                        monkeys_to_send.add(key_list[i] + self.offset)

                if monkeys_to_send is not None:
                    levelbase = 0
                    await ctx.send_msgs([{
                        "cmd": "LocationChecks",
                        "locations": list(x+levelbase for x in monkeys_to_send)
                    }])
            elif level != self.levelglobal and (level != 88 and level != 255 and self.levelglobal != 88 and self.levelglobal != 255):
                monkeyaddrs = self.monkeyaddrs[self.levelglobal]
                key_list = list(monkeyaddrs.keys())
                val_list = list(monkeyaddrs.values())

                addresses = [(1, 1, ""), (1, 1, "")]

                for val in val_list:
                    tuple1 = (val, 1, "MainRAM")
                    addresses.append(tuple1)

                addresses.pop(0)
                addresses.pop(0)

                readmonkeys = ((await bizhawk.read(ctx.bizhawk_ctx, addresses)))
                monkeys_to_send = set()

                for i in range(len(readmonkeys)):
                    if int.from_bytes(readmonkeys[i], byteorder='little') == 0x02:
                        # position = val_list.index(monkeyaddrs[i])

                        monkeys_to_send.add(key_list[i] + self.offset)

                if monkeys_to_send is not None:
                    levelbase = 0
                    await ctx.send_msgs([{
                        "cmd": "LocationChecks",
                        "locations": list(x + levelbase for x in monkeys_to_send)
                    }])


            self.levelglobal = level






        except bizhawk.RequestFailedError:
            # Exit handler and return to main loop to reconnect
            pass
