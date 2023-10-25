from __future__ import annotations

from Options import Choice, DefaultOnToggle, Option, OptionSet, Range, Toggle, FreeText, PerGameCommonOptions

from typing import Dict

class Goal(Choice):
    """
    Determines what your goal is to consider the game beaten

    Champion: Become the champion and enter the hall of fame
    Steven: Defeat Steven in Meteor Falls
    Norman: Defeat Norman in Petalburg Gym
    """
    display_name = "Goal"
    default = 0
    option_champion = 0
    option_steven = 1
    option_norman = 2