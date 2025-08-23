from typing_extensions import final

from BaseClasses import Tutorial
from ..AutoWorld import WebWorld


@final
class SpyroWeb(WebWorld):
    theme = "grass"

    setup_en = Tutorial(
        "Spyro the Dragon Multiworld Setup Guide",
        "A guide to setting up Spyro the Dragon in Archipelago",
        "English",
        "guide_en.md",
        "setup/en",
        ["gamefreq0"]
    )

    tutorials = [setup_en]
