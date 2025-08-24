from dataclasses import dataclass

try:
    from typing import final
except ImportError:
    from typing_extensions import final

from Options import Choice, DeathLink, PerGameCommonOptions, FreeText, Toggle


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

    Options are:
    artisans
    peace_keepers
    magic_crafters
    beast_makers
    dream_weavers
    """

    display_name = "Starting Homeworld"
    option_artisans = 0x00
    option_peace_keepers = 0x01
    option_magic_crafters = 0x02
    option_beast_makers = 0x03
    option_dream_weavers = 0x04
    default = option_artisans


@final
class PortalShuffleOption(Toggle):
    """If enabled, where a portal leads to is shuffled."""

    display_name = "Portal Shuffle"
    default = False


@final
class SpyroColorOption(FreeText):
    """Choose a color to tint Spyro, in RGBA format.

    Note that a value of FFFFFF00 will result in the vanilla colors.
    """

    display_name = "Spyro Color"
    default = "FFFFFF00"


@dataclass
@final
class SpyroOptions(PerGameCommonOptions):
    goal: GoalOption
    starting_world: StartingHomeworldOption
    portal_shuffle: PortalShuffleOption
    spyro_color: SpyroColorOption
    death_link: DeathLink
