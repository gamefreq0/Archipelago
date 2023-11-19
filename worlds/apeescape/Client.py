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
    levelglobal = 0
    roomglobal = 0
    worldkeycount = 0
    boss1flag = 0
    boss2flag = 0
    boss3flag = 0
    boss4flag = 0

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
            # Get items from server
            gadgetStateFromServer = 3
            keyCountFromServer = 0

            for item in ctx.items_received:
                if 0x1 <= (item.item - self.offset) <= 0x80:
                    if gadgetStateFromServer | (item.item - self.offset) != gadgetStateFromServer:
                        gadgetStateFromServer = gadgetStateFromServer | (item.item - self.offset)
                elif item.item - self.offset == 0x100:
                    keyCountFromServer = keyCountFromServer + 1

            if keyCountFromServer > self.worldkeycount:
                self.worldkeycount = keyCountFromServer

            # Read Array
            # 0: Hundo monkey count, to write to required count
            # 1: Gadget unlocked states
            # 2: Current Room
            # 3: Current Game state
            # 4: Current Level

            readTuples = [
                (RAM.hundoApesAddress, 1, "MainRAM"),
                (RAM.unlockedGadgetsAddress, 1, "MainRAM"),
                (RAM.currentRoomIdAddress, 1, "MainRAM"),
                (RAM.gameStateAddress, 1, "MainRAM"),
                (RAM.currentLevelAddress, 1, "MainRAM")
            ]

            reads = await bizhawk.read(ctx.bizhawk_ctx, readTuples)

            hundoCount = int.from_bytes(reads[0], byteorder="little")
            gadgets = int.from_bytes(reads[1], byteorder="little")
            currentRoom = int.from_bytes(reads[2], byteorder="little")
            gameState = int.from_bytes(reads[3], byteorder="little")
            currentLevel = int.from_bytes(reads[4], byteorder="little")

            # Check if in level select or in time hub, then read global monkeys
            if gameState == RAM.gameState["LevelSelect"] or currentLevel == RAM.levels["Time"]:
                keyList = list(RAM.monkeyListGlobal.keys())
                valList = list(RAM.monkeyListGlobal.values())

                addresses = []

                for val in valList:
                    tuple1 = (val, 1, "MainRAM")
                    addresses.append(tuple1)

                globalMonkeys = await bizhawk.read(ctx.bizhawk_ctx, addresses)
                monkeysToSend = set()

                for i in range(len(globalMonkeys)):
                    if int.from_bytes(globalMonkeys[i], byteorder='little') == RAM.caughtStatus["Caught"]:
                        monkeysToSend.add(keyList[i] + self.offset)

                if monkeysToSend is not None:
                    await ctx.send_msgs([{
                        "cmd": "LocationChecks",
                        "locations": list(x for x in monkeysToSend)
                    }])

            # elif changing room but still in level, use local list
            # if level stays the same, and room changes and in level
            elif gameState == RAM.gameState[
                "InLevel"] and currentLevel == self.levelglobal and currentRoom != self.roomglobal:
                monkeyaddrs = RAM.monkeyListLocal[self.roomglobal]
                key_list = list(monkeyaddrs.keys())
                val_list = list(monkeyaddrs.values())

                addresses = []

                for val in val_list:
                    tuple1 = (val, 1, "MainRAM")
                    addresses.append(tuple1)

                localmonkeys = await bizhawk.read(ctx.bizhawk_ctx, addresses)
                monkeys_to_send = set()

                for i in range(len(localmonkeys)):
                    if int.from_bytes(localmonkeys[i], byteorder='little') == RAM.caughtStatus["Caught"]:
                        monkeys_to_send.add(key_list[i] + self.offset)

                if monkeys_to_send is not None:
                    await ctx.send_msgs([{
                        "cmd": "LocationChecks",
                        "locations": list(x for x in monkeys_to_send)
                    }])

            # check for victory condition
            if (gameState == RAM.gameState["Cleared"] or gameState == RAM.gameState["Credits1"]) and currentRoom == 86:
                victory = set()
                victory.add(RAM.items["Victory"] + self.offset)
                await ctx.send_msgs([{
                    "cmd": "LocationChecks",
                    "locations": list(x for x in victory)
                }])
                await ctx.send_msgs([{
                    "cmd": "StatusUpdate",
                    "status": ClientStatus.CLIENT_GOAL
                }])

            # Write Array
            # Training Room, set to 0xFF to mark as complete
            # Gadgets unlocked
            # Required apes (to match hundo)
            # Local apes first room (optional: for if in hub)
            # unlockLevels()

            writes = [
                (RAM.trainingRoomProgressAddress, 0xFF.to_bytes(1, "little"), "MainRAM"),
                (RAM.unlockedGadgetsAddress, (gadgets | gadgetStateFromServer).to_bytes(1, "little"), "MainRAM"),
                (RAM.requiredApesAddress, hundoCount.to_bytes(1, "little"), "MainRAM"),
            ]

            if gameState == RAM.gameState["LevelSelect"]:
                writes += [(RAM.localApeStartAddress, 0x0.to_bytes(8, "little"), "MainRAM")]

            writes += self.unlockLevels()

            await bizhawk.write(ctx.bizhawk_ctx, writes)

            self.levelglobal = currentLevel
            self.roomglobal = currentRoom

        except bizhawk.RequestFailedError:
            # Exit handler and return to main loop to reconnect
            pass

    def unlockLevels(self):

        key = self.worldkeycount

        current = RAM.levelStatus["Open"].to_bytes(1, byteorder="little")
        currentLock = RAM.levelStatus["Locked"].to_bytes(1, byteorder="little")
        if key > 0:
            current = RAM.levelStatus["Complete"].to_bytes(1, byteorder="little")
            currentLock = RAM.levelStatus["Complete"].to_bytes(1, byteorder="little")

        w11 = (RAM.levelAddresses[11], current, "MainRAM")
        w12 = (RAM.levelAddresses[12], current, "MainRAM")
        w13 = (RAM.levelAddresses[13], currentLock, "MainRAM")

        if key == 1:
            current = RAM.levelStatus["Open"].to_bytes(1, byteorder="little")
            currentLock = RAM.levelStatus["Locked"].to_bytes(1, byteorder="little")
        elif key > 1:
            current = RAM.levelStatus["Complete"].to_bytes(1, byteorder="little")
            currentLock = RAM.levelStatus["Complete"].to_bytes(1, byteorder="little")
        else:
            current = RAM.levelStatus["Locked"].to_bytes(1, byteorder="little")
            currentLock = RAM.levelStatus["Locked"].to_bytes(1, byteorder="little")

        w21 = (RAM.levelAddresses[21], current, "MainRAM")
        w22 = (RAM.levelAddresses[22], current, "MainRAM")
        w23 = (RAM.levelAddresses[23], currentLock, "MainRAM")

        if key == 2:
            current = RAM.levelStatus["Open"].to_bytes(1, byteorder="little")
            currentLock = RAM.levelStatus["Locked"].to_bytes(1, byteorder="little")
        elif key > 2:
            current = RAM.levelStatus["Complete"].to_bytes(1, byteorder="little")
            currentLock = RAM.levelStatus["Complete"].to_bytes(1, byteorder="little")
        else:
            current = RAM.levelStatus["Locked"].to_bytes(1, byteorder="little")
            currentLock = RAM.levelStatus["Locked"].to_bytes(1, byteorder="little")

        w31 = (RAM.levelAddresses[31], current, "MainRAM")
        w41 = (RAM.levelAddresses[41], current, "MainRAM")
        w42 = (RAM.levelAddresses[42], current, "MainRAM")
        w43 = (RAM.levelAddresses[43], currentLock, "MainRAM")

        if key == 3:
            current = RAM.levelStatus["Open"].to_bytes(1, byteorder="little")
            currentLock = RAM.levelStatus["Locked"].to_bytes(1, byteorder="little")
        elif key > 3:
            current = RAM.levelStatus["Complete"].to_bytes(1, byteorder="little")
            currentLock = RAM.levelStatus["Complete"].to_bytes(1, byteorder="little")
        else:
            current = RAM.levelStatus["Locked"].to_bytes(1, byteorder="little")
            currentLock = RAM.levelStatus["Locked"].to_bytes(1, byteorder="little")

        w51 = (RAM.levelAddresses[51], current, "MainRAM")
        w52 = (RAM.levelAddresses[52], current, "MainRAM")
        w53 = (RAM.levelAddresses[53], currentLock, "MainRAM")

        if key == 4:
            current = RAM.levelStatus["Open"].to_bytes(1, byteorder="little")
            currentLock = RAM.levelStatus["Locked"].to_bytes(1, byteorder="little")
        elif key > 4:
            current = RAM.levelStatus["Complete"].to_bytes(1, byteorder="little")
            currentLock = RAM.levelStatus["Complete"].to_bytes(1, byteorder="little")
        else:
            current = RAM.levelStatus["Locked"].to_bytes(1, byteorder="little")
            currentLock = RAM.levelStatus["Locked"].to_bytes(1, byteorder="little")

        w61 = (RAM.levelAddresses[61], current, "MainRAM")
        w71 = (RAM.levelAddresses[71], current, "MainRAM")
        w72 = (RAM.levelAddresses[72], current, "MainRAM")
        w73 = (RAM.levelAddresses[73], currentLock, "MainRAM")

        if key == 5:
            current = RAM.levelStatus["Open"].to_bytes(1, byteorder="little")
            currentLock = RAM.levelStatus["Locked"].to_bytes(1, byteorder="little")
        elif key > 5:
            current = RAM.levelStatus["Complete"].to_bytes(1, byteorder="little")
            currentLock = RAM.levelStatus["Complete"].to_bytes(1, byteorder="little")
        else:
            current = RAM.levelStatus["Locked"].to_bytes(1, byteorder="little")
            currentLock = RAM.levelStatus["Locked"].to_bytes(1, byteorder="little")

        w81 = (RAM.levelAddresses[81], current, "MainRAM")
        w82 = (RAM.levelAddresses[82], current, "MainRAM")
        w83 = (RAM.levelAddresses[83], currentLock, "MainRAM")

        if key == 6:
            current = RAM.levelStatus["Open"].to_bytes(1, byteorder="little")
            currentLock = RAM.levelStatus["Locked"].to_bytes(1, byteorder="little")
        elif key > 6:
            current = RAM.levelStatus["Complete"].to_bytes(1, byteorder="little")
            currentLock = RAM.levelStatus["Complete"].to_bytes(1, byteorder="little")
        else:
            current = RAM.levelStatus["Locked"].to_bytes(1, byteorder="little")
            currentLock = RAM.levelStatus["Locked"].to_bytes(1, byteorder="little")

        w91 = (RAM.levelAddresses[91], current, "MainRAM")

        return [w11, w12, w13, w21, w22, w23, w31, w41, w42, w43, w51, w52, w53, w61, w71, w72, w73, w81, w82, w83, w91]
