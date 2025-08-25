try:
    from typing import TYPE_CHECKING
except ImportError:
    from typing_extensions import TYPE_CHECKING

from BaseClasses import ItemClassification, Region, EntranceType
from .items import SpyroItem, boss_items

from .locations import SpyroLocation, location_name_to_id
from .addresses import RAM, Environment

if TYPE_CHECKING:
    from .world import SpyroWorld

ENTRANCE_IN: int = 0x0
ENTRANCE_OUT: int = 0x1


def create_regions(world: "SpyroWorld"):
    options = world.options
    player = world.player
    multiworld = world.multiworld

    # Menu
    menu = Region("Menu", player, multiworld)

    # Start of level/world regions. Anywhere accessible upon spawning within.
    hub_regions: dict[str, Region] = {}
    level_regions: dict[str, Region] = {}

    hub: Environment

    for hub in RAM.hub_environments:
        hub_regions[hub.name] = Region(hub.name, player, multiworld)

        for level in hub.child_environments:
            level_regions[level.name] = Region(level.name, player, multiworld)

    main_world = Region("Global Stats", player, multiworld)

    balloonist_menu = Region("Balloonist Menu", player, multiworld)

    regions: list[Region] = [
        menu,
        main_world, balloonist_menu
    ]

    for hub in RAM.hub_environments:
        regions.append(hub_regions[hub.name])
        for level in hub.child_environments:
            regions.append(level_regions[level.name])

    # Add matching locations to their level region. This will be very manual
    # if move shuffle becomes a thing, because not all locations will be
    # accessible from the start of the level. Oh, joy.
    for region in regions:
        if region != menu:
            for location_name, location_id in location_name_to_id.items():
                if region.name in location_name:
                    region.locations.append(SpyroLocation(player, location_name, location_id, region))
                elif (region == main_world) and ("00 Gems" in location_name):
                    region.locations.append(SpyroLocation(player, location_name, location_id, region))

    world.get_location("Defeated Gnasty Gnorc").parent_region = level_regions["Gnasty Gnorc"]

    # TODO: Create regions within levels for move shuffle eventually.

    multiworld.regions.extend(regions)

    starting_world_name = options.starting_world.current_key
    starting_world_name = starting_world_name.replace("_", " ")
    starting_world: Region = hub_regions[starting_world_name.title()]

    _ = menu.connect(starting_world, "Starting Homeworld")
    _ = menu.connect(main_world, "Global Stats")
    for hub in RAM.hub_environments:
        hub_region = hub_regions[hub.name]
        level: Environment
        for level in hub.child_environments:
            level_region = level_regions[level.name]
            portal_to_flyin = hub_region.create_exit(f"{level.name} Portal")
            portal_to_flyin.randomization_type = EntranceType.TWO_WAY
            portal_to_flyin.randomization_group = ENTRANCE_IN
            portal_to_flyin.access_rule = (lambda state, level_name=level.name: state.has(level_name, player))
            portal_from_vortex = hub_region.create_er_target(f"{level.name} Portal")
            portal_from_vortex.randomization_type = EntranceType.TWO_WAY
            portal_from_vortex.randomization_group = ENTRANCE_IN
            level_flyin_from_portal = level_region.create_er_target(f"{level.name} Fly-in")
            level_flyin_from_portal.randomization_type = EntranceType.TWO_WAY
            level_flyin_from_portal.randomization_group = ENTRANCE_OUT
            level_vortex_to_portal = level_region.create_exit(f"{level.name} Fly-in")
            level_vortex_to_portal.randomization_type = EntranceType.TWO_WAY
            level_vortex_to_portal.randomization_group = ENTRANCE_OUT

        _ = hub_region.connect(balloonist_menu, f"{hub.name} Balloonist")

        if hub.name != "Gnasty's World":
            _ = balloonist_menu.connect(
                    hub_region, f"Balloonist to {hub.name}", lambda state,
                    hub_name=hub.name: state.has(hub_name, player)
            )

    _ = balloonist_menu.connect(
            hub_regions["Gnasty's World"], "Balloonist to Gnorc Gnexus",
            lambda state: state.has_all(boss_items, player)
    )

    for hub in RAM.hub_environments:
        # TODO: Redo this bit with logic for individual gem colors, for move shuffle
        # Add number of virtual gems to a hub's region based on that hub's total gems
        for gem_index in range(0, hub.total_gems, 100):
            add_event_location(
                world,
                hub_regions[hub.name],
                f"{hub.name} 100 Gems set {int(gem_index / 100) + 1}",
                "100 Gems"
            )

        for level in hub.child_environments:
            # Add number of virtual gems to a level's region based on that level's total gems
            for gem_index in range(0, level.total_gems, 100):
                add_event_location(
                    world,
                    level_regions[level.name],
                    f"{level.name} 100 Gems set {int(gem_index / 100) + 1}",
                    "100 Gems"
                )


def add_event_location(world: "SpyroWorld", region: Region, name: str, event_name: str) -> None:
    """Add a virtual, named location to a given region, containing a given event item

    Args:
        world: The world this is called from, for getting the current player
        region: The region to add the virtual location to
        name: The name of the virtual location
        event_name: The name of the event item to place at the location
    """
    location: SpyroLocation = SpyroLocation(world.player, name, None, region)
    region.locations.append(location)
    location.place_locked_item(SpyroItem(event_name, ItemClassification.progression, None, world.player))
