from enum import Enum


class RAM:
    """A handy collection of memory values and addresses for Spyro"""

    unused_space: int = 0x0f000  # At least, it seems unused. Test...

    last_received_archipelago_id: int = unused_space + 4
    """The ID of the last item the game has been given. Useful for save state issues and such."""

    fake_timer: int = unused_space + 8

    last_selected_valid_choice: int = unused_space + 12

    class Environment():
        """A container holding various useful pieces of data tied to a given level or homeworld"""
        balloon_pointers: list[int]
        name: str
        internal_id: int
        text_offset: int
        has_vortex: bool
        dragons: dict[str, tuple[int, int]]  # dragons[name] = (address, flag)
        # TODO: eggs
        gem_counter: int
        statue_head_checks: list[int]
        child_environments: list["RAM.Environment"]

        def __init__(
            self, name: str, internal_id: int, has_vortex: bool = False
        ) -> None:
            self.name = name
            self.internal_id = internal_id
            self.balloon_pointers = []
            self.text_offset = 0
            self.has_vortex = has_vortex
            self.dragons = {}
            self.gem_counter = 0
            self.statue_head_checks = []
            self.child_environments = []

        def is_hub(self) -> bool:
            """Whether the current environment is a homeworld"""
            is_hub = False
            if self.internal_id % 10 == 0:
                is_hub = True
            return is_hub

    hub_environments: list[Environment] = []
    hub_environments.append(Environment("Artisans", 10))
    hub_environments.append(Environment("Peace Keepers", 20))
    hub_environments.append(Environment("Magic Crafters", 30))
    hub_environments.append(Environment("Beast Makers", 40))
    hub_environments.append(Environment("Dream Weavers", 50))
    hub_environments.append(Environment("Gnasty's World", 60))

    hub_environments[0].balloon_pointers = [0x7bc04, 0x7bc08]
    hub_environments[1].balloon_pointers = [0x7c5dc, 0x7c5e0]
    hub_environments[2].balloon_pointers = [0x7c5d4, 0x7c5d8]
    hub_environments[3].balloon_pointers = [0x7c3c8, 0x7c3cc]
    hub_environments[4].balloon_pointers = [0x7c5fc, 0x7c600]
    hub_environments[5].balloon_pointers = [0x7bb74, 0x7bb78]

    hub_environments[0].text_offset = 0x1006c
    hub_environments[1].text_offset = 0x1005c
    hub_environments[2].text_offset = 0x1004c
    hub_environments[3].text_offset = 0x1003c
    hub_environments[4].text_offset = 0x1002c
    hub_environments[5].text_offset = 0x1001c

    hub_environments[0].statue_head_checks = [
        0x7f48c,
        0x7f4c8
    ]
    hub_environments[5].statue_head_checks = [
        0x817fc,
        0x81810,
        0x81848,
        0x81884,
        0x8189c,
        0x818b4
    ]

    cur_level_id: int = 0x7596c
    dest_level_id: int = 0x758b4
    cur_game_state: int = 0x757d8
    balloonist_menu_choice: int = 0x777f0
    unlocked_worlds: int = 0x758d0
    starting_level_id: int = 0x2d4f0
    """Which level you start in after the intro cutscene."""
    gnasty_anim_flag: int = 0x160f08
    GNASTY_DEFEATED: int = 0x08

    nestor_unskippable: int = 0x1747f4
    spyro_cur_animation: int = 0x78ad0
    spyro_color_filter: int = 0x78a80

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


def menu_lookup(current_world_num: int, menu_choice: int) -> int:
    if menu_choice > current_world_num:
        return menu_choice
    return menu_choice - 1
