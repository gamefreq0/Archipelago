from enum import Enum


class RAM:
    """A handy collection of memory values and addresses for Spyro"""
    unusedSpace: int = 0x0f000  # At least, it seems unused. Test...
    lastReceivedArchipelagoID: int = unusedSpace + 0x4
    """The ID of the last item the game has been given. Useful for save state issues and such."""
    curLevelID: int = 0x7596c
    destLevelID: int = 0x758b4
    curGameState: int = 0x757d8
    balloonistMenuChoice: int = 0x777f0
    unlockedWorlds: int = 0x758d0
    startingLevelID: int = 0x2d4f0
    """Which level you start in after the intro cutscene."""
    gnastyAnimFlag: int = 0x160f08
    GNASTY_DEFEATED: int = 0x08

    class WorldTextOffsets(Enum):
        """RAM offsets for world names"""
        ARTISANS = 0x1006c
        KEEPERS = 0x1005c
        CRAFTERS = 0x1004c
        MAKERS = 0x1003c
        WEAVERS = 0x1002c
        GNASTY = 0x1001c

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
        GNASTYS_WORLD = 60
        GNASTY_GNORC = 63
