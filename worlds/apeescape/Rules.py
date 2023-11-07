from worlds.apeescape import location_table
from worlds.generic.Rules import add_rule, set_rule, forbid_item
from BaseClasses import LocationProgressType
from .Regions import connect_regions
from .Strings import AEItem, AEWorld, AERoom


def set_rules(world, player: int):
    connect_regions(world, player, "Menu", AEWorld.W1.value, lambda state: NoRequirement())

    #Worlds
    connect_regions(world, player, AEWorld.W1.value, AEWorld.W2.value, lambda state: Keys(state, player, 1))
    connect_regions(world, player, AEWorld.W2.value, AEWorld.W3.value, lambda state: Keys(state, player, 2))
    connect_regions(world, player, AEWorld.W3.value, AEWorld.W4.value, lambda state: NoRequirement())#state.has(AEItem.WaterNet.value, player, 1))
    connect_regions(world, player, AEWorld.W4.value, AEWorld.W5.value, lambda state: Keys(state, player, 3))
    connect_regions(world, player, AEWorld.W5.value, AEWorld.W6.value, lambda state: Keys(state, player, 4))
    connect_regions(world, player, AEWorld.W6.value, AEWorld.W7.value, lambda state: state.has(AEItem.Flyer.value, player, 1))
    connect_regions(world, player, AEWorld.W7.value, AEWorld.W8.value, lambda state: Keys(state, player, 5))
    connect_regions(world, player, AEWorld.W8.value, AEWorld.W9.value, lambda state: Keys(state, player, 6))

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
    connect_regions(world, player, AERoom.W1L3Entry.value, AERoom.W1L3Triceratops.value, lambda state: True)

    connect_regions(world, player, AERoom.W1L3Entry.value, AERoom.W1L3Scotty.value, lambda state: NoRequirement())
    connect_regions(world, player, AERoom.W1L3Entry.value, AERoom.W1L3Coco.value, lambda state: NoRequirement())
    connect_regions(world, player, AERoom.W1L3Entry.value, AERoom.W1L3JThomas.value, lambda state: CanHitMultiple(state, player))
    connect_regions(world, player, AERoom.W1L3Entry.value, AERoom.W1L3Moggan.value, lambda state: NoRequirement())
    connect_regions(world, player, AERoom.W1L3Volcano.value, AERoom.W1L3Barney.value, lambda state: NoRequirement())
    connect_regions(world, player, AERoom.W1L3Volcano.value, AERoom.W1L3Mattie.value, lambda state: NoRequirement())
    connect_regions(world, player, AERoom.W1L3Triceratops.value, AERoom.W1L3Rocky.value, lambda state: state.has(AEItem.Sling.value, player, 1) and CanHitMultiple(state, player))



    connect_regions(world, player, AEWorld.W2.value, "2-1", lambda state: True)
    connect_regions(world, player, AEWorld.W2.value, "2-2", lambda state: True)
    connect_regions(world, player, AEWorld.W2.value, "2-3", lambda state: True)
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



    connect_regions(world, player, "2-1", "2-1 Mush", lambda state: state.has("Sky Flyer", player, 1))
    connect_regions(world, player, "2-1", "2-1 Hang", lambda state:
        state.has("Slingback Shooter", player, 1)
        or state.has("Sky Flyer", player, 1))
    connect_regions(world, player, "2-1", "2-1 UFO", lambda state: state.has("Slingback Shooter", player, 1))

    connect_regions(world, player, "2-2", "2-2 Fast", lambda state: state.has("Super Hoop", player, 1))
    connect_regions(world, player, "2-2", "2-2 Fan", lambda state:
        state.has("Super Hoop", player, 1)
        or state.has("Slingback Shooter", player, 1)
        or state.has("Magic Punch", player, 1))
    connect_regions(world, player, "2-2", "2-2 Vine", lambda state: state.has("Slingback Shooter", player, 1))
    connect_regions(world, player, "2-2", "2-2 Base", lambda state:
        state.has("Super Hoop", player, 1)
        or state.has("Slingback Shooter", player, 1))

    connect_regions(world, player, "2-3", "2-3 SF", lambda state:
        state.has("Slingback Shooter", player, 1)
        or state.has("Sky Flyer", player, 1))
    connect_regions(world, player, "2-3", "2-3 SP", lambda state:
        state.has("Slingback Shooter", player, 1)
        or state.has("Magic Punch", player, 1))
    connect_regions(world, player, "2-3", "2-3 SPC", lambda state:
        (state.has("Slingback Shooter", player, 1)
        or state.has("Sky Flyer", player, 1))
        and state.has("R.C. Car", player, 1))

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
