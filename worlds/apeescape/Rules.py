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
    connect_regions(world, player, "w6", "w7", lambda state: state.has("Sky Flyer", player, 1))
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

    world.completion_condition[player] = lambda state: state.has("Victory", player, 1)