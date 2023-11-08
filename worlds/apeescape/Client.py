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

    monkeyaddrs = {
        1: { #1-1
            1: 0x0DFE00,
            3: 0x0DFE02,
            2: 0x0DFE01,
            4: 0x0DFE03
        },
        2: { #1-2
            5: 0x0DFE00,
            6: 0x0DFE01,
            7: 0x0DFE03,
            10: 0x0DFE04,
            9: 0x0DFE05,
            8: 0x0DFE02
        },
        3: { #1-3
            11: 0x0DFE00,
            12: 0x0DFE01,
            17: 0x0DFE03,
            13: 0x0DFE02
        },
        4: { #3 sub area
            14: 0x0DFE19,
            15: 0x0DFE18
        },
        5: { #3 sub area
            16: 0x0DFE30
        },
        6: { #2-1
            18: 0x0DFE00,
            19: 0x0DFE01,
            20: 0x0DFE02
        },
        7: { #6 sub area
            29: 0x0DFE18,
            30: 0x0DFE1A,
            31: 0x0DFE19
        },
        8: { #6 sub area
            23: 0x0DFE32,
            21: 0x0DFE30,
            22: 0x0DFE31
        },
        9: { #6 sub area
            24: 0x0DFE49,
            25: 0x0DFE48,
            26: 0x0DFE4A
        },
        10: { #6 sub area
            27: 0x0DFE61,
            28: 0x0DFE60
        },
        11: { #2-2
            32: 0x0DFE04,
            33: 0x0DFE00,
            34: 0x0DFE03,
            37: 0x0DFE01,
            42: 0x0DFE02
        },
        12: { #sub area of 11
            35: 0x0DFE18,
            36: 0x0DFE19
        },
        13: { #sub area of 11
            38: 0x0DFE32,
            41: 0x0DFE30,
            43: 0x0DFE31
        },
        14: { #sub area of 11
            39: 0x0DFE48,
            40: 0x0DFE49,
            44: 0x0DFE4A
        },
        15: { #2-3
            49: 0x0DFE01,
            51: 0x0DFE00
        },
        16: { #sub area of 15
            45: 0x0DFE18
        },
        17: { #sub area of 15
            47: 0x0DFE30,
            50: 0x0DFE32,
            46: 0x0DFE31
        },
        18: { #sub area of 16
            48: 0x0DFE48,
            52: 0x0DFE49
        },
        20: { #4-1
            53: 0x0DFE00,
            54: 0x0DFE01,
            55: 0x0DFE02,
            56: 0x0DFE03
        },
        21: { #sub area of 20
            57: 0x0DFE18,
            58: 0x0DFE1A,
            59: 0x0DFE1B,
            60: 0x0DFE19
        },
        22: { #4-2
            61: 0x0DFE00,
            62: 0x0DFE01,
            63: 0x0DFE02, #doesn't match ign
            64: 0x0DFE03
        },
        23: { #sub area 22
            65: 0x0DFE18,
            67: 0x0DFE19, #doesn't match ign
            66: 0x0DFE1B,
            68: 0x0DFE1A
        },
        24: { #4-3
            69: 0x0DFE01,
            70: 0x0DFE00
        },
        25: {
            71: 0x0DFE19,
            77: 0x0DFE18,
            78: 0x0DFE1A
        },
        26: {
            72: 0x0DFE30,
            73: 0x0DFE31,
            74: 0x0DFE32,
            75: 0x0DFE33,
            76: 0x0DFE34
        },
        27: {
            79: 0x0DFE48
        },
        28: {

        },
        29: { #5-1
            80: 0x0DFE00,
            81: 0x0DFE01,
            83: 0x0DFE02,
            84: 0x0DFE04,
            85: 0x0DFE05,
            82: 0x0DFE03
        },
        30: { #5-2
            86: 0x0DFE00,
            87: 0x0DFE01
        },
        32: {
            88: 0x0DFE30,
            89: 0x0DFE32,
            90: 0x0DFE31
        },
        31: {
            91: 0x0DFE18,
            92: 0x0DFE1A,
            93: 0x0DFE19,
            94: 0x0DFE1B
        },
        33: { #5-3
            95: 0x0DFE00,
            96: 0x0DFE01,
            99: 0x0DFE02,
            100: 0x0DFE03
        },
        35: {
            97: 0x0DFE31,
            98: 0x0DFE30
        },
        34: {
            101: 0x0DFE18,
            102: 0x0DFE19,
            103: 0x0DFE1A
        },
        37: { #7-1
            104: 0x0DFE00,
            105: 0x0DFE01,
            106: 0x0DFE02,
            107: 0x0DFE03
        },
        38: {
            108: 0x0DFE1A,
            109: 0x0DFE19,
            110: 0x0DFE18,
            114: 0x0DFE1B,
            115: 0x0DFE1C
        },
        39: {
            111: 0x0DFE31,
            112: 0x0DFE32,
            113: 0x0DFE30
        },
        40: { #7-2
            116: 0x0DFE00,
            117: 0x0DFE01
        },
        41: {
            118: 0x0DFE18,
            119: 0x0DFE19,
            120: 0x0DFE1A
        },
        42: {
            121: 0x0DFE30
        },
        43: {
            122: 0x0DFE49,
            123: 0x0DFE48,
            124: 0x0DFE60,
            125: 0x0DFE61
        },
        45: { #7-3
            126: 0x0DFE02,
            127: 0x0DFE00,
            131: 0x0DFE03,
            137: 0x0DFE04,
            136: 0x0DFE01
        },
        46: {
            132: 0x0DFE18,
            133: 0x0DFE1B,
            134: 0x0DFE1A,
            135: 0x0DFE19
        },
        47: {
            141: 0x0DFE30,
            142: 0x0DFE31,
            143: 0x0DFE32
        },
        49: {
            144: 0x0DFE61,
            145: 0x0DFE60
        },
        50: {
            138: 0x0DFE78,
            139: 0x0DFE79,
            140: 0x0DFE7A
        },
        51: {
            128: 0x0DFE92,
            129: 0x0DFE91,
            130: 0x0DFE90
        },
        53: { #8-1
            146: 0x0DFE00,
            147: 0x0DFE03,
            149: 0x0DFE01,
            148: 0x0DFE02
        },
        54: {
            152: 0x0DFE19,
            151: 0x0DFE18,
            150: 0x0DFE1A
        },
        55: {
            155: 0x0DFE32,
            154: 0x0DFE30,
            156: 0x0DFE33,
            157: 0x0DFE34,
            153: 0x0DFE31,
            158: 0x0DFE35
        },
        56: { #8-2
            160: 0x0DFE00,
            159: 0x0DFE01
        },
        57: {
            162: 0x0DFE18
        },
        58: {
            161: 0x0DFE30
        },
        59: {
            164: 0x0DFE49,
            167: 0x0DFE4A,
            168: 0x0DFE48
        },
        61: {
            165: 0x0DFE79,
            166: 0x0DFE78
        },
        62: {
            163: 0x0DFE90
        },
        63: { #8-3
            169: 0x0DFE00
        },
        64: {
            173: 0x0DFE19,
            172: 0x0DFE18
        },
        65: {
            170: 0x0DFE30,
            171: 0x0DFE31
        },
        66: {
            175: 0x0DFE48,
            174: 0x0DFE49,
            176: 0x0DFE4A
        },
        67: {
            177: 0x0DFE60,
            178: 0x0DFE62,
            179: 0x0DFE63,
            180: 0x0DFE61
        },
        69: {

        },
        70: {

        },
        71: {

        },
        72: {
            185: 0x0DFE00
        },
        73: {

        },
        74: {

        },
        75: {
            186: 0x0DFE48
        },
        76: {
            187: 0x0DFE60,
            188: 0x0DFE61,
            189: 0x0DFE62
        },
        77: {
            181: 0x0DFE01,
            182: 0x0DFE00,
            183: 0x0DFE02,
            184: 0x0DFE03
        },
        78: {
            190: 0x0DFE00
        },
        79: {
            192: 0x0DFE18,
            193: 0x0DFE19
        },
        80: {
            194: 0x0DFE30,
            195: 0x0DFE32,
            196: 0x0DFE31,
            197: 0x0DFE33
        },
        81: {
            201: 0x0DFE48,
            202: 0x0DFE49
        },
        82: {
            203: 0x0DFE60,
            204: 0x0DFE61
        },
        83: {

        },
        84: {
            198: 0x0DFE90,
            199: 0x0DFE91,
            200: 0x0DFE92
        },
        85: {
            191: 0x0DFEA8
        },
        86: {

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
