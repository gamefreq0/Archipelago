from BaseClasses import CollectionState
from ..AutoWorld import World
from .locations import total_treasure
from .addresses import RAM


def set_rules(world: World):
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player, 1)
    for gem_threshold_count in range(500, total_treasure + 1, 500):
        gem_threshold_location = world.get_location(f"{gem_threshold_count} Gems")
        gem_threshold_location.access_rule = (
            lambda state, world=world, min_gems=gem_threshold_count: can_reach_gems_minimum(world, state, min_gems)
        )


def can_reach_gems_minimum(world: World, state: CollectionState, min_gems: int) -> bool:
    """Returns whether the player can access enough gems to clear a given threshold

    Args:
        world: The current SpyroWorld
        state: The current CollectionState
        min_gems: The gem threshold to check against

    Returns:
        bool
    """
    return total_reachable_gems(world, state) >= min_gems


def total_reachable_gems(world: World, state: CollectionState) -> int:
    """Returns the total value of gems that can be reached for a given CollectionState

    Args:
        world: The current SpyroWorld
        state: The current CollectionState

    Returns:
        Total value of gems
    """
    total_gems = 0

    for hub in RAM.hub_environments:
        # This will represent moveless areas, eventually
        if state.can_reach_region(hub.name, world.player):
            total_gems += hub.total_gems

        for level in hub.child_environments:
            # This will represent moveless areas, eventually
            if state.can_reach_region(level.name, world.player):
                total_gems += level.total_gems

    return total_gems
