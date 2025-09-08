from BaseClasses import Location

from .addresses import RAM, Environment

BASE_SPYRO_LOCATION_ID: int = 1000


class SpyroLocation(Location):
    game: str = "Spyro the Dragon"


class SpyroPlayerLocations():
    """Defines locations for a single player
    """

    def __init__(self, envs: list[Environment], total_gem_mult: float, max_per_env_threshold: int) -> None:
        """Defines locations after logic changes due to options"""
        self.included_locations: set[str] = set(create_locations_list(total_gem_mult, envs, max_per_env_threshold))
        return


def get_all_envs() -> list[Environment]:
    all_envs: list[Environment] = []
    for hub in RAM.hub_environments:
        all_envs.append(hub)

        for level in hub.child_environments:
            all_envs.append(level)

    return all_envs


def create_location_groups(envs: list[Environment], location_name_to_id: dict[str, int]) -> dict[str, set[str]]:
    loc_groups: dict[str, set[str]] = {}
    location_list: list[str] = list(location_name_to_id.keys())

    # Iterate through the environments, add matching locations to a group named for the environment
    for env in envs:
        loc_groups[env.name] = set()
        for location in location_list:
            if env.name in location:
                loc_groups[env.name].add(location)

    global_quarter_gems: dict[int, set[str]] = {}
    # Initialize all the sets so we can add to them later
    for index in range(1, 5):
        global_quarter_gems[index * 25] = set()

    for env in envs:
        for index in range(1, 5):
            global_quarter_gems[index * 25].add(f"{env.name} {index * 25}% Gems")

    for index in range(1, 5):
        loc_groups[f"{index * 25}% Gems"] = global_quarter_gems[index * 25]

    loc_groups["Flight Levels"] = set()
    for flight_name_prefix in ("Sunny", "Night", "Crystal", "Wild", "Icy"):
        loc_groups["Flight Levels"].update(loc_groups[f"{flight_name_prefix} Flight"])

    loc_groups["Boss Levels"] = set()
    for boss_level_name in ("Toasty", "Doctor Shemp", "Blowhard", "Metalhead", "Jacques", "Gnasty Gnorc"):
        loc_groups["Boss Levels"].update(loc_groups[boss_level_name])

    return loc_groups


def create_locations_list(
    gem_percent_mult: float,
    envs: list[Environment],
    max_per_env_threshold: int,
) -> list[str]:
    locations_list: list[str] = []
    locations_list.extend(create_total_treasure_locations(envs, gem_percent_mult))
    locations_list.extend(create_per_env_gem_locations(envs, max_per_env_threshold))
    locations_list.extend(create_dragon_locations(envs))
    locations_list.extend(create_egg_locations(envs))
    locations_list.extend(create_vortex_locations(envs))
    locations_list.append("Defeated Gnasty Gnorc")

    return locations_list


def create_total_treasure_locations(envs: list[Environment], gem_percent_mult: float) -> list[str]:
    calculated_total_treasure: int = 0

    for env in envs:
        calculated_total_treasure += int(env.total_gems * gem_percent_mult)

    total_gem_threshold_locations: list[str] = []

    for gem_count in range(500, calculated_total_treasure + 1, 500):
        total_gem_threshold_locations.append(f"{gem_count} Gems")

    return total_gem_threshold_locations


def create_per_env_gem_locations(envs: list[Environment], max_threshold: int) -> list[str]:
    gem_locs: list[str] = []
    for env in envs:
        # Create locations for each 1/4 of an environment's total gems
        for index in range(1, 5):
            if (index * 25) <= max_threshold:
                gem_locs.append(f"{env.name} {index * 25}% Gems")

    return gem_locs


def create_dragon_locations(envs: list[Environment]) -> list[str]:
    dragon_locs: list[str] = []
    for env in envs:
        for dragon_name in env.dragons:
            dragon_locs.append(f"{env.name} {dragon_name}")

    return dragon_locs


def create_egg_locations(envs: list[Environment]) -> list[str]:
    egg_locs: list[str] = []
    for env in envs:
        for egg_name in env.eggs:
            egg_locs.append(f"{env.name} {egg_name}")

    return egg_locs


def create_vortex_locations(envs: list[Environment]) -> list[str]:
    vortex_locs: list[str] = []
    for env in envs:
        if env.has_vortex:
            vortex_locs.append(f"{env.name} Vortex")

    return vortex_locs


static_locations: dict[str, int]
static_loc_groups: dict[str, set[str]]
static_locations = {
    v: k for k, v in enumerate(create_locations_list(1.0, get_all_envs(), 100), start=BASE_SPYRO_LOCATION_ID)
}
static_loc_groups = create_location_groups(get_all_envs(), static_locations)
