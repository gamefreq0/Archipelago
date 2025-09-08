from BaseClasses import CollectionState
from ..AutoWorld import World
from .addresses import RAM, Environment


def set_rules(world: World, gem_threshold_mult: float, envs: list[Environment]):
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player, 1)
    for gem_threshold_count in range(500, int(RAM.TOTAL_TREASURE * gem_threshold_mult) + 1, 500):
        gem_threshold_location = world.get_location(f"{gem_threshold_count} Gems")
        gem_threshold_location.access_rule = (
            lambda
            state,
            world=world,
            min_gems=gem_threshold_count,
            scale=gem_threshold_mult,
            envs=envs:
            can_reach_gems_minimum(world, state, min_gems, scale, envs)
        )


def can_reach_gems_minimum(
    world: World,
    state: CollectionState,
    min_gems: int,
    scale: float,
    envs: list[Environment],
) -> bool:
    """Returns whether the player can access enough gems to clear a given threshold

    Args:
        world: The current SpyroWorld
        state: The current CollectionState
        min_gems: The gem threshold to check against
        scale: Scaling to apply to reachable gems
        envs: Environments to check against (might be less than the full list with excluded levels/hubs)

    Returns:
        bool
    """
    return total_reachable_gems(world, state, scale, envs) >= min_gems


def total_reachable_gems(world: World, state: CollectionState, scale: float, envs: list[Environment]) -> int:
    """Returns the total value of gems that can be reached for a given CollectionState

    Args:
        world: The current SpyroWorld
        state: The current CollectionState
        scale: Scaling factor applied to reachable gems
        envs: list[Environment]

    Returns:
        Total value of gems
    """
    total_gems: int = 0

    for env in envs:
        if state.can_reach_region(env.name, world.player):
            total_gems += int(env.total_gems * scale)

    return total_gems
