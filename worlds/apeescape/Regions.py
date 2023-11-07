from BaseClasses import MultiWorld, Region, Entrance
from .Locations import location_table, ApeEscapeLocation
from .Strings import AEWorld, AERoom

def create_regions(world: MultiWorld, player: int):

    #menu
    menu = Region("Menu", player, world)

    #worlds
    w1 = Region(AEWorld.W1.value, player, world)
    w2 = Region(AEWorld.W2.value, player, world)
    w3 = Region(AEWorld.W3.value, player, world)
    w4 = Region(AEWorld.W4.value, player, world)
    w5 = Region(AEWorld.W5.value, player, world)
    w6 = Region(AEWorld.W6.value, player, world)
    w7 = Region(AEWorld.W7.value, player, world)
    w8 = Region(AEWorld.W8.value, player, world)
    w9 = Region(AEWorld.W9.value, player, world)

    #1-1
    l11 = Region(AERoom.W1L1Main.value, player, world)
    noonan = Region(AERoom.W1L1Noonan.value, player, world)
    noonan.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], noonan) for loc_name
                       in get_array([1])]
    jorjy = Region(AERoom.W1L1Jorjy.value, player, world)
    jorjy.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], jorjy) for loc_name
                         in get_array([2])]
    nati = Region(AERoom.W1L1Nati.value, player, world)
    nati.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], nati) for loc_name
                         in get_array([3])]
    trayc = Region(AERoom.W1L1TrayC.value, player, world)
    trayc.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], trayc) for loc_name
                         in get_array([4])]


    #1-2
    l12 = Region(AERoom.W1L2Main.value, player, world)
    shay = Region(AERoom.W1L2Shay.value, player, world)
    shay.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], shay) for loc_name
                         in get_array([5])]
    drmonk = Region(AERoom.W1L2DrMonk.value, player, world)
    drmonk.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], drmonk) for loc_name
                         in get_array([6])]
    grunt = Region(AERoom.W1L2Grunt.value, player, world)
    grunt.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], grunt) for loc_name
                         in get_array([7])]
    ahchoo = Region(AERoom.W1L2Ahchoo.value, player, world)
    ahchoo.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], ahchoo) for loc_name
                         in get_array([8])]
    gornif = Region(AERoom.W1L2Gornif.value, player, world)
    gornif.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], gornif) for loc_name
                         in get_array([9])]
    tyrone = Region(AERoom.W1L2Tyrone.value, player, world)
    tyrone.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], tyrone) for loc_name
                         in get_array([10])]

    #1-3
    l131 = Region(AERoom.W1L3Entry.value, player, world)
    l132 = Region(AERoom.W1L3Volcano.value, player, world)
    l133 = Region(AERoom.W1L3Triceratops.value, player, world)
    scotty = Region(AERoom.W1L3Scotty.value, player, world)
    scotty.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], scotty) for loc_name
                      in get_array([11])]
    coco = Region(AERoom.W1L3Coco.value, player, world)
    coco.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coco) for loc_name
                         in get_array([12])]
    jthomas = Region(AERoom.W1L3JThomas.value, player, world)
    jthomas.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], jthomas) for loc_name
                       in get_array([13])]
    mattie = Region(AERoom.W1L3Mattie.value, player, world)
    mattie.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], mattie) for loc_name
                          in get_array([14])]
    barney = Region(AERoom.W1L3Barney.value, player, world)
    barney.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], barney) for loc_name
                          in get_array([15])]
    rocky = Region(AERoom.W1L3Rocky.value, player, world)
    rocky.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], rocky) for loc_name
                          in get_array([16])]
    moggan = Region(AERoom.W1L3Moggan.value, player, world)
    moggan.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], moggan) for loc_name
                          in get_array([17])]

    #2-1
    l21 = Region("2-1", player, world)
    l21.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l21) for loc_name
                      in get_range(18, 26)]

    l211 = Region("2-1 Mush", player, world)
    l211.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l211) for loc_name
                      in get_range(29, 31)]

    l212 = Region("2-1 Hang", player, world)
    l212.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l212) for loc_name
                       in get_range(27, 27)]

    l213 = Region("2-1 UFO", player, world)
    l213.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l213) for loc_name
                       in get_range(28, 28)]

    l22 = Region("2-2", player, world)
    l22.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l22) for loc_name
                      in get_range(33, 34)]
    l22.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l22) for loc_name
                      in get_range(36, 37)]
    l22.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l22) for loc_name
                      in get_range(40, 43)]

    l221 = Region("2-2 Fast", player, world)
    l221.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l221) for loc_name
                      in get_range(32, 32)]

    l222 = Region("2-2 Fan", player, world)
    l222.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l222) for loc_name
                       in get_range(35, 35)]

    l223 = Region("2-2 Vine", player, world)
    l223.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l223) for loc_name
                       in get_range(38, 38)]

    l224 = Region("2-2 Base", player, world)
    l224.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l224) for loc_name
                       in get_range(39, 39)]
    l224.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l224) for loc_name
                       in get_range(44, 44)]

    l23 = Region("2-3", player, world)
    l23.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l23) for loc_name
                      in get_range(49, 49)]

    l231 = Region("2-3 SF", player, world)
    l231.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l231) for loc_name
                      in get_range(45, 45)]
    l231.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l231) for loc_name
                       in get_range(51, 51)]

    l232 = Region("2-3 SP", player, world)
    l232.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l232) for loc_name
                       in get_range(46, 48)]
    l232.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l232) for loc_name
                       in get_range(50, 50)]

    l233 = Region("2-3 SPC", player, world)
    l233.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l233) for loc_name
                       in get_range(52, 52)]

    l41 = Region("4-1", player, world)
    l41.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l41) for loc_name
                      in get_range(53, 57)]
    l41.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l41) for loc_name
                      in get_range(60, 60)]

    l411 = Region("4-1 SF", player, world)
    l411.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l411) for loc_name
                      in get_range(58, 58)]

    l412 = Region("4-1 F", player, world)
    l412.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l412) for loc_name
                      in get_range(59, 59)]

    l42 = Region("4-2", player, world)
    l42.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l42) for loc_name
                      in get_range(61, 61)]
    l42.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l42) for loc_name
                      in get_range(63, 63)]
    l42.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l42) for loc_name
                      in get_range(65, 68)]

    l421 = Region("4-2 HF", player, world)
    l421.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l421) for loc_name
                      in get_range(62, 62)]
    l421.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l421) for loc_name
                       in get_range(64, 64)]

    l43 = Region("4-3", player, world)
    l43.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l43) for loc_name
                      in get_range(69, 71)]
    l43.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l43) for loc_name
                      in get_range(74, 76)]
    l43.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l43) for loc_name
                      in get_range(78, 79)]

    l431 = Region("4-3 C", player, world)
    l431.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l431) for loc_name
                      in get_range(77, 77)]

    l432 = Region("4-3 S", player, world)
    l432.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l432) for loc_name
                      in get_range(72, 73)]

    l51 = Region("5-1", player, world)
    l51.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l51) for loc_name
                      in get_range(80, 83)]
    l51.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l51) for loc_name
                      in get_range(85, 85)]

    l511 = Region("5-1 S", player, world)
    l511.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l511) for loc_name
                      in get_range(84, 84)]

    l52 = Region("5-2", player, world)
    l52.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l52) for loc_name
                      in get_range(86, 90)]
    l52.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l52) for loc_name
                      in get_range(92, 94)]

    l522 = Region("5-2 S", player, world)
    l522.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l522) for loc_name
                      in get_range(91, 91)]

    l53 = Region("5-3", player, world)
    l53.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l53) for loc_name
                      in get_range(95, 98)]

    l531 = Region("5-3 F", player, world)
    l531.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l531) for loc_name
                      in get_range(99, 103)]

    l71 = Region("7-1", player, world)
    l71.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l71) for loc_name
                      in get_range(104, 106)]
    l71.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l71) for loc_name
                      in get_range(108, 112)]

    l711 = Region("7-1 S", player, world)
    l711.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l711) for loc_name
                      in get_range(107, 107)]
    l711.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l711) for loc_name
                       in get_range(113, 113)]

    l712 = Region("7-1 F", player, world)
    l712.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l712) for loc_name
                       in get_range(114, 115)]

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
                              w1, w2, w3, w4, w5, w6, w7, w8, w9,
                              l11, noonan, jorjy, nati, trayc,
                              l12, shay, drmonk, grunt, ahchoo, gornif, tyrone,
                              l131, l132, l133, scotty, coco, jthomas, mattie, barney, rocky, moggan,
                              l21, l22, l23, l41, l42, l43,
                              l51, l52, l53, l71, l72, l73, l81, l82, l83, l91,
                              l131,l132,
                              l211,l212,l213,l221,l222,l223,l224,l231,l232,l233,
                              l411,l412,l421,l431,l432,
                              l511, l522, l531,
                              l711, l712])

    world.regions.extend([menu,
                          w1, w2, w3, w4, w5, w6, w7, w8, w9,
                          l11, noonan, jorjy, nati, trayc,
                          l12, shay, drmonk, grunt, ahchoo, gornif, tyrone,
                          l131, l132, l133, scotty, coco, jthomas, mattie, barney, rocky, moggan,
                          l21, l22, l23, l41, l42, l43,
                          l51, l52, l53, l71, l72, l73, l81, l82, l83, l91,
                          l131, l132,
                          l211, l212, l213, l221, l222, l223, l224, l231, l232, l233,
                          l411, l412, l421, l431, l432,
                          l511, l522, l531,
                          l711, l712])



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

def get_array(array):
    res = dict()
    for i in array:
        for key, val in location_table.items():
            if int(val) == i + 128000000:
                res[key] = val
    return res
