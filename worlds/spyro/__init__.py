from typing import final

from BaseClasses import Item, Location, MultiWorld, Tutorial, ItemClassification
from ..AutoWorld import World, WebWorld
from .Client import SpyroClient
from .Items import SpyroItem, item_table
from .Locations import SpyroLocation
from .Options import SpyroOptions


@final
class SpyroWorld(World):
    """
    Spyro the Dragon, originally release on the PS1 in 1998, is a 3D collectathon platform starring the titular
    purple dragon, Spyro. Charge, jump, flame, and glide your way through 28 different levels across 6 different
    homeworlds, as you collect gems, recover stolen dragon eggs, free crystallized dragons, and make your way
    to Gnasty's World to torch him and save the world of dragons.
    """
    game = "Spyro the Dragon"
    options_dataclass = SpyroOptions
    options: SpyroOptions
    topology_present = True

    item_name_to_id = {v: k for k, v in item_table.items()}
