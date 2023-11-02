from worlds.apeescape import location_table
from worlds.generic.Rules import add_rule, set_rule, forbid_item
from BaseClasses import LocationProgressType
from .Regions import connect_regions


def set_rules(world, player: int):
    connect_regions(world, player, "Menu", "w1", lambda state: True)

    connect_regions(world, player, "w1", "w2", lambda state: state.has("World Key", player, 1))
    connect_regions(world, player, "w2", "w3", lambda state: state.has("World Key", player, 2))
    connect_regions(world, player, "w3", "w4", lambda state: True)
    connect_regions(world, player, "w4", "w5", lambda state: state.has("World Key", player, 3))
    connect_regions(world, player, "w5", "w6", lambda state: state.has("World Key", player, 4))
    connect_regions(world, player, "w6", "w7", lambda state: True)
    connect_regions(world, player, "w7", "w8", lambda state: state.has("World Key", player, 5))
    connect_regions(world, player, "w8", "w9", lambda state: state.has("World Key", player, 6))

    connect_regions(world, player, "w1", "1-1", lambda state: True)
    connect_regions(world, player, "w1", "1-2", lambda state: True)
    connect_regions(world, player, "w1", "1-3", lambda state: True)
    connect_regions(world, player, "w2", "2-1", lambda state: True)
    connect_regions(world, player, "w2", "2-2", lambda state: True)
    connect_regions(world, player, "w2", "2-3", lambda state: True)
    connect_regions(world, player, "w4", "4-1", lambda state: True)
    connect_regions(world, player, "w4", "4-2", lambda state: True)
    connect_regions(world, player, "w4", "4-3", lambda state: True)
    connect_regions(world, player, "w5", "5-1", lambda state: True)
    connect_regions(world, player, "w5", "5-2", lambda state: True)
    connect_regions(world, player, "w5", "5-3", lambda state: True)
    connect_regions(world, player, "w7", "7-1", lambda state: True)
    connect_regions(world, player, "w7", "7-2", lambda state: True)
    connect_regions(world, player, "w7", "7-3", lambda state: True)
    connect_regions(world, player, "w8", "8-1", lambda state: True)
    connect_regions(world, player, "w8", "8-2", lambda state: True)
    connect_regions(world, player, "w8", "8-3", lambda state: True)

    connect_regions(world, player, "w9", "9-1", lambda state: True)

    connect_regions(world, player, "1-1", "1-1 Ledge", lambda state: state.has("Sky Flyer", player, 1))

    connect_regions(world, player, "1-3", "1-3 Tri", lambda state: state.has("Slingback Shooter", player, 1))

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

    world.completion_condition[player] = lambda state: state.has("Victory", player, 1)
