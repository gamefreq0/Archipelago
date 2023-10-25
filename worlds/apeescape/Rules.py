from worlds.apeescape import location_table
from worlds.generic.Rules import add_rule, set_rule, forbid_item
from BaseClasses import LocationProgressType
from .Regions import connect_regions


def set_rules(world, player: int):
    connect_regions(world, player, "Menu", "1-1", lambda state: True)
    connect_regions(world, player, "Menu", "1-2", lambda state: True)
    connect_regions(world, player, "Menu", "1-3", lambda state: True)
    connect_regions(world, player, "1-3", "9-1", lambda state: state.has("Monkey Radar", player, 1))

    world.completion_condition[player] = lambda state: state.can_reach("9-1 Specter", "Location", player)