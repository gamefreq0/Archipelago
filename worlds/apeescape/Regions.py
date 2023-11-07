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
    l211 = Region(AERoom.W2L1Entry.value, player, world)
    l212 = Region(AERoom.W2L1Mushroom.value, player, world)
    l213 = Region(AERoom.W2L1Fish.value, player, world)
    l214 = Region(AERoom.W2L1Tent.value, player, world)
    l215 = Region(AERoom.W2L1Boulder.value, player, world)
    marquez = Region(AERoom.W2L1Marquez.value, player, world)
    marquez.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], marquez) for loc_name
                         in get_array([18])]
    livinston = Region(AERoom.W2L1Livinston.value, player, world)
    livinston.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], livinston) for loc_name
                         in get_array([19])]
    george = Region(AERoom.W2L1George.value, player, world)
    george.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], george) for loc_name
                         in get_array([20])]
    gonzo = Region(AERoom.W2L1Gonzo.value, player, world)
    gonzo.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], gonzo) for loc_name
                         in get_array([29])]
    zanzibar = Region(AERoom.W2L1Zanzibar.value, player, world)
    zanzibar.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], zanzibar) for loc_name
                         in get_array([22])]
    alphonse = Region(AERoom.W2L1Alphonse.value, player, world)
    alphonse.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], alphonse) for loc_name
                         in get_array([30])]
    maki = Region(AERoom.W2L1Maki.value, player, world)
    maki.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], maki) for loc_name
                         in get_array([21])]
    herb = Region(AERoom.W2L1Herb.value, player, world)
    herb.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], herb) for loc_name
                         in get_array([25])]
    dilweed = Region(AERoom.W2L1Dilweed.value, player, world)
    dilweed.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], dilweed) for loc_name
                         in get_array([23])]
    stoddy = Region(AERoom.W2L1Stoddy.value, player, world)
    stoddy.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], stoddy) for loc_name
                         in get_array([27])]
    mitong = Region(AERoom.W2L1Mitong.value, player, world)
    mitong.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], mitong) for loc_name
                         in get_array([24])]
    nasus = Region(AERoom.W2L1Nasus.value, player, world)
    nasus.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], nasus) for loc_name
                         in get_array([26])]
    elehcim = Region(AERoom.W2L1Elehcim.value, player, world)
    elehcim.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], elehcim) for loc_name
                         in get_array([28])]
    selur = Region(AERoom.W2L1Selur.value, player, world)
    selur.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], selur) for loc_name
                        in get_array([31])]

    #2-2
    l221 = Region(AERoom.W2L2Outside.value, player, world)
    l222 = Region(AERoom.W2L2Fan.value, player, world)
    l223 = Region(AERoom.W2L2Obelisk.value, player, world)
    l224 = Region(AERoom.W2L2Water.value, player, world)

    mooshy = Region(AERoom.W2L2Mooshy.value, player, world)
    mooshy.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], mooshy) for loc_name in
                         get_array([32])]
    kyle = Region(AERoom.W2L2Kyle.value, player, world)
    kyle.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], kyle) for loc_name in
                       get_array([33])]
    cratman = Region(AERoom.W2L2Cratman.value, player, world)
    cratman.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], cratman) for loc_name in
                          get_array([34])]
    nuzzy = Region(AERoom.W2L2Nuzzy.value, player, world)
    nuzzy.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], nuzzy) for loc_name in
                        get_array([35])]
    mav = Region(AERoom.W2L2Mav.value, player, world)
    mav.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], mav) for loc_name in
                      get_array([36])]
    stan = Region(AERoom.W2L2Stan.value, player, world)
    stan.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], stan) for loc_name in
                       get_array([37])]
    bernt = Region(AERoom.W2L2Bernt.value, player, world)
    bernt.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], bernt) for loc_name in
                       get_array([38])]
    runt = Region(AERoom.W2L2Runt.value, player, world)
    runt.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], runt) for loc_name in
                        get_array([39])]
    hoolah = Region(AERoom.W2L2Hoolah.value, player, world)
    hoolah.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], hoolah) for loc_name in
                       get_array([40])]
    papou = Region(AERoom.W2L2Papou.value, player, world)
    papou.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], papou) for loc_name in
                         get_array([41])]
    kenny = Region(AERoom.W2L2Kenny.value, player, world)
    kenny.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], kenny) for loc_name in
                        get_array([42])]
    trance = Region(AERoom.W2L2Trance.value, player, world)
    trance.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], trance) for loc_name in
                        get_array([43])]
    chino = Region(AERoom.W2L2Chino.value, player, world)
    chino.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], chino) for loc_name in
                         get_array([44])]

    #2-3
    l231 = Region(AERoom.W2L3Outside.value, player, world)
    l232 = Region(AERoom.W2L3Side.value, player, world)
    l233 = Region(AERoom.W2L3Main.value, player, world)
    l234 = Region(AERoom.W2L3Pillar.value, player, world)

    troopa = Region(AERoom.W2L3Troopa.value, player, world)
    troopa.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], troopa) for loc_name in
                        get_array([45])]
    spanky = Region(AERoom.W2L3Spanky.value, player, world)
    spanky.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], spanky) for loc_name in
                         get_array([46])]
    stymie = Region(AERoom.W2L3Stymie.value, player, world)
    stymie.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], stymie) for loc_name in
                         get_array([47])]
    pally = Region(AERoom.W2L3Pally.value, player, world)
    pally.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], pally) for loc_name in
                         get_array([48])]
    freeto = Region(AERoom.W2L3Freeto.value, player, world)
    freeto.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], freeto) for loc_name in
                        get_array([49])]
    jesta = Region(AERoom.W2L3Jesta.value, player, world)
    jesta.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], jesta) for loc_name in
                         get_array([50])]
    bazzle = Region(AERoom.W2L3Bazzle.value, player, world)
    bazzle.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], bazzle) for loc_name in
                        get_array([51])]
    crash = Region(AERoom.W2L3Crash.value, player, world)
    crash.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], crash) for loc_name in
                         get_array([52])]

    #4-1
    l411 = Region(AERoom.W4L1FirstRoom.value, player, world)
    l412 = Region(AERoom.W4L1SecondRoom.value, player, world)
    coolblue = Region(AERoom.W4L1CoolBlue.value, player, world)
    coolblue.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coolblue) for loc_name in
                        get_array([53])]
    sandy = Region(AERoom.W4L1Sandy.value, player, world)
    sandy.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], sandy) for loc_name in
                           get_array([54])]
    sandy = Region(AERoom.W4L1Sandy.value, player, world)
    sandy.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], sandy) for loc_name in
                        get_array([54])]
    shelle = Region(AERoom.W4L1ShellE.value, player, world)
    shelle.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], shelle) for loc_name in
                        get_array([55])]
    gidget = Region(AERoom.W4L1Gidget.value, player, world)
    gidget.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], gidget) for loc_name in
                         get_array([56])]
    shaka = Region(AERoom.W4L1Shaka.value, player, world)
    shaka.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], shaka) for loc_name in
                         get_array([57])]
    maxmahalo = Region(AERoom.W4L1MaxMahalo.value, player, world)
    maxmahalo.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], maxmahalo) for loc_name in
                        get_array([58])]
    moko = Region(AERoom.W4L1Moko.value, player, world)
    moko.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], moko) for loc_name in
                            get_array([59])]
    puka = Region(AERoom.W4L1Puka.value, player, world)
    puka.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], puka) for loc_name in
                       get_array([60])]

    #4-2
    l421 = Region(AERoom.W4L2FirstRoom.value, player, world)
    l422 = Region(AERoom.W4L2SecondRoom.value, player, world)
    chip = Region(AERoom.W4L2Chip.value, player, world)
    chip.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], chip) for loc_name in
                       get_array([61])]
    oreo = Region(AERoom.W4L2Oreo.value, player, world)
    oreo.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], oreo) for loc_name in
                       get_array([62])]
    puddles = Region(AERoom.W4L2Puddles.value, player, world)
    puddles.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], puddles) for loc_name in
                       get_array([63])]
    kalama = Region(AERoom.W4L2Kalama.value, player, world)
    kalama.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], kalama) for loc_name in
                          get_array([64])]
    iz = Region(AERoom.W4L2Iz.value, player, world)
    iz.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], iz) for loc_name in
                         get_array([65])]
    jux = Region(AERoom.W4L2Jux.value, player, world)
    jux.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], jux) for loc_name in
                     get_array([66])]
    bongbong = Region(AERoom.W4L2BongBong.value, player, world)
    bongbong.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], bongbong) for loc_name in
                      get_array([67])]
    pickles = Region(AERoom.W4L2Pickles.value, player, world)
    pickles.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], pickles) for loc_name in
                           get_array([68])]

    #4-3
    l431 = Region(AERoom.W4L3Outside.value, player, world)
    l432 = Region(AERoom.W4L3Stomach.value, player, world)
    l433 = Region(AERoom.W4L3Slide.value, player, world)
    l434 = Region(AERoom.W4L3Gallery.value, player, world)
    l435 = Region(AERoom.W4L3Tentacle.value, player, world)
    stuw = Region(AERoom.W4L3Stuw.value, player, world)
    stuw.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], stuw) for loc_name in
                          get_array([69])]
    tonton = Region(AERoom.W4L3TonTon.value, player, world)
    tonton.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], tonton) for loc_name in
                       get_array([70])]
    murky = Region(AERoom.W4L3Murky.value, player, world)
    murky.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], murky) for loc_name in
                         get_array([71])]
    howeerd = Region(AERoom.W4L3Howeerd.value, player, world)
    howeerd.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], howeerd) for loc_name in
                        get_array([72])]
    robbin = Region(AERoom.W4L3Robbin.value, player, world)
    robbin.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], robbin) for loc_name in
                          get_array([73])]
    jakkee = Region(AERoom.W4L3Jakkee.value, player, world)
    jakkee.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], jakkee) for loc_name in
                         get_array([74])]
    frederic = Region(AERoom.W4L3Frederic.value, player, world)
    frederic.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], frederic) for loc_name in
                         get_array([75])]
    baba = Region(AERoom.W4L3Baba.value, player, world)
    baba.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], baba) for loc_name in
                           get_array([76])]
    mars = Region(AERoom.W4L3Mars.value, player, world)
    mars.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], mars) for loc_name in
                       get_array([77])]
    horke = Region(AERoom.W4L3Horke.value, player, world)
    horke.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], horke) for loc_name in
                       get_array([78])]
    quirck = Region(AERoom.W4L3Quirck.value, player, world)
    quirck.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], quirck) for loc_name in
                        get_array([79])]

    #5-1
    l51 = Region(AERoom.W5L1Main.value, player, world)

    popcicle = Region(AERoom.W5L1Popcicle.value, player, world)
    popcicle.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], popcicle) for loc_name in
                         get_array([80])]
    iced = Region(AERoom.W5L1Iced.value, player, world)
    iced.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], iced) for loc_name in
                           get_array([81])]
    denggoy = Region(AERoom.W5L1Denggoy.value, player, world)
    denggoy.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], denggoy) for loc_name in
                       get_array([82])]

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
                              l211, l212, l213, l214, l215, marquez, livinston, george, maki, herb, dilweed, mitong, stoddy, nasus, selur, elehcim, gonzo, alphonse, zanzibar,
                              l221, l222, l223, l224, kyle, stan, kenny, cratman, mooshy, nuzzy, mav, papou, trance, bernt, runt, hoolah, chino,
                              l231, l232, l233, l234, bazzle, freeto, troopa, stymie, spanky, jesta, pally, crash,
                              l411, l412, coolblue, sandy, shelle, gidget, shaka, maxmahalo, moko, puka,
                              l421, l422, chip, oreo, puddles, kalama, iz, bongbong, jux, pickles,
                              l431, l432, l433, l434, l435, tonton, stuw, mars, murky, horke, howeerd, robbin, jakkee, frederic, baba, quirck,
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
                          l211, l212, l213, l214, l215, marquez, livinston, george, maki, herb, dilweed, mitong, stoddy,
                          nasus, selur, elehcim, gonzo, alphonse, zanzibar,
                          l221, l222, l223, l224, kyle, stan, kenny, cratman, mooshy, nuzzy, mav, papou, trance, bernt,
                          runt, hoolah, chino,
                          l231, l232, l233, l234, bazzle, freeto, troopa, stymie, spanky, jesta, pally, crash,
                          l411, l412, coolblue, sandy, shelle, gidget, shaka, maxmahalo, moko, puka,
                          l421, l422, chip, oreo, puddles, kalama, iz, bongbong, jux, pickles,
                          l431, l432, l433, l434, l435, tonton, stuw, mars, murky, horke, howeerd, robbin, jakkee,
                          frederic, baba, quirck,
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
