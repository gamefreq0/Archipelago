from dataclasses import dataclass

from Options import Choice, DeathLink, PerGameCommonOptions, FreeText, Toggle, Range


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
    Also accepts "random" as an option, which will roll a random RGB value with full alpha

    Note that a value of FFFFFF00 will result in the vanilla colors.
    """

    display_name: str = "Spyro Color"
    default: str = "FFFFFF00"


class GlobalGemThresholdOption(Range):
    """A percentage multiplier for the every 500 gem total threshold locations. 50, for example, will mean that getting
    50% of the gems in every accessible level will logically be expected at any given point. Accepts a range between
    1 and 100.
    """

    display_name: str = "Global Gem Threshold Percentage"
    default: int = 100
    range_end: int = 100
    range_start: int = 1


class MaxLevelGemThresholdOption(Choice):
    """The maximum gem threshold locations to include for each level/hub. Corresponds to the maximum percentage of gems
    per area to create locations for. Useful for reducing amount of filler relative to useful items for this game.
    """
    display_name: str = "Maximum Per-Area Gem Threshold"
    option_0: int = 0
    option_25: int = 25
    option_50: int = 50
    option_75: int = 75
    option_100: int = 100
    default: int = option_100


@dataclass
class SpyroOptions(PerGameCommonOptions):
    goal: GoalOption
    starting_world: StartingHomeworldOption
    portal_shuffle: PortalShuffleOption
    spyro_color: SpyroColorOption
    global_gem_percent: GlobalGemThresholdOption
    max_level_gem_threshold: MaxLevelGemThresholdOption
    death_link: DeathLink
