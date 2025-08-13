from typing import final
from BaseClasses import Location

base_spyro_location_id = 1000


@final
class SpyroLocation(Location):
    game: str = "Spyro the Dragon"


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


total_treasure: int = 14000
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
for d in (homeworld_stats, artisans_stats, keepers_stats, crafters_stats, makers_stats, weavers_stats, gnasty_stats):
    all_stats.update(d)

level_gem_threshold_locations: dict[str, int] = {}
for level, _ in all_stats:
    level_gem_threshold_locations[level + " 25% Gems"] = int(all_stats[level].treasure_count / 4)
    level_gem_threshold_locations[level + " 50% Gems"] = int(all_stats[level].treasure_count / 4)
    level_gem_threshold_locations[level + " 75% Gems"] = int(all_stats[level].treasure_count / 4)
    level_gem_threshold_locations[level + " 100% Gems"] = int(all_stats[level].treasure_count / 4)

total_gem_threshold_locations: dict[str, int] = {}
for gem_count in range(500, total_treasure, 500):
    total_gem_threshold_locations[f"{gem_count:,d} Gems"] = gem_count

# TODO: Create table of dragon names. Ugh. Can't take easy way out with numbers like with gems.
dragon_locations: list[str] = []

egg_locations: list[str] = []
for level, stats in all_stats.items():
    for count in range(stats.egg_count):
        egg_locations.append(f"{level} Egg {count:d}")

location_list: list[str] = []
for d in (level_gem_threshold_locations.keys(), total_gem_threshold_locations.keys(), dragon_locations, egg_locations):
    for item in d:
        location_list.append(item)

location_table = dict(enumerate(location_list, start=base_spyro_location_id))

flight_levels = [
    "Sunny Flight",
    "Night Flight",
    "Crystal Flight",
    "Wild Flight",
    "Icy Flight"
]
boss_levels = [
    "Toasty",
    "Doctor Shemp",
    "Blowhard",
    "Metalhead",
    "Jacques",
    "Gnasty Gnorc"
]
