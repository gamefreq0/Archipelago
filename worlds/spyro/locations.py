from BaseClasses import Location

from .addresses import RAM

BASE_SPYRO_LOCATION_ID: int = 1000


class SpyroLocation(Location):
    game: str = "Spyro the Dragon"


total_treasure: int = 0

# TODO: Remove this in favor of dynamically calculating during gen, based on excluded levels/hubs
for hub in RAM.hub_environments:
    total_treasure += hub.total_gems

    for level in hub.child_environments:
        total_treasure += level.total_gems


level_gem_threshold_locations: list[str] = []
dragon_locations: list[str] = []
egg_locations: list[str] = []

for hub in RAM.hub_environments:

    # Add locations for each 1/4 of a hub's total gems
    for index in range(1, 5):
        level_gem_threshold_locations.append(f"{hub.name} {index * 25}% Gems")

    # Add locations for dragons as needed
    for dragon_name in hub.dragons:
        dragon_locations.append(f"{hub.name} {dragon_name}")

    # Add locations for eggs as needed
    for egg_name in hub.eggs:
        egg_locations.append(f"{hub.name} {egg_name}")

    for level in hub.child_environments:

        # Add locations for each 1/4 of a level's total gems
        for index in range(1, 5):
            level_gem_threshold_locations.append(f"{level.name} {index * 25}% Gems")

        # Add locations for dragons as needed
        for dragon_name in level.dragons:
            dragon_locations.append(f"{level.name} {dragon_name}")

        # Add locations for eggs as needed
        for egg_name in level.eggs:
            egg_locations.append(f"{level.name} {egg_name}")

total_gem_threshold_locations: list[str] = []

for gem_count in range(500, total_treasure + 1, 500):
    total_gem_threshold_locations.append(f"{gem_count} Gems")

vortex_locations: list[str] = []

for hub in RAM.hub_environments:
    for level in hub.child_environments:
        if level.has_vortex:
            vortex_locations.append(f"{level.name} Vortex")

misc_locations: list[str] = []
misc_locations.append("Defeated Gnasty Gnorc")

location_list: list[str] = []

location_list.extend(level_gem_threshold_locations)
location_list.extend(total_gem_threshold_locations)
location_list.extend(dragon_locations)
location_list.extend(egg_locations)
location_list.extend(vortex_locations)
location_list.extend(misc_locations)

location_id_to_name: dict[int, str] = dict(enumerate(location_list, start=BASE_SPYRO_LOCATION_ID))
location_name_to_id: dict[str, int] = {v: k for k, v in location_id_to_name.items()}

flight_levels: set[str] = {
    "Sunny Flight",
    "Night Flight",
    "Crystal Flight",
    "Wild Flight",
    "Icy Flight"
}

boss_levels: set[str] = {
    "Toasty",
    "Doctor Shemp",
    "Blowhard",
    "Metalhead",
    "Jacques",
    "Gnasty Gnorc"
}

gems_25: set[str] = set()
gems_50: set[str] = set()
gems_75: set[str] = set()
gems_100: set[str] = set()

for hub in RAM.hub_environments:
    gems_25.add(f"{hub.name} 25% Gems")
    gems_50.add(f"{hub.name} 50% Gems")
    gems_75.add(f"{hub.name} 75% Gems")
    gems_100.add(f"{hub.name} 100% Gems")

    for level in hub.child_environments:
        gems_25.add(f"{level.name} 25% Gems")
        gems_50.add(f"{level.name} 50% Gems")
        gems_75.add(f"{level.name} 75% Gems")
        gems_100.add(f"{level.name} 100% Gems")

meta_groups: dict[str, set[str]] = {
    "Flight Levels": set(flight_levels),
    "Boss Levels": set(boss_levels),
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

grouped_locations["25% Gems"] = gems_25
grouped_locations["50% Gems"] = gems_50
grouped_locations["75% Gems"] = gems_75
grouped_locations["100% Gems"] = gems_100
