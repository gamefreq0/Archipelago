from .locations import total_treasure

try:
    from typing import TYPE_CHECKING
except ImportError:
    from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from .world import SpyroWorld


def set_rules(world: "SpyroWorld"):
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player, 1)
    for gem_threshold_count in range(500, total_treasure + 1, 500):
        gem_threshold_location = world.get_location(f"{gem_threshold_count} Gems")
        gem_threshold_location.access_rule = lambda state, gem_count=gem_threshold_count: state.has(
            "100 Gems", world.player, int(gem_count / 100)
        )
