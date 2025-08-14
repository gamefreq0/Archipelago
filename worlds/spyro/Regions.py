from os import name
from typing import TYPE_CHECKING

from BaseClasses import Region

from .Locations import SpyroLocation, location_table

if TYPE_CHECKING:
    from . import SpyroWorld

# TODO: Handle entrances for level shuffle


def create_regions(world: "SpyroWorld"):
    options = world.options
    player = world.player
    multiworld = world.multiworld

    # Menu
    menu = Region("Menu", player, multiworld)

    # Start of level/world regions. Anywhere accessible upon spawning within.
    hub_artisans = Region("Artisans", player, multiworld)
    level_stone_hill = Region("Stone Hill", player, multiworld)
    level_dark_hollow = Region("Dark Hollow", player, multiworld)
    level_town_square = Region("Town Square", player, multiworld)
    level_toasty = Region("Toasty", player, multiworld)
    level_sunny_flight = Region("Sunny Flight", player, multiworld)

    hub_keepers = Region("Peace Keepers", player, multiworld)
    level_dry_canyon = Region("Dry Canyon", player, multiworld)
    level_cliff_town = Region("Cliff Town", player, multiworld)
    level_ice_cavern = Region("Ice Cavern", player, multiworld)
    level_doctor_shemp = Region("Doctor Shemp", player, multiworld)
    level_night_flight = Region("Night Flight", player, multiworld)

    hub_crafters = Region("Magic Crafters", player, multiworld)
    level_alpine_ridge = Region("Alpine Ridge", player, multiworld)
    level_high_caves = Region("High Caves", player, multiworld)
    level_wizard_peak = Region("Wizard Peak", player, multiworld)
    level_blowhard = Region("Blowhard", player, multiworld)
    level_crystal_flight = Region("Crystal Flight", player, multiworld)

    hub_makers = Region("Beast Makers", player, multiworld)
    level_terrace_village = Region("Terrace Village", player, multiworld)
    level_misty_bog = Region("Misty Bog", player, multiworld)
    level_tree_tops = Region("Tree Tops", player, multiworld)
    level_metalhead = Region("Metalhead", player, multiworld)
    level_wild_flight = Region("Wild Flight", player, multiworld)

    hub_weavers = Region("Dream Weavers", player, multiworld)
    level_dark_passage = Region("Dark Passage", player, multiworld)
    level_lofty_castle = Region("Lofty Castle", player, multiworld)
    level_haunted_towers = Region("Haunted Towers", player, multiworld)
    level_jacques = Region("Jacques", player, multiworld)
    level_icy_flight = Region("Icy Flight", player, multiworld)

    hub_gnasty = Region("Gnasty's World", player, multiworld)
    level_gnorc_cove = Region("Gnorc Cove", player, multiworld)
    level_twilight_harbor = Region("Twilight Harbor", player, multiworld)
    level_gnasty_gnorc = Region("Gnasty Gnorc", player, multiworld)
    level_loot = Region("Gnasty's Loot", player, multiworld)

    regions = [
        menu,
        hub_artisans, level_stone_hill, level_dark_hollow, level_town_square, level_toasty, level_sunny_flight,
        hub_keepers, level_dry_canyon, level_cliff_town, level_ice_cavern, level_doctor_shemp, level_night_flight,
        hub_crafters, level_alpine_ridge, level_high_caves, level_wizard_peak, level_blowhard, level_crystal_flight,
        hub_makers, level_terrace_village, level_misty_bog, level_tree_tops, level_metalhead, level_wild_flight,
        hub_weavers, level_dark_passage, level_lofty_castle, level_haunted_towers, level_jacques, level_icy_flight,
        hub_gnasty, level_gnorc_cove, level_twilight_harbor, level_gnasty_gnorc, level_loot
    ]

    # Add matching locations to their level region. This will be very manual if move shuffle becomes a thing, because
    # not all locations will be accessible from the start of the level. Oh, joy.
    for region in regions:
        if region != menu:
            for location in location_table:
                if region.name in location_table[location]:
                    region.locations.append(SpyroLocation(world.player, location_table[location]))

    # TODO: Create regions within levels for move shuffle eventually.
    # TODO: Move following bit elsewhere for ER, to account for the disconnect between starting area and
    # ability to actually reach the balloonist. Won't matter until move shuffle, though.

    _ = menu.add_exits(
            {hub_artisans.name: "Balloonist"},
            {hub_artisans.name: lambda state: state.has(hub_artisans.name, world.player)}
        )
    _ = menu.add_exits(
            {hub_keepers.name: "Balloonist"},
            {hub_keepers.name: lambda state: state.has(hub_keepers.name, world.player)}
        )
    _ = menu.add_exits(
            {hub_crafters.name: "Balloonist"},
            {hub_crafters.name: lambda state: state.has(hub_crafters.name, world.player)}
        )
    _ = menu.add_exits(
            {hub_makers.name: "Balloonist"},
            {hub_makers.name: lambda state: state.has(hub_makers.name, world.player)}
        )
    _ = menu.add_exits(
            {hub_weavers.name: "Balloonist"},
            {hub_weavers.name: lambda state: state.has(hub_weavers.name, world.player)}
        )
    _ = menu.add_exits(
            {hub_gnasty.name: "Balloonist"},
            {hub_gnasty.name: lambda state: state.has(hub_gnasty.name, world.player)}
        )
    multiworld.regions.extend(regions)
