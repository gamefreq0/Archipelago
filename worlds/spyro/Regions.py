from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region, EntranceType
from worlds.spyro.Items import boss_items

from .Locations import SpyroLocation, location_table

if TYPE_CHECKING:
    from . import SpyroWorld

ENTRANCE_IN: int = 0x0
ENTRANCE_OUT: int = 0x1

hub_names: dict[str, list[str]]

hub_names = {
    "Artisans": [
        "Stone Hill",
        "Dark Hollow",
        "Town Square",
        "Toasty",
        "Sunny Flight"
    ],
    "Peace Keepers": [
        "Dry Canyon",
        "Cliff Town",
        "Ice Cavern",
        "Doctor Shemp",
        "Night Flight"
    ],
    "Magic Crafters": [
        "Alpine Ridge",
        "High Caves",
        "Wizard Peak",
        "Blowhard",
        "Crystal Flight"
    ],
    "Beast Makers": [
        "Terrace Village",
        "Misty Bog",
        "Tree Tops",
        "Metalhead",
        "Wild Flight"
    ],
    "Dream Weavers": [
        "Dark Passage",
        "Lofty Castle",
        "Haunted Towers",
        "Jacques",
        "Icy Flight"
    ],
    "Gnasty's World": [
        "Gnorc Cove",
        "Twilight Harbor",
        "Gnasty Gnorc",
        "Gnasty's Loot"
    ]
}


def create_regions(world: "SpyroWorld"):
    options = world.options
    player = world.player
    multiworld = world.multiworld

    # Menu
    menu = Region("Menu", player, multiworld)

    # Start of level/world regions. Anywhere accessible upon spawning within.
    hub_regions: dict[str, Region] = {}
    level_regions: dict[str, Region] = {}
    for hub in hub_names.items():
        hub_name, level_names = hub
        hub_regions[hub_name] = Region(hub_name, player, multiworld)
        for level_name in level_names:
            level_regions[level_name] = Region(level_name, player, multiworld)

    main_world = Region("Global Stats", player, multiworld)

    balloonist_menu = Region("Balloonist Menu", player, multiworld)

    regions: list[Region] = [
        menu,
        main_world, balloonist_menu
    ]

    for hub in hub_regions.items():
        hub_name, hub_region = hub
        regions.append(hub_region)
    for level in level_regions.items():
        level_name, level_region = level
        regions.append(level_region)

    # Add matching locations to their level region. This will be very manual if move shuffle becomes a thing, because
    # not all locations will be accessible from the start of the level. Oh, joy.
    for region in regions:
        if region != menu:
            for location in location_table:
                location_name = location_table[location]
                if (region.name in location_table[location]):
                    region.locations.append(SpyroLocation(
                        player, location_name,
                        world.location_name_to_id[location_name], region
                    ))
                elif (region == main_world) and (
                    "00 Gems" in location_table[location]
                ):
                    region.locations.append(SpyroLocation(
                        player, location_name,
                        world.location_name_to_id[location_name], region
                    ))

    # TODO: Create regions within levels for move shuffle eventually.

    multiworld.regions.extend(regions)

    starting_world_name = options.starting_world.current_key
    starting_world_name = starting_world_name.replace("_", " ")
    starting_world: Region = hub_regions[starting_world_name.title()]

    _ = menu.connect(starting_world, "Starting Homeworld")
    _ = menu.connect(main_world, "Global Stats")
    for hub in hub_regions.items():
        hub_name, hub_region = hub
        for level_name in hub_names[hub_name]:
            level_region = level_regions[level_name]
            portal_to_flyin = hub_region.create_exit(f"{level_name} Portal")
            portal_to_flyin.randomization_type = EntranceType.TWO_WAY
            portal_to_flyin.randomization_group = ENTRANCE_IN
            portal_to_flyin.access_rule = (
                lambda state, level_name=level_name: state.has(
                    level_name, player
                )
            )
            portal_from_vortex = hub_region.create_er_target(
                f"{level_name} Portal"
            )
            portal_from_vortex.randomization_type = EntranceType.TWO_WAY
            portal_from_vortex.randomization_group = ENTRANCE_IN
            level_flyin_from_portal = level_region.create_er_target(
                f"{level_name} Fly-in"
            )
            level_flyin_from_portal.randomization_type = EntranceType.TWO_WAY
            level_flyin_from_portal.randomization_group = ENTRANCE_OUT
            level_vortex_to_portal = level_region.create_exit(
                f"{level_name} Fly-in"
            )
            level_vortex_to_portal.randomization_type = EntranceType.TWO_WAY
            level_vortex_to_portal.randomization_group = ENTRANCE_OUT
        _ = hub_region.connect(balloonist_menu, f"{hub_name} Balloonist")
        if "Gnasty" not in hub_name:
            _ = balloonist_menu.connect(
                    hub_region, f"Balloonist to {hub_name}", lambda state,
                    hub_name=hub_name: state.has(hub_name, player)
            )
    _ = balloonist_menu.connect(
            hub_regions["Gnasty's World"], "Balloonist to Gnorc Gnexus",
            lambda state: state.has_all(boss_items, player)
    )
