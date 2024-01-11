from __future__ import annotations

from dataclasses import dataclass
from Options import Choice, Option, PerGameCommonOptions

from typing import Dict


class DebugOption(Choice):
    """Choose current Debug Settings

        Off: No debug settings
        Early Items: Gadgets will be placed in first two levels
        Early Keys: Keys will be placed in the first two levels

        Supported values: off, item, key
        Default value: off
        """

    display_name = "Debug Option"
    option_off = 0x00
    option_item = 0x01
    option_key = 0x02
    default = option_off


class GoalOption(Choice):
    """Choose end goal

        first: First final boss at Monkey Madness
        second: 100% boss at Peak Point Matrix

        Supported values: first, second
        Default value: first
    """

    display_name = "Goal"
    option_first = 0x00
    option_second = 0x01
    default = option_first


class LogicOption(Choice):
    """Choose expected trick knowledge

        glitchless: no glitches required
        noij: all glitches except infinite jump
        ij: all glitches

        Supported values: glitchless, noij, ij
        Default value: glitchless
    """

    display_name = "Logic"
    option_glitchless = 0x00
    option_noij = 0x01
    option_ij = 0x02


class CoinOption(Choice):
    """Choose if Specter Coins should act as Locations

        true: coins are added as locations
        false: coins are not added as locations

        Supported values: true, false
        Default value: false
    """

    display_name = "Coin"
    option_true = 0x00
    option_false = 0x01


@dataclass
class ApeEscapeOptions(PerGameCommonOptions):
    debug: DebugOption
    goal: GoalOption
    logic: LogicOption
    coin: CoinOption