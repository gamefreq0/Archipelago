from worlds.apeescape import location_table
from worlds.generic.Rules import add_rule, set_rule, forbid_item
from BaseClasses import LocationProgressType
from .Regions import connect_regions
from .Strings import AEItem, AEWorld, AERoom


def set_rules(world, player: int):

    #Worlds
    connect_regions(world, player, "Menu", AEWorld.W1.value, lambda state: NoRequirement())
    connect_regions(world, player, "Menu", AEWorld.W2.value, lambda state: Keys(state, player, 1))
    connect_regions(world, player, "Menu", AEWorld.W3.value, lambda state: Keys(state, player, 2))
    connect_regions(world, player, "Menu", AEWorld.W4.value, lambda state: CanDive(state, player))#I think?
    connect_regions(world, player, "Menu", AEWorld.W5.value, lambda state: Keys(state, player, 3))
    connect_regions(world, player, "Menu", AEWorld.W6.value, lambda state: Keys(state, player, 4))
    connect_regions(world, player, "Menu", AEWorld.W7.value, lambda state: state.has(AEItem.Flyer.value, player, 1))
    connect_regions(world, player, "Menu", AEWorld.W8.value, lambda state: Keys(state, player, 5))
    connect_regions(world, player, "Menu", AEWorld.W9.value, lambda state: Keys(state, player, 6))

    #1-1
    connect_regions(world, player, AEWorld.W1.value, AERoom.W1L1Main.value, lambda state: True)

    connect_regions(world, player, AERoom.W1L1Main.value, AERoom.W1L1Noonan.value, lambda state: NoRequirement())
    connect_regions(world, player, AERoom.W1L1Main.value, AERoom.W1L1Jorjy.value, lambda state: NoRequirement())
    connect_regions(world, player, AERoom.W1L1Main.value, AERoom.W1L1Nati.value, lambda state: NoRequirement())
    connect_regions(world, player, AERoom.W1L1Main.value, AERoom.W1L1TrayC.value, lambda state: state.has(AEItem.Flyer.value, player, 1))

    #1-2
    connect_regions(world, player, AEWorld.W1.value, AERoom.W1L2Main.value, lambda state: True)

    connect_regions(world, player, AERoom.W1L2Main.value, AERoom.W1L2Shay.value, lambda state: NoRequirement())
    connect_regions(world, player, AERoom.W1L2Main.value, AERoom.W1L2DrMonk.value, lambda state: NoRequirement())
    connect_regions(world, player, AERoom.W1L2Main.value, AERoom.W1L2Grunt.value, lambda state: CanSwim(state, player) or state.has(AEItem.Flyer.value, player, 1))
    connect_regions(world, player, AERoom.W1L2Main.value, AERoom.W1L2Ahchoo.value, lambda state: NoRequirement())
    connect_regions(world, player, AERoom.W1L2Main.value, AERoom.W1L2Gornif.value, lambda state: CanSwim(state, player))
    connect_regions(world, player, AERoom.W1L2Main.value, AERoom.W1L2Tyrone.value, lambda state: NoRequirement())

    #1-3
    connect_regions(world, player, AEWorld.W1.value, AERoom.W1L3Entry.value, lambda state: True)
    connect_regions(world, player, AERoom.W1L3Entry.value, AERoom.W1L3Volcano.value, lambda state: True)
    connect_regions(world, player, AERoom.W1L3Entry.value, AERoom.W1L3Triceratops.value, lambda state: state.has(AEItem.Sling.value, player, 1))

    connect_regions(world, player, AERoom.W1L3Entry.value, AERoom.W1L3Scotty.value, lambda state: NoRequirement())
    connect_regions(world, player, AERoom.W1L3Entry.value, AERoom.W1L3Coco.value, lambda state: NoRequirement())
    connect_regions(world, player, AERoom.W1L3Entry.value, AERoom.W1L3JThomas.value, lambda state: CanHitMultiple(state, player))
    connect_regions(world, player, AERoom.W1L3Entry.value, AERoom.W1L3Moggan.value, lambda state: NoRequirement())
    connect_regions(world, player, AERoom.W1L3Volcano.value, AERoom.W1L3Barney.value, lambda state: NoRequirement())
    connect_regions(world, player, AERoom.W1L3Volcano.value, AERoom.W1L3Mattie.value, lambda state: NoRequirement())
    connect_regions(world, player, AERoom.W1L3Triceratops.value, AERoom.W1L3Rocky.value, lambda state: CanHitMultiple(state, player))

    #2-1
    connect_regions(world, player, AEWorld.W2.value, AERoom.W2L1Entry.value, lambda state: True)
    connect_regions(world, player, AERoom.W2L1Entry.value, AERoom.W2L1Mushroom.value, lambda state: True)
    connect_regions(world, player, AERoom.W2L1Entry.value, AERoom.W2L1Fish.value, lambda state: True)
    connect_regions(world, player, AERoom.W2L1Entry.value, AERoom.W2L1Tent.value, lambda state: True)
    connect_regions(world, player, AERoom.W2L1Entry.value, AERoom.W2L1Boulder.value, lambda state: True)

    connect_regions(world, player, AERoom.W2L1Entry.value, AERoom.W2L1Marquez.value, lambda state: CanHitMultiple(state, player))
    connect_regions(world, player, AERoom.W2L1Entry.value, AERoom.W2L1Livinston.value, lambda state: CanHitMultiple(state, player))
    connect_regions(world, player, AERoom.W2L1Entry.value, AERoom.W2L1George.value, lambda state: NoRequirement())
    connect_regions(world, player, AERoom.W2L1Mushroom.value, AERoom.W2L1Gonzo.value, lambda state: TJ_Mushroom(state, player) and CanHitMultiple(state, player))
    connect_regions(world, player, AERoom.W2L1Mushroom.value, AERoom.W2L1Zanzibar.value, lambda state: TJ_Mushroom(state, player) and CanHitMultiple(state, player))
    connect_regions(world, player, AERoom.W2L1Mushroom.value, AERoom.W2L1Alphonse.value, lambda state: TJ_Mushroom(state, player) and CanHitMultiple(state, player))
    connect_regions(world, player, AERoom.W2L1Fish.value, AERoom.W2L1Maki.value, lambda state: TJ_FishEntry(state, player) and state.has(AEItem.Sling.value, player, 1))
    connect_regions(world, player, AERoom.W2L1Fish.value, AERoom.W2L1Herb.value, lambda state: TJ_FishEntry(state, player))
    connect_regions(world, player, AERoom.W2L1Fish.value, AERoom.W2L1Dilweed.value, lambda state: (TJ_FishEntry(state, player) and CanHitMultiple(state, player)) or (TJ_UFOEntry(state, player) and TJ_UFOCliff(state, player)))
    connect_regions(world, player, AERoom.W2L1Tent.value, AERoom.W2L1Stoddy.value, lambda state: (TJ_FishEntry(state, player) and CanHitMultiple(state, player)) or (TJ_UFOEntry(state, player) and TJ_UFOCliff(state, player)))
    connect_regions(world, player, AERoom.W2L1Tent.value, AERoom.W2L1Mitong.value, lambda state: (TJ_FishEntry(state, player) and CanHitMultiple(state, player)) or (TJ_UFOEntry(state, player) and TJ_UFOCliff(state, player)))
    connect_regions(world, player, AERoom.W2L1Tent.value, AERoom.W2L1Nasus.value, lambda state: (TJ_FishEntry(state, player) or (TJ_UFOEntry(state, player) and TJ_UFOCliff(state, player)) and CanHitMultiple(state, player)))
    connect_regions(world, player, AERoom.W2L1Boulder.value, AERoom.W2L1Elehcim.value, lambda state: (TJ_UFOEntry(state, player) or TJ_FishEntry(state, player)) and CanHitMultiple(state, player) and state.has(AEItem.Sling.value, player, 1))
    connect_regions(world, player, AERoom.W2L1Boulder.value, AERoom.W2L1Selur.value, lambda state: ((TJ_UFOEntry(state, player) and TJ_UFOCliff(state, player)) or TJ_FishEntry(state, player)) and CanHitMultiple(state, player) and state.has(AEItem.Sling.value, player, 1))

    #2-2
    connect_regions(world, player, AEWorld.W2.value, AERoom.W2L2Outside.value, lambda state: True)
    connect_regions(world, player, AERoom.W2L2Outside.value, AERoom.W2L2Fan.value, lambda state: True)
    connect_regions(world, player, AERoom.W2L2Outside.value, AERoom.W2L2Obelisk.value, lambda state: True)
    connect_regions(world, player, AERoom.W2L2Outside.value, AERoom.W2L2Water.value, lambda state: True)

    connect_regions(world, player, AERoom.W2L2Outside.value, AERoom.W2L2Kyle.value, lambda state: CanHitOnce(state, player) and state.has(AEItem.Flyer.value, player, 1))
    connect_regions(world, player, AERoom.W2L2Outside.value, AERoom.W2L2Stan.value, lambda state: NoRequirement())
    connect_regions(world, player, AERoom.W2L2Outside.value, AERoom.W2L2Kenny.value, lambda state: NoRequirement())
    connect_regions(world, player, AERoom.W2L2Outside.value, AERoom.W2L2Cratman.value, lambda state: NoRequirement())
    connect_regions(world, player, AERoom.W2L2Outside.value, AERoom.W2L2Mooshy.value, lambda state: state.has(AEItem.Hoop.value, player, 1))
    connect_regions(world, player, AERoom.W2L2Fan.value, AERoom.W2L2Nuzzy.value, lambda state: state.has(AEItem.Sling.value, player, 1) or state.has(AEItem.Hoop.value, player, 1) or state.has(AEItem.Punch.value, player, 1))
    connect_regions(world, player, AERoom.W2L2Fan.value, AERoom.W2L2Mav.value, lambda state: NoRequirement())
    connect_regions(world, player, AERoom.W2L2Obelisk.value, AERoom.W2L2Papou.value, lambda state: NoRequirement())
    connect_regions(world, player, AERoom.W2L2Obelisk.value, AERoom.W2L2Trance.value, lambda state: NoRequirement())
    connect_regions(world, player, AERoom.W2L2Obelisk.value, AERoom.W2L2Bernt.value, lambda state: state.has(AEItem.Sling.value, player, 1))
    connect_regions(world, player, AERoom.W2L2Water.value, AERoom.W2L2Runt.value, lambda state: CanSwim(state, player) and (state.has(AEItem.Sling.value, player, 1) or state.has(AEItem.Hoop.value, player, 1)) and (CanHitOnce(state, player) or state.has(AEItem.Flyer.value, player, 1)))
    connect_regions(world, player, AERoom.W2L2Water.value, AERoom.W2L2Hoolah.value, lambda state: CanHitMultiple(state, player))
    connect_regions(world, player, AERoom.W2L2Water.value, AERoom.W2L2Chino.value, lambda state: CanSwim(state, player) and (state.has(AEItem.Sling.value, player, 1) or state.has(AEItem.Hoop.value, player, 1)) and (CanHitOnce(state, player) or state.has(AEItem.Flyer.value, player, 1)))

    #2-3
    connect_regions(world, player, AEWorld.W2.value, AERoom.W2L3Outside.value, lambda state: True)
    connect_regions(world, player, AERoom.W2L3Outside.value, AERoom.W2L3Side.value, lambda state: True)
    connect_regions(world, player, AERoom.W2L3Outside.value, AERoom.W2L3Main.value, lambda state: True)
    connect_regions(world, player, AERoom.W2L3Outside.value, AERoom.W2L3Pillar.value, lambda state: True)

    connect_regions(world, player, AERoom.W2L3Outside.value, AERoom.W2L3Bazzle.value, lambda state: state.has(AEItem.Sling.value, player, 1) or state.has(AEItem.Flyer.value, player, 1))
    connect_regions(world, player, AERoom.W2L3Outside.value, AERoom.W2L3Freeto.value, lambda state: NoRequirement())
    connect_regions(world, player, AERoom.W2L3Side.value, AERoom.W2L3Troopa.value, lambda state: (state.has(AEItem.Sling.value, player, 1) or state.has(AEItem.Flyer.value, player, 1)) and CanHitOnce(state, player))
    connect_regions(world, player, AERoom.W2L3Main.value, AERoom.W2L3Stymie.value, lambda state: CR_Inside(state, player))
    connect_regions(world, player, AERoom.W2L3Main.value, AERoom.W2L3Spanky.value, lambda state: CR_Inside(state, player) and CanSwim(state, player))
    connect_regions(world, player, AERoom.W2L3Main.value, AERoom.W2L3Jesta.value, lambda state: CR_Inside(state, player))
    connect_regions(world, player, AERoom.W2L3Pillar.value, AERoom.W2L3Pally.value, lambda state: CR_Inside(state, player))
    connect_regions(world, player, AERoom.W2L3Pillar.value, AERoom.W2L3Crash.value, lambda state: CR_Inside(state, player) and state.has(AEItem.Car.value, player, 1))

    #4-1
    connect_regions(world, player, AEWorld.W4.value, "4-1", lambda state: True)
    connect_regions(world, player, AEWorld.W4.value, "4-2", lambda state: True)
    connect_regions(world, player, AEWorld.W4.value, "4-3", lambda state: True)
    connect_regions(world, player, AEWorld.W5.value, "5-1", lambda state: True)
    connect_regions(world, player, AEWorld.W5.value, "5-2", lambda state: state.has("Sky Flyer", player, 1))
    connect_regions(world, player, AEWorld.W5.value, "5-3", lambda state: True)
    connect_regions(world, player, AEWorld.W7.value, "7-1", lambda state: True)
    connect_regions(world, player, AEWorld.W7.value, "7-2", lambda state: True)
    connect_regions(world, player, AEWorld.W7.value, "7-3", lambda state: True)
    connect_regions(world, player, AEWorld.W8.value, "8-1", lambda state: True)
    connect_regions(world, player, AEWorld.W8.value, "8-2", lambda state: True)
    connect_regions(world, player, AEWorld.W8.value, "8-3", lambda state: True)

    connect_regions(world, player, AEWorld.W9.value, "9-1", lambda state: True)

    connect_regions(world, player, "4-1", "4-1 F", lambda state: state.has("Sky Flyer", player, 1))
    connect_regions(world, player, "4-1", "4-1 SF", lambda state:
        state.has("Slingback Shooter", player, 1)
        and state.has("Sky Flyer", player, 1))

    connect_regions(world, player, "4-2", "4-2 HF", lambda state:
        state.has("Super Hoop", player, 1)
        or state.has("Sky Flyer", player, 1))

    connect_regions(world, player, "4-3", "4-3 S", lambda state: state.has("Slingback Shooter", player, 1))
    connect_regions(world, player, "4-3", "4-3 C", lambda state: state.has("R.C. Car", player, 1))

    connect_regions(world, player, "5-1", "5-1 S", lambda state: state.has("Slingback Shooter", player, 1))

    connect_regions(world, player, "5-2", "5-2 S", lambda state: state.has("Slingback Shooter", player, 1))

    connect_regions(world, player, "5-3", "5-3 F", lambda state: state.has("Sky Flyer", player, 1))

    connect_regions(world, player, "7-1", "7-1 S", lambda state: state.has("Slingback Shooter", player, 1))

    connect_regions(world, player, "7-1", "7-1 F", lambda state: state.has("Sky Flyer", player, 1))

    world.completion_condition[player] = lambda state: state.has("Victory", player, 1)


def Keys(state, player, count):
    return state.has(AEItem.Key.value, player, count)
def NoRequirement():
    return True

def CanHitOnce(state, player):
    return state.has(AEItem.Club.value, player, 1) or state.has(AEItem.Sling.value, player, 1) or state.has(
        AEItem.Punch.value, player, 1)

def CanHitMultiple(state, player):
    return state.has(AEItem.Club.value, player, 1) or state.has(AEItem.Punch.value, player, 1)

def CanGainHeight(state, player):
    return state.has(AEItem.Flyer.value, player, 1)

def HasMobility(state, player):
    return state.has(AEItem.Flyer.value, player, 1)

def RCMonkey (state, player):
    return state.has(AEItem.Car.value, player, 1)

def CanSwim(state, player):
    return state.has(AEItem.WaterNet.value, player, 1)

def CanDive(state, player):
    return state.has(AEItem.WaterNet.value, player, 1)

def CanWaterCatch(state, player):
    return state.has(AEItem.WaterNet.value, player, 1)

def TJ_UFOEntry(state, player):
    return CanDive(state, player)

def TJ_UFOCliff(state, player):
    return state.has(AEItem.Flyer.value, player, 1)

def TJ_FishEntry(state, player):
    return CanSwim(state, player)

def TJ_Mushroom(state, player):
    return HasMobility(state, player)

def CR_Inside(state, player):
    return state.has(AEItem.Sling.value, player, 1) or state.has(AEItem.Punch.value, player, 1)

def DI_SecondHalf(state, player):
    return CanHitOnce(state, player) and CanDive(state, player)

def DI_Boulders(state, player):
    return state.has(AEItem.Hoop.value, player, 1) or state.has(AEItem.Car.value, player, 1)

def WSW_ThirdRoom(state, player):
    return state.has(AEItem.Sling.value, player, 1) or state.has(AEItem.Flyer.value, player, 1)

def WSW_ForthRoom(state, player):
    return CanHitMultiple(state, player) or state.has(AEItem.Flyer.value, player, 1)

def CC_5Monkeys(state, player):
    return state.has(AEItem.Club.value, player, 1) or state.has(AEItem.Flyer.value, player, 1) or state.has(AEItem.Punch.value, player, 1)

def CC_WaterRoom(state, player):
    return CanHitMultiple(state, player) or (CanDive(state, player) and state.has(AEItem.Punch.value, player, 1))

def CC_ButtonRoom(state, player):
    return CC_WaterRoom(state, player) and CanSwim(state, player)

def CP_FrontSewer(state, player):
    return state.has(AEItem.Car.value, player, 1)

def CP_FrontBarrels(state, player):
    return CP_FrontSewer(state, player) and (CanSwim(state, player) or HasMobility(state, player))

def CP_BackSewer(state, player):
    return False

def SF_CarRoom(state, player):
    return state.has(AEItem.Car.value, player, 1) or state.has(AEItem.Punch.value, player, 1)

def SF_MechRoom(state, player):
    return state.has(AEItem.Club.value, player, 1) and SF_CarRoom(state, player)

def TVT_HitButton(state, player):
    return state.has(AEItem.Flyer.value, player, 1) and CanHitOnce(state, player)

def TVT_TankRoom(state, player):
    return TVT_HitButton(state, player)

def MM_Natalie(state, player):
    return CanHitMultiple(state, player)

def MM_Professor(state, player):
    return state.has(AEItem.Flyer.value, player, 1) and CanHitMultiple(state, player)

def Jake_Open(state, player):
    return MM_Natalie(state, player) and MM_Professor(state, player)

def MM_Jake(state, player):
    return CanHitMultiple(state, player) and Jake_Open(state, player)

def MM_SHA(state, player):
    return MM_Natalie(state, player) and MM_Professor(state, player) and MM_Jake(state, player)

def MM_UFODoor(state, player):
    return MM_SHA(state, player) and state.has(AEItem.Sling.value, player, 1)

def MM_DoubleDoor(state, player):
    return MM_UFODoor(state, player) and state.has(AEItem.Hoop.value, player, 1) and state.has(AEItem.Car.value, player, 1) and CanHitMultiple(state, player)

def MM_SpaceMonkeys(state, player):
    return MM_DoubleDoor(state, player) and state.has(AEItem.Flyer.value, player, 1)

def MM_FinalBoss(state, player):
    return MM_DoubleDoor(state, player) and state.has(AEItem.Sling.value, player, 1) and state.has(AEItem.Flyer.value, player, 1)