from typing_extensions import TYPE_CHECKING

from BaseClasses import Entrance
from worlds.generic.Rules import add_rule
from .Regions import hub_names

if TYPE_CHECKING:
    from . import SpyroWorld


def set_rules(world: "SpyroWorld"):
    world.multiworld.completion_condition[world.player] =\
        lambda state: state.has("Victory", world.player, 1)
