from logging import warning

try:
    from typing import final, override, ClassVar
except ImportError:
    from typing_extensions import final, override, ClassVar

from BaseClasses import Entrance, MultiWorld
from BaseClasses import ItemClassification
from Options import OptionError
from entrance_rando import randomize_entrances
from ..AutoWorld import WebWorld, World
from .web import SpyroWeb
from .items import SpyroItem, filler_items, goal_item
from .items import homeworld_access, level_access, boss_items, trap_items
from .items import grouped_items, item_name_to_id
from .locations import location_name_to_id
from .locations import grouped_locations
from .options import SpyroOptions
from .regions import create_regions, ENTRANCE_OUT, ENTRANCE_IN
from .rules import set_rules


@final
class SpyroWorld(World):
    """
    Spyro the Dragon, originally released on the PS1 in 1998, is a 3D collectathon platform starring the titular
    purple dragon, Spyro. Charge, jump, flame, and glide your way through 29 different levels across 6 different
    homeworlds, as you collect gems, recover stolen dragon eggs, free crystallized dragons, and make your way
    to Gnorc Gnexus to torch Gnasty and save the world of dragons.
    """
    game = "Spyro the Dragon"
    web: ClassVar[WebWorld] = SpyroWeb()
    options_dataclass = SpyroOptions
    # Following ignore is for https://github.com/python/typing/discussions/1486 reasons
    # Hopefully, eventually this becomes unnecessary
    options: SpyroOptions  # pyright: ignore[reportIncompatibleVariableOverride]
    topology_present = True

    item_name_to_id = item_name_to_id

    location_name_to_id = location_name_to_id

    item_name_groups = grouped_items
    location_name_groups = grouped_locations

    def __init__(self, multiworld: "MultiWorld", player: int):
        super().__init__(multiworld, player)
        self.goal: int | None = 0
        self.itempool: list[SpyroItem] = []
        self.shuffled_entrance_pairings: list[tuple[str, str]] = []

    @override
    def generate_early(self) -> None:
        self.goal = self.options.goal.value
        self.itempool = []
        
        try:
            _: int = int(self.options.spyro_color.value, 16)
        except ValueError as exc:
            raise OptionError(
                f"{self.player_name}'s spyro_color value of " +
                f'"{self.options.spyro_color.value}" is not a valid RGBA color.'
            ) from exc
        
        if self.options.goal == self.options.goal.option_loot:
            raise OptionError(
                f"{self.player_name} set goal to loot, but loot goal doesn't work yet."
            )
        
        if self.options.portal_shuffle.value == 1:
            raise OptionError(
                f"{self.player_name} enabled portal shuffle, but portal shuffle doesn't work yet."
            )
        
        if self.options.death_link.value == 1:
            warning(
                f"Deathlink for {self.game} doesn't work yet. Option will be ignored"
            )

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
            
        return SpyroItem(name, classification, self.item_name_to_id[name], self.player)

    def create_event(self, event: str) -> SpyroItem:
        """Generate item with no ID, for use with generation-time logic

        Args:
            event: Event item name

        Returns:
            The generated SpyroItem
        """
        return SpyroItem(event, ItemClassification.progression, None, self.player)

    @override
    def create_items(self) -> None:
        for name in homeworld_access:
            if name == self.options.starting_world.get_option_name(self.options.starting_world.value):
                self.push_precollected(self.create_item(name))
            else:
                self.itempool += [self.create_item(name)]
        
        for name in level_access:
            self.itempool += [self.create_item(name)]
        
        for name in boss_items:
            self.itempool += [self.create_item(name)]
        
        victory = self.create_item(goal_item[0])

        trap_percentage = 0.05
        total_unfilled_locations = len(self.multiworld.get_unfilled_locations(self.player))
        total_filled_local_locations = len(self.itempool) + 1  # Victory item
        trap_count = round((total_unfilled_locations - total_filled_local_locations) * trap_percentage)
        total_filled_local_locations += trap_count

        for _ in range(trap_count):
            random_trap = self.multiworld.random.choice(trap_items)
            self.itempool += [self.create_item(random_trap)]

        junk_count = total_unfilled_locations - total_filled_local_locations

        for _ in range(junk_count):
            random_filler = self.multiworld.random.choice(filler_items)
            self.itempool += [self.create_item(random_filler)]

        if self.options.goal == "gnasty":
            self.get_location("Defeated Gnasty Gnorc").place_locked_item(victory)

        self.multiworld.itempool += self.itempool

    @override
    def connect_entrances(self) -> None:
        if self.options.portal_shuffle:
            shuffled_entrances = randomize_entrances(
                self, 
                True, 
                {
                    ENTRANCE_IN: [ENTRANCE_OUT],
                    ENTRANCE_OUT: [ENTRANCE_IN]
                }, 
                False
            )
            self.shuffled_entrance_pairings = shuffled_entrances.pairings
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
                vanilla_pairs.append((all_ents_list[index], all_ents_list[index + 1]))
                
            for pair in vanilla_pairs:
                if (
                    (pair[0].parent_region is not None)
                    and (pair[1].parent_region is not None)
                    and (pair[0].connected_region is None)
                    and (pair[1].connected_region is None)
                ):
                    pair[0].connect(pair[1].parent_region)
                    pair[1].connect(pair[0].parent_region)

    @override
    def set_rules(self) -> None:
        set_rules(self)

    @override
    def fill_slot_data(self) -> dict[str, int | list[tuple[str, str]] | str]:
        return {
            "goal": self.options.goal.value,
            "starting_world": self.options.starting_world.value,
            "portal_shuffle": self.options.portal_shuffle.value,
            "entrances": self.shuffled_entrance_pairings,
            "spyro_color": self.options.spyro_color.value
        }
