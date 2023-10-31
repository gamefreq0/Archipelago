from BaseClasses import MultiWorld, Region, Entrance
from .Locations import location_table, ApeEscapeLocation

def create_regions(world: MultiWorld, player: int):

    #menu
    menu = Region("Menu", player, world)

    #worlds
    w1 = Region("w1", player, world)
    w2 = Region("w2", player, world)
    w3 = Region("w3", player, world)
    w4 = Region("w4", player, world)
    w5 = Region("w5", player, world)
    w6 = Region("w6", player, world)
    w7 = Region("w7", player, world)
    w8 = Region("w8", player, world)
    w9 = Region("w9", player, world)

    #levels
    l11 = Region("1-1", player, world)
    l11.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l11) for loc_name
                      in get_range(1,3)]

    l111 = Region("1-1 Ledge", player, world)
    l111.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l111) for loc_name
                      in get_range(4, 4)]

    l12 = Region("1-2", player, world)
    l12.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l12) for loc_name
                      in get_range(5,10)]

    l13 = Region("1-3", player, world)
    l13.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l13) for loc_name
                      in get_range(11,15)]
    l13.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l13) for loc_name
                      in get_range(17, 17)]

    l131 = Region("1-3 Tri", player, world)
    l131.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l131) for loc_name
                      in get_range(16, 16)]

    l21 = Region("2-1", player, world)
    l21.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l21) for loc_name
                      in get_range(18, 31)]

    l22 = Region("2-2", player, world)
    l22.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l22) for loc_name
                      in get_range(32, 44)]

    l23 = Region("2-3", player, world)
    l23.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l23) for loc_name
                      in get_range(45, 52)]

    l41 = Region("4-1", player, world)
    l41.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l41) for loc_name
                      in get_range(53, 60)]

    l42 = Region("4-2", player, world)
    l42.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l42) for loc_name
                      in get_range(61, 68)]

    l43 = Region("4-3", player, world)
    l43.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l43) for loc_name
                      in get_range(69, 79)]

    l51 = Region("5-1", player, world)
    l51.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l51) for loc_name
                      in get_range(80, 85)]

    l52 = Region("5-2", player, world)
    l52.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l52) for loc_name
                      in get_range(86, 94)]

    l53 = Region("5-3", player, world)
    l53.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l53) for loc_name
                      in get_range(95, 103)]

    l71 = Region("7-1", player, world)
    l71.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l71) for loc_name
                      in get_range(104, 115)]

    l72 = Region("7-2", player, world)
    l72.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l72) for loc_name
                      in get_range(116, 125)]

    l73 = Region("7-3", player, world)
    l73.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l73) for loc_name
                      in get_range(126, 145)]

    l81 = Region("8-1", player, world)
    l81.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l81) for loc_name
                      in get_range(146, 158)]

    l82 = Region("8-2", player, world)
    l82.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l82) for loc_name
                      in get_range(159, 168)]

    l83 = Region("8-3", player, world)
    l83.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l83) for loc_name
                      in get_range(169, 180)]

    l91 = Region("9-1", player, world)
    l91.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l91) for loc_name
                      in get_range(181,205)]

    world.initialize_regions([menu,
                              w1,w2,w3,w4,w5,w6,w7,w8,w9,
                              l11, l12, l13, l21, l22, l23, l41, l42, l43,
                              l51, l52, l53, l71, l72, l73, l81, l82, l83, l91,
                              l111])

    world.regions.extend([menu,
                          w1, w2, w3, w4, w5, w6, w7, w8, w9,
                          l11, l12, l13, l21, l22, l23, l41, l42, l43,
                          l51, l52, l53, l71, l72, l73, l81, l82, l83, l91,
                          l111])



def connect_regions(world: MultiWorld, player: int, source: str, target: str, rule=None):
    sourceRegion = world.get_region(source, player)
    targetRegion = world.get_region(target, player)

    connection = Entrance(player, '', sourceRegion)
    if rule:
        connection.access_rule = rule

    sourceRegion.exits.append(connection)
    connection.connect(targetRegion)

def get_range(i, j):
    i = i + 128000000
    j = j + 128000000
    res = dict()
    for key, val in location_table.items():
        if int(val) >= i and int(val) <= j:
            res[key] = val
    return res