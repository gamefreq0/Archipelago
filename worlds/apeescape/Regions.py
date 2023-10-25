from BaseClasses import MultiWorld, Region, Entrance
from .Locations import location_table, ApeEscapeLocation

def create_regions(world: MultiWorld, player: int):

    menu = Region("Menu", player, world)

    l11 = Region("1-1", player, world)

    # initializing range
    i, j = 128000001, 128000004

    # using loop to iterate through all keys
    res = dict()
    for key, val in location_table.items():
        if int(val) >= i and int(val) <= j:
            res[key] = val

    l11.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l11) for loc_name in res]

    l12 = Region("1-2", player, world)

    # initializing range
    i, j = 128000005, 128000010

    # using loop to iterate through all keys
    res = dict()
    for key, val in location_table.items():
        if int(val) >= i and int(val) <= j:
            res[key] = val

    l12.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l12) for loc_name in res]

    l13 = Region("1-3", player, world)

    # initializing range
    i, j = 128000011, 128000017

    # using loop to iterate through all keys
    res = dict()
    for key, val in location_table.items():
        if int(val) >= i and int(val) <= j:
            res[key] = val

    l13.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l13) for loc_name in res]

    l91 = Region("9-1", player, world)

    # initializing range
    i, j = 128000181, 128000205

    # using loop to iterate through all keys
    res = dict()
    for key, val in location_table.items():
        if int(val) >= i and int(val) <= j:
            res[key] = val
    l91.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l91) for loc_name in res]

    world.initialize_regions([menu,l11, l12, l91])
    world.regions.extend([menu,l11,l12,l13,l91])



def connect_regions(world: MultiWorld, player: int, source: str, target: str, rule=None):
    sourceRegion = world.get_region(source, player)
    targetRegion = world.get_region(target, player)

    connection = Entrance(player, '', sourceRegion)
    if rule:
        connection.access_rule = rule

    sourceRegion.exits.append(connection)
    connection.connect(targetRegion)