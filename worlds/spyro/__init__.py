from typing import final, override

from BaseClasses import Entrance, MultiWorld
from BaseClasses import ItemClassification
from entrance_rando import randomize_entrances
from ..AutoWorld import World
from .Client import SpyroClient
from .Items import SpyroItem, filler_items, goal_item, item_table
from .Items import homeworld_access, level_access, boss_items, trap_items
from .Items import grouped_items
from .Locations import location_table, grouped_locations
from .Options import SpyroOptions
from .Regions import create_regions, ENTRANCE_OUT, ENTRANCE_IN
from .Rules import set_rules


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
    # Following ignore is for https://github.com/python/typing/discussions/1486 reasons
    # Hopefully, eventually this becomes unnecessary
    options: SpyroOptions  # pyright: ignore[reportIncompatibleVariableOverride]
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
        if name in filler_items:
            classification = ItemClassification.filler
        elif name in trap_items:
            classification = ItemClassification.trap
        else:
            classification = ItemClassification.progression
        return SpyroItem(
            name, classification, self.item_name_to_id[name], self.player
        )

    def create_event(self, event: str) -> SpyroItem:
        return SpyroItem(
            event, ItemClassification.progression, None, self.player
        )

    @override
    def create_items(self) -> None:
        for name in homeworld_access:
            if name == self.options.starting_world.get_option_name(
                self.options.starting_world.value
            ):
                self.push_precollected(self.create_item(name))
            else:
                self.itempool += [self.create_item(name)]
        for name in level_access:
            self.itempool += [self.create_item(name)]
        for name in boss_items:
            self.itempool += [self.create_item(name)]
        victory = self.create_item(goal_item[0])

        trap_percentage = 0.05
        total_unfilled_locations = len(
            self.multiworld.get_unfilled_locations(self.player)
        )
        total_filled_local_locations = len(self.itempool) + 1  # Victory item
        trap_count = round(
            (
                total_unfilled_locations - total_filled_local_locations
            ) * trap_percentage
        )
        total_filled_local_locations += trap_count

        for _ in range(trap_count):
            random_trap = self.multiworld.random.choice(trap_items)
            self.itempool += [self.create_item(random_trap)]

        junk_count = total_unfilled_locations - total_filled_local_locations

        for _ in range(junk_count):
            random_filler = self.multiworld.random.choice(filler_items)
            self.itempool += [self.create_item(random_filler)]

        if self.options.goal == "gnasty":
            # TODO: Replace goal location with beating Gnasty
            self.get_location("Gnasty Gnorc 100% Gems").place_locked_item(
                victory
            )

        self.multiworld.itempool += self.itempool

    @override
    def connect_entrances(self) -> None:
        if self.options.portal_shuffle:
            shuffled_entrances = randomize_entrances(
                self, True, {
                    ENTRANCE_IN: [ENTRANCE_OUT],
                    ENTRANCE_OUT: [ENTRANCE_IN]
                }, False
            )
        else:
            all_entrances = self.get_entrances()
            all_ents_list: list[Entrance] = []
            for entrance in all_entrances:
                all_ents_list.append(entrance)
            levels_start: int = 0
            levels_stop: int = 0
            for index, ent in enumerate(all_ents_list):
                if ("Stone Hill" in ent.name) and (levels_start == 0):
                    levels_start = index
                elif "Gnasty's Loot" in ent.name:
                    levels_stop = index
            vanilla_pairs: list[tuple[Entrance, Entrance]] = []
            for index in range(levels_start, levels_stop, 2):
                vanilla_pairs.append(
                    (all_ents_list[index], all_ents_list[index + 1])
                )
            for pair in vanilla_pairs:
                if (pair[0].parent_region is not None) and (
                    pair[1].parent_region is not None
                ):
                    pair[0].connect(pair[1].parent_region)
                    pair[1].connect(pair[0].parent_region)

    @override
    def set_rules(self) -> None:
        set_rules(self)
