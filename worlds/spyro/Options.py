from typing import final

from dataclasses import dataclass
from Options import Choice, DeathLink, PerGameCommonOptions, FreeText


@final
class GoalOption(Choice):
    """Choose the victory condition for this world.

    gnasty: Defeat Gnasty Gnorc
    loot: Reach the vortex at the end of Gnasty's Loot
    """

    display_name = "Goal"
    option_gnasty = 0x00
    option_loot = 0x01
    default = option_gnasty


@final
class StartingHomeworldOption(Choice):
    """Choose which homeworld to start in.
    artisans: Start in the Artisans
    keepers: Start in Peace Keepers
    crafters: Start in Magic Crafters
    makers: Start in Beast Makers
    weavers: Start in Dream Weavers
    """

    display_name = "Starting Homeworld"
    option_artisans = 0x00
    option_keepers = 0x01
    option_crafters = 0x02
    option_makers = 0x03
    option_weavers = 0x04
    default = option_artisans


@final
class SpyroColorOption(FreeText):
    """Choose a color to tint Spyro, in RGBA format.
    Note that a value of FFFFFF00 will result in the vanilla colors.
    """

    display_name = "Spyro Color"
    default = "FFFFFF00"


@dataclass
class SpyroOptions(PerGameCommonOptions):
    goal: GoalOption
    starting_world: StartingHomeworldOption
    spyro_color: SpyroColorOption
    death_link: DeathLink
    