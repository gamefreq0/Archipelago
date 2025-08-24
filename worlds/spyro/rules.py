from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from .world import SpyroWorld


def set_rules(world: "SpyroWorld"):
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player, 1)
