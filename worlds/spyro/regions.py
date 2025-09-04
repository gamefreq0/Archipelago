"""Holds create_regions override for AP to call during gen
"""
try:
    from typing import TYPE_CHECKING
except ImportError:
    from typing_extensions import TYPE_CHECKING

from BaseClasses import Region, EntranceType, MultiWorld, Entrance
from .items import boss_items

from .locations import SpyroLocation, location_name_to_id
from .addresses import RAM, Environment

if TYPE_CHECKING:
    from .world import SpyroWorld

ENTRANCE_IN: int = 0x0
ENTRANCE_OUT: int = 0x1


def create_regions(world: "SpyroWorld"):
    """Create regions, connect static regions, create dangling entrances for generic ER

    Args:
        world: The SpyroWorld to create the logical regions for
    """
    player: int = world.player
    multiworld: MultiWorld = world.multiworld

    # Menu
    menu: Region = Region("Menu", player, multiworld)

    # Start of level/world regions. Anywhere accessible upon spawning within.
    hub_regions: dict[str, Region] = {}
    level_regions: dict[str, Region] = {}

    hub: Environment

    for hub in RAM.hub_environments:
        hub_regions[hub.name] = Region(hub.name, player, multiworld)

        for level in hub.child_environments:
            level_regions[level.name] = Region(level.name, player, multiworld)

    main_world: Region = Region("Global Stats", player, multiworld)

    balloonist_menu: Region = Region("Balloonist Menu", player, multiworld)

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

    if not hasattr(world.multiworld, "generation_is_fake"):  # If not UT gen, connect as normal
        starting_world_name: str = RAM.hub_environments[world.starting_world].name
        starting_world_name = starting_world_name.replace("_", " ")
        starting_world: Region = hub_regions[starting_world_name.title()]

        _ = menu.connect(starting_world, "Starting Homeworld")

    _ = menu.connect(main_world, "Global Stats")

    for hub in RAM.hub_environments:
        hub_region: Region = hub_regions[hub.name]

        for level in hub.child_environments:
            level_region: Region = level_regions[level.name]

            # Create dangling exit in hub for each portal, set access rule to item for portal, used for portal to
            # fly-in connection in connect_entrances
            portal_to_flyin: Entrance = hub_region.create_exit(f"{level.name} Portal")
            portal_to_flyin.randomization_type = EntranceType.TWO_WAY
            portal_to_flyin.randomization_group = ENTRANCE_IN
            portal_to_flyin.access_rule = (lambda state, level_name=level.name: state.has(level_name, player))

            # Create dangling entrance in hub for each portal, as a place to logically arrive from exiting a level
            portal_from_vortex: Entrance = hub_region.create_er_target(f"{level.name} Portal")
            portal_from_vortex.randomization_type = EntranceType.TWO_WAY
            portal_from_vortex.randomization_group = ENTRANCE_IN

            # Create dangling entrance at the level fly-in, logical destination from a portal in a hub after
            # doing connect_entrances
            level_flyin_from_portal: Entrance = level_region.create_er_target(f"{level.name} Fly-in")
            level_flyin_from_portal.randomization_type = EntranceType.TWO_WAY
            level_flyin_from_portal.randomization_group = ENTRANCE_OUT

            # Create dangling exit from level, in vanilla logically connects to the portal for the level
            # In our case, it represents both the vortex and exit from menu transitions
            level_vortex_to_portal: Entrance = level_region.create_exit(f"{level.name} Fly-in")
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
