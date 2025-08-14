from typing import final, override

from BaseClasses import Item, Location, MultiWorld, Tutorial, ItemClassification
from ..AutoWorld import World, WebWorld
from .Client import SpyroClient
from .Items import SpyroItem, filler_items, item_table, grouped_items
from .Items import homeworld_access, level_access, boss_items, trap_items
from .Locations import SpyroLocation, location_table, grouped_locations
from .Options import SpyroOptions
from .Regions import create_regions


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

    @override
    def create_regions(self) -> None:
        return create_regions(self)
    
    @override
    def create_item(self, name: str) -> SpyroItem:
        if (name in homeworld_access) or (name in level_access) or (name in boss_items):
            classification = ItemClassification.progression
        elif name in trap_items:
            classification = ItemClassification.trap
        else:
            classification = ItemClassification.filler
        return SpyroItem(name, classification, self.item_name_to_id[name], self.player)

    @override
    def create_items(self) -> None:
        for name in homeworld_access:
            self.itempool += [self.create_item(name)]
        for name in level_access:
            self.itempool += [self.create_item(name)]
        for name in boss_items:
            self.itempool += [self.create_item(name)]

        trap_percentage = 0.05
        trap_count = round(len(self.multiworld.get_unfilled_locations(self.player)) * trap_percentage)

        for _ in range(trap_count):
            random_trap = self.multiworld.random.choice(trap_items)
            self.itempool += [self.create_item(random_trap)]

        junk_count = len(self.multiworld.get_unfilled_locations(self.player))

        for _ in range(junk_count):
            random_filler = self.multiworld.random.choice(filler_items)
            self.itempool += [self.create_item(random_filler)]
