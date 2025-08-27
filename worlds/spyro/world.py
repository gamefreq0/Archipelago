from logging import warning

from typing import TYPE_CHECKING
try:
    from typing import final, override, ClassVar
except ImportError:
    if TYPE_CHECKING:
        from typing import final, override, ClassVar
    else:
        from typing_extensions import final, override, ClassVar

from BaseClasses import Entrance, MultiWorld, Region
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
from .addresses import RAM


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

    _goal: str
    _portal_shuffle: int
    _death_link: int
    _starting_world: int
    _spyro_color: int

    def __init__(self, multiworld: "MultiWorld", player: int):
        super().__init__(multiworld, player)
        self._goal = "gnasty"
        self._portal_shuffle = 0
        self._death_link = 0
        self._starting_world = 0
        self._spyro_color = -1
        self.itempool: list[SpyroItem] = []
        self.shuffled_entrance_pairings: list[tuple[str, str]] = []

    @property
    def goal(self) -> str:
        """Goal for this world

        Returns:
            The goal name
        """
        return self._goal

    @goal.setter
    def goal(self, value: str) -> None:
        if value in ("gnasty", "loot"):
            self._goal = value
        else:
            raise OptionError(f"Invalid value {value} for goal for player {self.player_name}")

    @property
    def portal_shuffle(self) -> bool:
        """Whether portals are shuffled

        Returns:
            bool
        """
        return self._portal_shuffle == 1

    @portal_shuffle.setter
    def portal_shuffle(self, value: bool) -> None:
        if value:
            self._portal_shuffle = 1
        else:
            self._portal_shuffle = 0

    @property
    def death_link(self) -> bool:
        """Whether death link is on

        Returns:
            bool
        """
        return self._death_link == 1

    @death_link.setter
    def death_link(self, value: bool) -> None:
        if value:
            warning(f"Deathlink for {self.game} doesn't work yet. Option will be ignored.")
            self._death_link = 1
        else:
            self._death_link = 0

    @property
    def starting_world(self) -> int:
        """Which world the player starts in

        Returns:
            The index of the homeworld
        """
        return self._starting_world

    @starting_world.setter
    def starting_world(self, value: int) -> None:
        if value in range(5):
            self._starting_world = value
        else:
            raise OptionError(
                "This shouldn't happen! Let the dev of the apworld for " +
                f"{self.game} know that starting_homeworld broke!"
            )

    @property
    def spyro_color(self) -> int:
        """Spyro's RGBA color"""
        return self._spyro_color

    @spyro_color.setter
    def spyro_color(self, value: str) -> None:
        try:
            color: int = int(value, 16)
        except ValueError as exc:
            raise OptionError(
                f"{self.player_name}'s spyro_color value of " + f'"{value}" is not a valid RGBA color.'
            ) from exc
        self._spyro_color = color

    @override
    def generate_early(self) -> None:
        self.goal = self.options.goal.get_option_name(self.options.goal.value).lower()
        self.itempool = []
        self.starting_world = self.options.starting_world.value
        self.spyro_color = self.options.spyro_color.value
        self.death_link = self.options.death_link.value == 1
        self.portal_shuffle = self.options.portal_shuffle.value == 1

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

    @override
    def create_items(self) -> None:
        for name in homeworld_access:
            if name == RAM.hub_environments[self.starting_world].name:
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

        if self.goal == "gnasty":
            self.get_location("Defeated Gnasty Gnorc").place_locked_item(victory)
        elif self.goal == "loot":
            self.get_location("Gnasty's Loot Vortex").place_locked_item(victory)

        self.multiworld.itempool += self.itempool

    @override
    def connect_entrances(self) -> None:
        if not hasattr(self.multiworld, "generation_is_fake"):  # If not in UT gen, do the rest
            if self.portal_shuffle:
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
            "goal": self.goal,
            "starting_world": self.starting_world,
            "portal_shuffle": 1 if self.portal_shuffle else 0,
            "entrances": self.shuffled_entrance_pairings,
            "spyro_color": self.spyro_color,
        }

    def interpret_slot_data(self, slot_data: dict[str, any]) -> None:
        """Method called by UT, where we can handle deferred logic stuff

        Args:
            slot_data: Holds slot data, indexed by name of the piece of data
        """
        # Connect starting homeworld to menu region
        regions: dict[str, Region] = self.multiworld.regions.region_cache[self.player]
        entrances: dict[str, Entrance] = self.multiworld.regions.entrance_cache[self.player]

        starting_homeworld_index: int = slot_data["starting_world"]
        starting_homeworld = RAM.hub_environments[starting_homeworld_index].name
        starting_region: Region = regions[starting_homeworld]
        menu: Region = regions["Menu"]

        _ = menu.connect(starting_region, "Starting Homeworld")

        # Connect entrances
        if slot_data["portal_shuffle"] == 1:
            pairings: list[tuple[str, str]] = slot_data["entrances"]
            for pairing in pairings:
                entrances[pairing[0]].connect(entrances[pairing[1]].parent_region)
                entrances[pairing[1]].connect(entrances[pairing[0]].parent_region)
        else:
            all_entrances = entrances
            all_ents_list: list[Entrance] = []

            for entrance in all_entrances.values():
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
