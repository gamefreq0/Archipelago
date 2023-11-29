from worlds.apeescape import location_table
from worlds.generic.Rules import add_rule, set_rule, forbid_item
from BaseClasses import LocationProgressType
from .Regions import connect_regions
from .Strings import AEItem, AEWorld, AERoom
from .RulesGlitchless import Glitchless
from .RulesNoIJ import NoIJ
from .RulesIJ import IJ


def set_rules(world, player: int):
    if world.logic[player].value == 0x00:
        Glitchless.set_rules(None, world, player, world.coin[player].value == 0x00)
    elif world.logic[player].value == 0x01:
        NoIJ.set_rules(None, world, player, world.coin[player].value == 0x00)
    elif world.logic[player].value == 0x02:
        IJ.set_rules(None, world, player, world.coin[player].value == 0x00)
