from enum import Enum


class RAM:
    """A handy collection of memory values and addresses for Spyro"""
    unusedSpace: int = 0x0f000  # At least, it seems unused. Test...
    lastReceivedArchipelagoID: int = unusedSpace + 4
    """The ID of the last item the game has been given. Useful for save state issues and such."""
    fakeTimer: int = unusedSpace + 8
    lastSelectedValidChoice: int = unusedSpace + 12
    balloonPointers: dict[str, list[int]] = {
        "Artisans": [0x7bc04, 0x7bc08],
        "Peace Keepers": [0x7c5dc, 0x7c5e0],
        "Magic Crafters": [0x7c5d4, 0x7c5d8],
        "Beast Makers": [0x7c3c8, 0x7c3cc],
        "Dream Weavers": [0x7c5fc, 0x7c600],
        "Gnasty's World": [0x7bb74, 0x7bb78]
    }
    curLevelID: int = 0x7596c
    destLevelID: int = 0x758b4
    curGameState: int = 0x757d8
    balloonistMenuChoice: int = 0x777f0
    unlockedWorlds: int = 0x758d0
    startingLevelID: int = 0x2d4f0
    """Which level you start in after the intro cutscene."""
    gnastyAnimFlag: int = 0x160f08
    GNASTY_DEFEATED: int = 0x08
    worldTextOffsets: dict[str, int] = {
        "Artisans": 0x1006c,
        "Peace Keepers": 0x1005c,
        "Magic Crafters": 0x1004c,
        "Beast Makers": 0x1003c,
        "Dream Weavers": 0x1002c,
        "Gnasty's World": 0x1001c
    }

    nestorUnskippable: int = 0x1747f4
    spyroCurAnimation: int = 0x78ad0
    spyroColorFilter: int = 0x78a80

    class SpyroStates(Enum):
        """Animation states for Spyro"""
        STANDING = 0x00
        FLOP = 0x06
        ROLL = 0x13
        DEATH_SPIN = 0x1e

    class GameStates(Enum):
        """States the Spyro game engine can be in"""
        GAMEPLAY = 0x00
        LOADING = 0x01
        PAUSED = 0x02
        INVENTORY = 0x03
        DEATH = 0x04
        GAME_OVER = 0x05
        FLIGHT_MENU = 0x07
        DRAGON_CUTSCENE = 0x08
        FLY_IN = 0x09
        EXITING_LEVEL = 0x0a
        FAIRY_TEXTBOX = 0x0b
        BALLOONIST = 0x0c
        TITLE_SCREEN = 0x0d
        CUTSCENE = 0x0e
        CREDITS = 0x0f

    class LevelIDs(Enum):
        """The internal IDs of the levels in Spyro"""
        ARTISANS = 10
        STONE_HILL = 11
        PEACE_KEEPERS = 20
        MAGIC_CRAFTERS = 30
        BEAST_MAKERS = 40
        DREAM_WEAVERS = 50
        GNASTYS_WORLD = 60
        GNASTY_GNORC = 63


    hub_names: dict[int, str] = {
        0: "Artisans",
        1: "Peace Keepers",
        2: "Magic Crafters",
        3: "Beast Makers",
        4: "Dream Weavers",
        5: "Gnasty's World"
    }
    artisans_head_checks: list[int] = [
        0x7f48c,
        0x7f4c8
    ]
    gnasty_head_checks: list[int] = [
        0x817fc,
        0x81810,
        0x81848,
        0x81884,
        0x8189c,
        0x818b4
    ]


def menu_lookup(current_world_num: int, menu_choice: int) -> int:
    if menu_choice > current_world_num:
        return menu_choice
    return menu_choice - 1
