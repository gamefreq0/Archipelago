from typing import TYPE_CHECKING
try:
    from typing import final
except ImportError:
    if TYPE_CHECKING:
        from typing import final
    else:
        from typing_extensions import final

from BaseClasses import Location

from .addresses import RAM

BASE_SPYRO_LOCATION_ID = 1000


@final
class SpyroLocation(Location):
    game: str = "Spyro the Dragon"


# TODO: Remove class, duplicates stuff from addresses.RAM
class LevelStats():
    """Contains useful info for tracking level totals

    Attributes:
    egg_count: int
        The total number of eggs within the level
    treasure_count: int
        The total treasure within the level
    dragon_count: int
        The total number of dragon statues within the level
    has_vortex: bool
        Whether the level has a vortex to reach at the end
    reached_vortex: bool
        Whether the player has exited the level via the vortex
    """
    egg_count: int
    treasure_count: int
    dragon_count: int
    has_vortex: bool
    reached_vortex: bool

    def __init__(
        self, egg_count: int = 0, treasure_count: int = 0, dragon_count: int = 0, has_vortex: bool = True
    ) -> None:
        self.egg_count = egg_count
        self.treasure_count = treasure_count
        self.dragon_count = dragon_count
        self.has_vortex = has_vortex
        self.reached_vortex = False


total_treasure: int = 0

# TODO: Remove this in favor of dynamically calculating during gen, based on excluded levels/hubs
for hub in RAM.hub_environments:
    total_treasure += hub.total_gems

    for level in hub.child_environments:
        total_treasure += level.total_gems

homeworld_stats = {
    "Artisans": LevelStats(0, 100, 4, False),
    "Peace Keepers": LevelStats(1, 200, 3, False),
    "Magic Crafters": LevelStats(2, 300, 3, False),
    "Beast Makers": LevelStats(0, 300, 2, False),
    "Dream Weavers": LevelStats(0, 300, 3, False),
    "Gnasty's World": LevelStats(0, 200, 2, False)
}

artisans_stats = {
    "Stone Hill": LevelStats(1, 200, 4),
    "Dark Hollow": LevelStats(0, 100, 3),
    "Town Square": LevelStats(1, 200, 4),
    "Toasty": LevelStats(0, 100, 1),
    "Sunny Flight": LevelStats(0, 300, 0, False)
}

keepers_stats = {
    "Dry Canyon": LevelStats(1, 400, 4),
    "Cliff Town": LevelStats(1, 400, 3),
    "Ice Cavern": LevelStats(0, 400, 5),
    "Doctor Shemp": LevelStats(0, 300, 1),
    "Night Flight": LevelStats(0, 300, 0, False)
}

crafters_stats = {
    "Alpine Ridge": LevelStats(1, 500, 4),
    "High Caves": LevelStats(2, 500, 3),
    "Wizard Peak": LevelStats(2, 500, 1),
    "Blowhard": LevelStats(0, 400, 1),
    "Crystal Flight": LevelStats(0, 300, 0, False)
}

makers_stats = {
    "Terrace Village": LevelStats(0, 400, 2),
    "Misty Bog": LevelStats(0, 500, 4),
    "Tree Tops": LevelStats(0, 500, 3),
    "Metalhead": LevelStats(0, 500, 1),
    "Wild Flight": LevelStats(0, 300, 0, False),
}

weavers_stats = {
    "Dark Passage": LevelStats(0, 500, 5),
    "Lofty Castle": LevelStats(0, 400, 3),
    "Haunted Towers": LevelStats(0, 500, 3),
    "Jacques": LevelStats(0, 500, 2),
    "Icy Flight": LevelStats(0, 300, 0, False)
}

gnasty_stats = {
    "Gnorc Cove": LevelStats(0, 400, 2),
    "Twilight Harbor": LevelStats(0, 400, 2),
    "Gnasty Gnorc": LevelStats(0, 500, 0, False),
    "Gnasty's Loot": LevelStats(0, 2000, 0)
}

all_stats: dict[str, LevelStats] = {}

for d in [
        homeworld_stats,
        artisans_stats,
        keepers_stats,
        crafters_stats,
        makers_stats,
        weavers_stats,
        gnasty_stats
]:
    all_stats.update(d)

level_gem_threshold_locations: list[str] = []

for hub in RAM.hub_environments:
    quarter_gems_hub = int(hub.total_gems / 4)

    for index in range(1, 5):
        level_gem_threshold_locations.append(f"{hub.name} {index * 25}% Gems")

    for level in hub.child_environments:
        quarter_gems_level = int(level.total_gems / 4)

        for index in range(1, 5):
            level_gem_threshold_locations.append(f"{level.name} {index * 25}% Gems")

total_gem_threshold_locations: list[str] = []

for gem_count in range(500, total_treasure + 1, 500):
    total_gem_threshold_locations.append(f"{gem_count} Gems")

# TODO: Create table of dragon names. Ugh. Can't take easy way out with numbers like with gems.
dragon_locations: list[str] = []

vortex_locations: list[str] = []

for hub in RAM.hub_environments:
    for level in hub.child_environments:
        if level.has_vortex:
            vortex_locations.append(f"{level.name} Vortex")

# TODO: Restructure this bit based on eggs structure in RAM.Environments
egg_locations: list[str] = []

for level, stats in all_stats.items():
    for count in range(stats.egg_count):
        egg_locations.append(f"{level} Egg {count + 1:d}")

misc_locations: list[str] = []
misc_locations.append("Defeated Gnasty Gnorc")

location_list: list[str] = []

for d in [
    # TODO: implement dragon locations, egg locations
    level_gem_threshold_locations,
    total_gem_threshold_locations,
    # dragon_locations
    # egg_locations,
    vortex_locations,
    misc_locations,
]:
    for item in d:
        location_list.append(item)

location_id_to_name = dict(enumerate(location_list, start=BASE_SPYRO_LOCATION_ID))
location_name_to_id = {v: k for k, v in location_id_to_name.items()}

flight_levels = {
    "Sunny Flight",
    "Night Flight",
    "Crystal Flight",
    "Wild Flight",
    "Icy Flight"
}

boss_levels = {
    "Toasty",
    "Doctor Shemp",
    "Blowhard",
    "Metalhead",
    "Jacques",
    "Gnasty Gnorc"
}

meta_groups = {
    "Flight Levels": set(flight_levels),
    "Boss Levels": set(boss_levels)
}

level_groups: dict[str, set[str]] = {}
grouped_locations: dict[str, set[str]] = {}

for meta_group in meta_groups:
    # Initialize these so we can just .update() them later
    grouped_locations[meta_group] = set()

for hub in RAM.hub_environments:
    for level in hub.child_environments:
        cur_level_set: set[str] = set()

        for location in location_list:
            if level.name in location:
                cur_level_set.add(location)

        level_groups[level.name] = cur_level_set

for level, locations in level_groups.items():
    for meta_group, level_group in meta_groups.items():
        if level in level_group:
            grouped_locations[meta_group].update(locations)

    grouped_locations[level] = locations
