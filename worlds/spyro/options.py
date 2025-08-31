from dataclasses import dataclass

from Options import Choice, DeathLink, PerGameCommonOptions, FreeText, Toggle


class GoalOption(Choice):
    """Choose the victory condition for this world.

    gnasty: Defeat Gnasty Gnorc
    loot: Reach the vortex at the end of Gnasty's Loot
    """

    display_name: str = "Goal"
    option_gnasty: int = 0x00
    option_loot: int = 0x01
    default: int = option_gnasty


class StartingHomeworldOption(Choice):
    """Choose which homeworld to start in.

    Options are:
    artisans
    peace_keepers
    magic_crafters
    beast_makers
    dream_weavers
    """

    display_name: str = "Starting Homeworld"
    option_artisans: int = 0x00
    option_peace_keepers: int = 0x01
    option_magic_crafters: int = 0x02
    option_beast_makers: int = 0x03
    option_dream_weavers: int = 0x04
    default: int = option_artisans


class PortalShuffleOption(Toggle):
    """If enabled, where a portal leads to is shuffled."""

    display_name: str = "Portal Shuffle"
    default: bool = False


class SpyroColorOption(FreeText):
    """Choose a color to tint Spyro, in RGBA format.

    Note that a value of FFFFFF00 will result in the vanilla colors.
    """

    display_name: str = "Spyro Color"
    default: str = "FFFFFF00"


@dataclass
class SpyroOptions(PerGameCommonOptions):
    goal: GoalOption
    starting_world: StartingHomeworldOption
    portal_shuffle: PortalShuffleOption
    spyro_color: SpyroColorOption
    death_link: DeathLink
