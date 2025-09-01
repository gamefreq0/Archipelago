from enum import IntEnum

from typing import TYPE_CHECKING
try:
    from typing import final
except ImportError:
    if TYPE_CHECKING:
        from typing import final
    else:
        from typing_extensions import final


def internal_id_to_offset(internal_id: int) -> int:
    """Translates internal ID to zero-indexed offset in the overall environment"""
    homeworld_index = int(internal_id / 10) - 1
    homeworld_offset = internal_id % 10
    return (homeworld_index * 6) + homeworld_offset


class Environment():
    """A container holding various useful pieces of data tied to a given level or homeworld"""
    balloon_pointers: list[int]
    name: str
    internal_id: int
    text_offset: int
    has_vortex: bool
    dragons: dict[str, tuple[int, int]]  # dragons[name] = (address, flag)
    eggs: dict[str, tuple[int, int]]  # eggs[name] = (address, flag)
    gem_counter: int
    total_gems: int
    statue_head_checks: list[int]
    child_environments: list["Environment"]
    portal_surface_types: list[int]
    portal_dest_level_ids: list[int]
    VORTEX_BASE_POINTER: int = 0x7a6a8
    vortex_pointer: int
    vortex_moby_pointer: int

    def __init__(self, name: str, internal_id: int, has_vortex: bool = False) -> None:
        self.name = name
        self.internal_id = internal_id
        self.balloon_pointers = []
        self.text_offset = 0
        self.has_vortex = has_vortex
        self.dragons = {}
        self.eggs = {}
        self.gem_counter = 0
        self.total_gems = 0
        self.statue_head_checks = []
        self.child_environments = []
        self.portal_surface_types = []
        self.portal_dest_level_ids = []
        self.vortex_pointer = self.VORTEX_BASE_POINTER + internal_id_to_offset(self.internal_id)
        self.vortex_moby_pointer = 0

    def is_hub(self) -> bool:
        """Whether the current environment is a homeworld"""
        is_hub = False
        if self.internal_id % 10 == 0:
            is_hub = True
        return is_hub


@final
class RAM:
    """A handy collection of memory values and addresses for Spyro"""

    unused_space: int = 0x0f000  # At least, it seems unused. Test...

    last_received_archipelago_id: int = unused_space + 4
    """The ID of the last item the game has been given. Useful for save state issues and such."""

    switched_portal_dest: int = unused_space + 8

    fake_timer: int = unused_space + 12

    last_selected_valid_choice: int = unused_space + 16

    hub_environments: list[Environment] = []

    hub_environments.append(Environment("Artisans", 10))
    hub_environments.append(Environment("Peace Keepers", 20))
    hub_environments.append(Environment("Magic Crafters", 30))
    hub_environments.append(Environment("Beast Makers", 40))
    hub_environments.append(Environment("Dream Weavers", 50))
    hub_environments.append(Environment("Gnasty's World", 60))

    hub_environments[0].child_environments.append(Environment("Stone Hill", 11, True))
    hub_environments[0].child_environments.append(Environment("Dark Hollow", 12, True))
    hub_environments[0].child_environments.append(Environment("Town Square", 13, True))
    hub_environments[0].child_environments.append(Environment("Toasty", 14, True))
    hub_environments[0].child_environments.append(Environment("Sunny Flight", 15))

    hub_environments[1].child_environments.append(Environment("Dry Canyon", 21, True))
    hub_environments[1].child_environments.append(Environment("Cliff Town", 22, True))
    hub_environments[1].child_environments.append(Environment("Ice Cavern", 23, True))
    hub_environments[1].child_environments.append(Environment("Doctor Shemp", 24, True))
    hub_environments[1].child_environments.append(Environment("Night Flight", 25))

    hub_environments[2].child_environments.append(Environment("Alpine Ridge", 31, True))
    hub_environments[2].child_environments.append(Environment("High Caves", 32, True))
    hub_environments[2].child_environments.append(Environment("Wizard Peak", 33, True))
    hub_environments[2].child_environments.append(Environment("Blowhard", 34, True))
    hub_environments[2].child_environments.append(Environment("Crystal Flight", 35))

    hub_environments[3].child_environments.append(Environment("Terrace Village", 41, True))
    hub_environments[3].child_environments.append(Environment("Misty Bog", 42, True))
    hub_environments[3].child_environments.append(Environment("Tree Tops", 43, True))
    hub_environments[3].child_environments.append(Environment("Metalhead", 44, True))
    hub_environments[3].child_environments.append(Environment("Wild Flight", 45))

    hub_environments[4].child_environments.append(Environment("Dark Passage", 51, True))
    hub_environments[4].child_environments.append(Environment("Lofty Castle", 52, True))
    hub_environments[4].child_environments.append(Environment("Haunted Towers", 53, True))
    hub_environments[4].child_environments.append(Environment("Jacques", 54, True))
    hub_environments[4].child_environments.append(Environment("Icy Flight", 55))

    hub_environments[5].child_environments.append(Environment("Gnorc Cove", 61, True))
    hub_environments[5].child_environments.append(Environment("Twilight Harbor", 62, True))
    hub_environments[5].child_environments.append(Environment("Gnasty Gnorc", 63))
    hub_environments[5].child_environments.append(Environment("Gnasty's Loot", 64, True))

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

    hub_environments[0].portal_dest_level_ids.append(0xc12b4)  # Stone Hill
    hub_environments[0].portal_dest_level_ids.append(0xc12a8)  # Dark Hollow
    hub_environments[0].portal_dest_level_ids.append(0xc12c0)  # Town Square
    hub_environments[0].portal_dest_level_ids.append(0xc129c)  # Toasty
    hub_environments[0].portal_dest_level_ids.append(0xc12cc)  # Sunny Flight

    hub_environments[1].portal_dest_level_ids.append(0xbfc48)  # Dry Canyon
    hub_environments[1].portal_dest_level_ids.append(0xbfc54)  # Cliff Town
    hub_environments[1].portal_dest_level_ids.append(0xbfc60)  # Ice Cavern
    hub_environments[1].portal_dest_level_ids.append(0xbfc6c)  # Doctor Shemp
    hub_environments[1].portal_dest_level_ids.append(0xbfc78)  # Night Flight

    hub_environments[2].portal_dest_level_ids.append(0xc627c)  # Alpine Ridge
    hub_environments[2].portal_dest_level_ids.append(0xc6294)  # High Caves
    hub_environments[2].portal_dest_level_ids.append(0xc6288)  # Wizard Peak
    hub_environments[2].portal_dest_level_ids.append(0xc6264)  # Blowhard
    hub_environments[2].portal_dest_level_ids.append(0xc6270)  # Crystal Flight

    hub_environments[3].portal_dest_level_ids.append(0xb558c)  # Terrace Village
    hub_environments[3].portal_dest_level_ids.append(0xb5574)  # Misty Bog
    hub_environments[3].portal_dest_level_ids.append(0xb5580)  # Tree Tops
    hub_environments[3].portal_dest_level_ids.append(0xb5568)  # Metalhead
    hub_environments[3].portal_dest_level_ids.append(0xb5598)  # Wild Flight

    hub_environments[4].portal_dest_level_ids.append(0xc5ecc)  # Dark Passage
    hub_environments[4].portal_dest_level_ids.append(0xc5ee4)  # Lofty Castle
    hub_environments[4].portal_dest_level_ids.append(0xc5efc)  # Haunted Towers
    hub_environments[4].portal_dest_level_ids.append(0xc5ed8)  # Jacques
    hub_environments[4].portal_dest_level_ids.append(0xc5ef0)  # Icy Flight

    hub_environments[5].portal_dest_level_ids.append(0xa69d8)  # Gnorc Cove
    hub_environments[5].portal_dest_level_ids.append(0xa69b4)  # Twilight Harbor
    hub_environments[5].portal_dest_level_ids.append(0xa69c0)  # Gnasty Gnorc
    hub_environments[5].portal_dest_level_ids.append(0xa69cc)  # Gnasty's Loot

    hub_environments[0].child_environments[0].text_offset = 0x101fc  # stone hill
    hub_environments[0].child_environments[1].text_offset = 0x101f0  # dark hollow
    hub_environments[0].child_environments[2].text_offset = 0x101e4  # town square
    hub_environments[0].child_environments[3].text_offset = 0x75570  # toasty
    hub_environments[0].child_environments[4].text_offset = 0x101d4  # sunny flight

    hub_environments[1].child_environments[0].text_offset = 0x101c8  # dry canyon
    hub_environments[1].child_environments[1].text_offset = 0x101bc  # cliff town
    hub_environments[1].child_environments[2].text_offset = 0x101b0  # ice cavern
    hub_environments[1].child_environments[3].text_offset = 0x101a0  # doctor shemp
    hub_environments[1].child_environments[4].text_offset = 0x10190  # night flight

    hub_environments[2].child_environments[0].text_offset = 0x10180  # alpine ridge
    hub_environments[2].child_environments[1].text_offset = 0x10174  # high caves
    hub_environments[2].child_environments[2].text_offset = 0x10168  # wizard peak
    hub_environments[2].child_environments[3].text_offset = 0x1015c  # blowhard
    hub_environments[2].child_environments[4].text_offset = 0x1014c  # crystal flight

    hub_environments[3].child_environments[0].text_offset = 0x1013c  # terrace village
    hub_environments[3].child_environments[1].text_offset = 0x10130  # misty bog
    hub_environments[3].child_environments[2].text_offset = 0x10124  # tree tops
    hub_environments[3].child_environments[3].text_offset = 0x10118  # metalhead
    hub_environments[3].child_environments[4].text_offset = 0x1010c  # wild flight

    hub_environments[4].child_environments[0].text_offset = 0x100fc  # dark passage
    hub_environments[4].child_environments[1].text_offset = 0x100ec  # lofty castle
    hub_environments[4].child_environments[2].text_offset = 0x100dc  # haunted towers
    hub_environments[4].child_environments[3].text_offset = 0x75568  # jacques
    hub_environments[4].child_environments[4].text_offset = 0x100d0  # icy flight

    hub_environments[5].child_environments[0].text_offset = 0x100b4  # gnorc cove
    hub_environments[5].child_environments[1].text_offset = 0x100a4  # twilight harbor
    hub_environments[5].child_environments[2].text_offset = 0x10094  # gnasty gnorc
    hub_environments[5].child_environments[3].text_offset = 0x10084  # gnasty's loot

    hub: Environment = hub_environments[0]
    for hub in hub_environments:
        dest_offset: int = 0
        for dest_offset in hub.portal_dest_level_ids:
            hub.portal_surface_types.append(dest_offset - 4)

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

    hub_environments[0].total_gems = 100
    hub_environments[0].child_environments[0].total_gems = 200
    hub_environments[0].child_environments[1].total_gems = 100
    hub_environments[0].child_environments[2].total_gems = 200
    hub_environments[0].child_environments[3].total_gems = 100
    hub_environments[0].child_environments[4].total_gems = 300
    hub_environments[1].total_gems = 200
    hub_environments[1].child_environments[0].total_gems = 400
    hub_environments[1].child_environments[1].total_gems = 400
    hub_environments[1].child_environments[2].total_gems = 400
    hub_environments[1].child_environments[3].total_gems = 300
    hub_environments[1].child_environments[4].total_gems = 300
    hub_environments[2].total_gems = 300
    hub_environments[2].child_environments[0].total_gems = 500
    hub_environments[2].child_environments[1].total_gems = 500
    hub_environments[2].child_environments[2].total_gems = 500
    hub_environments[2].child_environments[3].total_gems = 400
    hub_environments[2].child_environments[4].total_gems = 300
    hub_environments[3].total_gems = 300
    hub_environments[3].child_environments[0].total_gems = 400
    hub_environments[3].child_environments[1].total_gems = 500
    hub_environments[3].child_environments[2].total_gems = 500
    hub_environments[3].child_environments[3].total_gems = 500
    hub_environments[3].child_environments[4].total_gems = 300
    hub_environments[4].total_gems = 300
    hub_environments[4].child_environments[0].total_gems = 500
    hub_environments[4].child_environments[1].total_gems = 400
    hub_environments[4].child_environments[2].total_gems = 500
    hub_environments[4].child_environments[3].total_gems = 500
    hub_environments[4].child_environments[4].total_gems = 300
    hub_environments[5].total_gems = 200
    hub_environments[5].child_environments[0].total_gems = 400
    hub_environments[5].child_environments[1].total_gems = 400
    hub_environments[5].child_environments[2].total_gems = 500
    hub_environments[5].child_environments[3].total_gems = 2000

    hub_environments[0].gem_counter = 0x77420
    hub_environments[0].child_environments[0].gem_counter = 0x77424
    hub_environments[0].child_environments[1].gem_counter = 0x77428
    hub_environments[0].child_environments[2].gem_counter = 0x7742c
    hub_environments[0].child_environments[3].gem_counter = 0x77430
    hub_environments[0].child_environments[4].gem_counter = 0x77434
    hub_environments[1].gem_counter = 0x77438
    hub_environments[1].child_environments[0].gem_counter = 0x7743c
    hub_environments[1].child_environments[1].gem_counter = 0x77440
    hub_environments[1].child_environments[2].gem_counter = 0x77444
    hub_environments[1].child_environments[3].gem_counter = 0x77448
    hub_environments[1].child_environments[4].gem_counter = 0x7744c
    hub_environments[2].gem_counter = 0x77450
    hub_environments[2].child_environments[0].gem_counter = 0x77454
    hub_environments[2].child_environments[1].gem_counter = 0x77458
    hub_environments[2].child_environments[2].gem_counter = 0x7745c
    hub_environments[2].child_environments[3].gem_counter = 0x77460
    hub_environments[2].child_environments[4].gem_counter = 0x77464
    hub_environments[3].gem_counter = 0x77468
    hub_environments[3].child_environments[0].gem_counter = 0x7746c
    hub_environments[3].child_environments[1].gem_counter = 0x77470
    hub_environments[3].child_environments[2].gem_counter = 0x77474
    hub_environments[3].child_environments[3].gem_counter = 0x77478
    hub_environments[3].child_environments[4].gem_counter = 0x7747c
    hub_environments[4].gem_counter = 0x77480
    hub_environments[4].child_environments[0].gem_counter = 0x77484
    hub_environments[4].child_environments[1].gem_counter = 0x77488
    hub_environments[4].child_environments[2].gem_counter = 0x7748c
    hub_environments[4].child_environments[3].gem_counter = 0x77490
    hub_environments[4].child_environments[4].gem_counter = 0x77494
    hub_environments[5].gem_counter = 0x77498
    hub_environments[5].child_environments[0].gem_counter = 0x7749c
    hub_environments[5].child_environments[1].gem_counter = 0x774a0
    hub_environments[5].child_environments[2].gem_counter = 0x774a4
    hub_environments[5].child_environments[3].gem_counter = 0x774a8

    hub_environments[0].child_environments[0].vortex_moby_pointer = 0x177330
    hub_environments[0].child_environments[1].vortex_moby_pointer = 0x1339ac
    hub_environments[0].child_environments[2].vortex_moby_pointer = 0x17d644
    hub_environments[0].child_environments[3].vortex_moby_pointer = 0x1738ac

    hub_environments[1].child_environments[0].vortex_moby_pointer = 0x169444
    hub_environments[1].child_environments[1].vortex_moby_pointer = 0x16f978
    hub_environments[1].child_environments[2].vortex_moby_pointer = 0x16b454
    hub_environments[1].child_environments[3].vortex_moby_pointer = 0x16ba44

    hub_environments[2].child_environments[0].vortex_moby_pointer = 0x17bbec
    hub_environments[2].child_environments[1].vortex_moby_pointer = 0x17e188
    hub_environments[2].child_environments[2].vortex_moby_pointer = 0x179ce4
    hub_environments[2].child_environments[3].vortex_moby_pointer = 0x1396e4

    hub_environments[3].child_environments[0].vortex_moby_pointer = 0x179020
    hub_environments[3].child_environments[1].vortex_moby_pointer = 0x17b68c
    hub_environments[3].child_environments[2].vortex_moby_pointer = 0x17ce24
    hub_environments[3].child_environments[3].vortex_moby_pointer = 0x173fc4

    hub_environments[4].child_environments[0].vortex_moby_pointer = 0x178950
    hub_environments[4].child_environments[1].vortex_moby_pointer = 0x15a3d8
    hub_environments[4].child_environments[2].vortex_moby_pointer = 0x176964
    hub_environments[4].child_environments[3].vortex_moby_pointer = 0x16deb0

    hub_environments[5].child_environments[0].vortex_moby_pointer = 0x174884
    hub_environments[5].child_environments[1].vortex_moby_pointer = 0x17c298
    # Gnasty Gnorc has no vortex, skip
    hub_environments[5].child_environments[3].vortex_moby_pointer = 0x14da14

    cur_level_id: int = 0x7596c
    dest_level_id: int = 0x758b4
    cur_game_state: int = 0x757d8
    total_gem_count: int = 0x75860
    balloonist_menu_choice: int = 0x777f0
    unlocked_worlds: int = 0x758d0

    last_touched_whirlwind: int = 0x78c7c
    """Holds a pointer to the moby object for the last touched whirlwind."""

    starting_level_id: int = 0x2d4f0
    """Which level you start in after the intro cutscene."""

    gnasty_anim_flag: int = 0x160f08
    GNASTY_DEFEATED: int = 0x08

    nestor_unskippable: int = 0x1747f4
    tuco_egg_minimum: int = 0x8492c
    spyro_cur_animation: int = 0x78ad0
    spyro_color_filter: int = 0x78a80

    class SpyroStates(IntEnum):
        """Animation states for Spyro"""
        STANDING = 0x00
        FLOP = 0x06
        WHIRLWIND = 0x11
        ROLL = 0x13
        DEATH_SPIN = 0x1e

    class GameStates(IntEnum):
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


def menu_lookup(current_world_num: int, menu_choice: int) -> int:
    """Replicates the same math the game uses for mapping a menu choice to the homeworld destination

    Args:
        current_world_num: The index of the current homeworld
        menu_choice: The current position of the menu cursor

    Returns:
        The index of the selected homeworld, or -1 if Stay Here is selected
    """
    if menu_choice > current_world_num:
        return menu_choice
    return menu_choice - 1
