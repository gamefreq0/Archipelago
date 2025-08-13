from typing import final, override

from BaseClasses import Item, Location, MultiWorld, Tutorial, ItemClassification
from ..AutoWorld import World, WebWorld
from .Client import SpyroClient
from .Items import SpyroItem, item_table, grouped_items
from .Locations import SpyroLocation, location_table, grouped_locations
from .Options import SpyroOptions


@final
class SpyroWorld(World):
    """
    Spyro the Dragon, originally released on the PS1 in 1998, is a 3D collectathon platform starring the titular
    purple dragon, Spyro. Charge, jump, flame, and glide your way through 29 different levels across 6 different
    homeworlds, as you collect gems, recover stolen dragon eggs, free crystallized dragons, and make your way
    to Gnorc Gnexus to torch Gnasty and save the world of dragons.
    """
    game = "Spyro the Dragon"
    options_dataclass = SpyroOptions
    options: SpyroOptions
    topology_present = True

    item_name_to_id = {v: k for k, v in item_table.items()}
    location_name_to_id = {v: k for k, v in location_table.items()}

    item_name_groups = grouped_items
    location_name_groups = grouped_locations

    def __init__(self, multiworld: "MultiWorld", player: int):
        self.goal: int | None = 0
        self.itempool: list[SpyroItem] = []
        super().__init__(multiworld, player)

    @override
    def generate_early(self) -> None:
        self.goal = self.options.goal.value
        self.itempool = []
