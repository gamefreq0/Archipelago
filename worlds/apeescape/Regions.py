from BaseClasses import MultiWorld, Region, Entrance
from .Locations import location_table, ApeEscapeLocation
from .Strings import AEWorld, AERoom


def create_regions(world: MultiWorld, player: int):
    # menu
    menu = Region("Menu", player, world)

    # worlds
    w1 = Region(AEWorld.W1.value, player, world)
    w2 = Region(AEWorld.W2.value, player, world)
    w3 = Region(AEWorld.W3.value, player, world)
    w4 = Region(AEWorld.W4.value, player, world)
    w5 = Region(AEWorld.W5.value, player, world)
    w6 = Region(AEWorld.W6.value, player, world)
    w7 = Region(AEWorld.W7.value, player, world)
    w8 = Region(AEWorld.W8.value, player, world)
    w9 = Region(AEWorld.W9.value, player, world)

    # 1-1
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

    # 1-2
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

    # 1-3
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


    # 2-1
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
                           in get_array([31])]
    alphonse = Region(AERoom.W2L1Alphonse.value, player, world)
    alphonse.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], alphonse) for loc_name
                           in get_array([30])]
    maki = Region(AERoom.W2L1Maki.value, player, world)
    maki.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], maki) for loc_name
                       in get_array([21])]
    herb = Region(AERoom.W2L1Herb.value, player, world)
    herb.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], herb) for loc_name
                       in get_array([22])]
    dilweed = Region(AERoom.W2L1Dilweed.value, player, world)
    dilweed.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], dilweed) for loc_name
                          in get_array([23])]
    stoddy = Region(AERoom.W2L1Stoddy.value, player, world)
    stoddy.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], stoddy) for loc_name
                         in get_array([25])]
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
                        in get_array([27])]

    # 2-2
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

    # 2-3
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

    # 4-1
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

    # 4-2
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



    # 4-3
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



    # 5-1
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
    skeens = Region(AERoom.W5L1Skeens.value, player, world)
    skeens.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], skeens) for loc_name in
                         get_array([83])]
    rickets = Region(AERoom.W5L1Rickets.value, player, world)
    rickets.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], rickets) for loc_name in
                          get_array([84])]
    chilly = Region(AERoom.W5L1Chilly.value, player, world)
    chilly.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], chilly) for loc_name in
                         get_array([85])]

    # 5-2
    l521 = Region(AERoom.W5L2Entry.value, player, world)
    l522 = Region(AERoom.W5L2Water.value, player, world)
    l523 = Region(AERoom.W5L2Caverns.value, player, world)
    storm = Region(AERoom.W5L2Storm.value, player, world)
    storm.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], storm) for loc_name in
                        get_array([86])]
    qube = Region(AERoom.W5L2Qube.value, player, world)
    qube.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], qube) for loc_name in
                       get_array([87])]
    gash = Region(AERoom.W5L2Gash.value, player, world)
    gash.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], gash) for loc_name in
                       get_array([88])]
    kundra = Region(AERoom.W5L2Kundra.value, player, world)
    kundra.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], kundra) for loc_name in
                         get_array([89])]
    shadow = Region(AERoom.W5L2Shadow.value, player, world)
    shadow.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], shadow) for loc_name in
                         get_array([90])]
    ranix = Region(AERoom.W5L2Ranix.value, player, world)
    ranix.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], ranix) for loc_name in
                        get_array([91])]
    sticky = Region(AERoom.W5L2Sticky.value, player, world)
    sticky.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], sticky) for loc_name in
                         get_array([92])]
    sharpe = Region(AERoom.W5L2Sharpe.value, player, world)
    sharpe.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], sharpe) for loc_name in
                         get_array([93])]
    droog = Region(AERoom.W5L2Droog.value, player, world)
    droog.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], droog) for loc_name in
                        get_array([94])]

    # 5-3
    l531 = Region(AERoom.W5L3Outside.value, player, world)
    l532 = Region(AERoom.W5L3Spring.value, player, world)
    l533 = Region(AERoom.W5L3Cave.value, player, world)
    punky = Region(AERoom.W5L3Punky.value, player, world)
    punky.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], punky) for loc_name in
                        get_array([95])]
    ameego = Region(AERoom.W5L3Ameego.value, player, world)
    ameego.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], ameego) for loc_name in
                         get_array([96])]
    roti = Region(AERoom.W5L3Roti.value, player, world)
    roti.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], roti) for loc_name in
                       get_array([97])]
    dissa = Region(AERoom.W5L3Dissa.value, player, world)
    dissa.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], dissa) for loc_name in
                        get_array([98])]
    yoky = Region(AERoom.W5L3Yoky.value, player, world)
    yoky.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], yoky) for loc_name in
                       get_array([99])]
    jory = Region(AERoom.W5L3Jory.value, player, world)
    jory.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], jory) for loc_name in
                       get_array([100])]
    crank = Region(AERoom.W5L3Crank.value, player, world)
    crank.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], crank) for loc_name in
                        get_array([101])]
    claxter = Region(AERoom.W5L3Claxter.value, player, world)
    claxter.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], claxter) for loc_name in
                          get_array([102])]
    looza = Region(AERoom.W5L3Looza.value, player, world)
    looza.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], looza) for loc_name in
                        get_array([103])]

    # 7-1
    l711 = Region(AERoom.W7L1Outside.value, player, world)
    l712 = Region(AERoom.W7L1Temple.value, player, world)
    l713 = Region(AERoom.W7L1Well.value, player, world)
    taku = Region(AERoom.W7L1Taku.value, player, world)
    taku.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], taku) for loc_name in
                       get_array([104])]
    rocka = Region(AERoom.W7L1Rocka.value, player, world)
    rocka.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], rocka) for loc_name in
                        get_array([105])]
    maralea = Region(AERoom.W7L1Maralea.value, player, world)
    maralea.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], maralea) for loc_name in
                          get_array([106])]
    wog = Region(AERoom.W7L1Wog.value, player, world)
    wog.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], wog) for loc_name in
                      get_array([107])]
    long = Region(AERoom.W7L1Long.value, player, world)
    long.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], long) for loc_name in
                       get_array([108])]
    mayi = Region(AERoom.W7L1Mayi.value, player, world)
    mayi.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], mayi) for loc_name in
                       get_array([109])]
    owyang = Region(AERoom.W7L1Owyang.value, player, world)
    owyang.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], owyang) for loc_name in
                         get_array([110])]
    queltin = Region(AERoom.W7L1QuelTin.value, player, world)
    queltin.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], queltin) for loc_name in
                          get_array([111])]
    phaldo = Region(AERoom.W7L1Phaldo.value, player, world)
    phaldo.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], phaldo) for loc_name in
                         get_array([112])]
    voti = Region(AERoom.W7L1Voti.value, player, world)
    voti.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], voti) for loc_name in
                       get_array([113])]
    elly = Region(AERoom.W7L1Elly.value, player, world)
    elly.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], elly) for loc_name in
                       get_array([114])]
    chunky = Region(AERoom.W7L1Chunky.value, player, world)
    chunky.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], chunky) for loc_name in
                         get_array([115])]

    # 7-2
    l721 = Region(AERoom.W7L2First.value, player, world)
    l722 = Region(AERoom.W7L2Gong.value, player, world)
    l723 = Region(AERoom.W7L2Middle.value, player, world)
    l724 = Region(AERoom.W7L2Course.value, player, world)
    l725 = Region(AERoom.W7L2Barrel.value, player, world)
    minky = Region(AERoom.W7L2Minky.value, player, world)
    minky.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], minky) for loc_name in
                        get_array([116])]
    zobbro = Region(AERoom.W7L2Zobbro.value, player, world)
    zobbro.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], zobbro) for loc_name in
                         get_array([117])]
    xeeto = Region(AERoom.W7L2Xeeto.value, player, world)
    xeeto.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], xeeto) for loc_name in
                        get_array([118])]
    moops = Region(AERoom.W7L2Moops.value, player, world)
    moops.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], moops) for loc_name in
                        get_array([119])]
    zanabi = Region(AERoom.W7L2Zanabi.value, player, world)
    zanabi.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], zanabi) for loc_name in
                         get_array([120])]
    buddah = Region(AERoom.W7L2Buddha.value, player, world)
    buddah.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], buddah) for loc_name in
                         get_array([121])]
    fooey = Region(AERoom.W7L2Fooey.value, player, world)
    fooey.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], fooey) for loc_name in
                        get_array([122])]
    doxs = Region(AERoom.W7L2Doxs.value, player, world)
    doxs.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], doxs) for loc_name in
                       get_array([123])]
    kong = Region(AERoom.W7L2Kong.value, player, world)
    kong.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], kong) for loc_name in
                       get_array([124])]
    phool = Region(AERoom.W7L2Phool.value, player, world)
    phool.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], phool) for loc_name in
                        get_array([125])]

    # 7-3
    l731 = Region(AERoom.W7L3Outside.value, player, world)
    l732 = Region(AERoom.W7L3Castle.value, player, world)
    l733 = Region(AERoom.W7L3Basement.value, player, world)
    l734 = Region(AERoom.W7L3Button.value, player, world)
    l735 = Region(AERoom.W7L3Elevator.value, player, world)
    l736 = Region(AERoom.W7L3Bell.value, player, world)
    l737 = Region(AERoom.W7L3Boss.value, player, world)

    naners = Region(AERoom.W7L3Naners.value, player, world)
    naners.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], naners) for loc_name in
                         get_array([126])]
    robart = Region(AERoom.W7L3Robart.value, player, world)
    robart.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], robart) for loc_name in
                         get_array([127])]
    neeners = Region(AERoom.W7L3Neeners.value, player, world)
    neeners.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], neeners) for loc_name in
                          get_array([128])]
    gustav = Region(AERoom.W7L3Gustav.value, player, world)
    gustav.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], gustav) for loc_name in
                         get_array([129])]
    wilhelm = Region(AERoom.W7L3Wilhelm.value, player, world)
    wilhelm.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], wilhelm) for loc_name in
                          get_array([130])]
    emmanuel = Region(AERoom.W7L3Emmanuel.value, player, world)
    emmanuel.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], emmanuel) for loc_name in
                           get_array([131])]
    sircutty = Region(AERoom.W7L3SirCutty.value, player, world)
    sircutty.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], sircutty) for loc_name in
                           get_array([132])]
    calligan = Region(AERoom.W7L3Calligan.value, player, world)
    calligan.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], calligan) for loc_name in
                           get_array([133])]
    castalist = Region(AERoom.W7L3Castalist.value, player, world)
    castalist.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], castalist) for loc_name in
                            get_array([134])]
    deveneom = Region(AERoom.W7L3Deveneom.value, player, world)
    deveneom.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], deveneom) for loc_name in
                           get_array([135])]
    igor = Region(AERoom.W7L3Igor.value, player, world)
    igor.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], igor) for loc_name in
                       get_array([136])]
    charles = Region(AERoom.W7L3Charles.value, player, world)
    charles.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], charles) for loc_name in
                          get_array([137])]
    astur = Region(AERoom.W7L3Astur.value, player, world)
    astur.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], astur) for loc_name in
                        get_array([138])]
    kilserack = Region(AERoom.W7L3Kilserack.value, player, world)
    kilserack.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], kilserack) for loc_name in
                            get_array([139])]
    ringo = Region(AERoom.W7L3Ringo.value, player, world)
    ringo.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], ringo) for loc_name in
                        get_array([140])]
    densil = Region(AERoom.W7L3Densil.value, player, world)
    densil.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], densil) for loc_name in
                         get_array([141])]
    figero = Region(AERoom.W7L3Figero.value, player, world)
    figero.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], figero) for loc_name in
                         get_array([142])]
    fej = Region(AERoom.W7L3Fej.value, player, world)
    fej.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], fej) for loc_name in
                      get_array([143])]
    joey = Region(AERoom.W7L3Joey.value, player, world)
    joey.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], joey) for loc_name in
                       get_array([144])]
    donqui = Region(AERoom.W7L3Donqui.value, player, world)
    donqui.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], donqui) for loc_name in
                         get_array([145])]

    # 8-1
    l811 = Region(AERoom.W8L1Outside.value, player, world)
    l812 = Region(AERoom.W8L1Sewers.value, player, world)
    l813 = Region(AERoom.W8L1Barrel.value, player, world)

    kaine = Region(AERoom.W8L1Kaine.value, player, world)
    kaine.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], kaine) for loc_name in
                        get_array([146])]
    jaxx = Region(AERoom.W8L1Jaxx.value, player, world)
    jaxx.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], jaxx) for loc_name in
                       get_array([147])]
    gehry = Region(AERoom.W8L1Gehry.value, player, world)
    gehry.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], gehry) for loc_name in
                        get_array([148])]
    alcatraz = Region(AERoom.W8L1Alcatraz.value, player, world)
    alcatraz.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], alcatraz) for loc_name in
                           get_array([149])]
    tino = Region(AERoom.W8L1Tino.value, player, world)
    tino.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], tino) for loc_name in
                       get_array([150])]
    qbee = Region(AERoom.W8L1QBee.value, player, world)
    qbee.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], qbee) for loc_name in
                       get_array([151])]
    mcmanic = Region(AERoom.W8L1McManic.value, player, world)
    mcmanic.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], mcmanic) for loc_name in
                          get_array([152])]
    dywan = Region(AERoom.W8L1Dywan.value, player, world)
    dywan.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], dywan) for loc_name in
                        get_array([153])]
    ckhutch = Region(AERoom.W8L1CKHutch.value, player, world)
    ckhutch.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], ckhutch) for loc_name in
                          get_array([154])]
    winky = Region(AERoom.W8L1Winky.value, player, world)
    winky.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], winky) for loc_name in
                        get_array([155])]
    bluv = Region(AERoom.W8L1BLuv.value, player, world)
    bluv.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], bluv) for loc_name in
                       get_array([156])]
    camper = Region(AERoom.W8L1Camper.value, player, world)
    camper.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], camper) for loc_name in
                         get_array([157])]
    huener = Region(AERoom.W8L1Huener.value, player, world)
    huener.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], huener) for loc_name in
                         get_array([158])]

    # 8-2
    l821 = Region(AERoom.W8L2Outside.value, player, world)
    l822 = Region(AERoom.W8L2Factory.value, player, world)
    l823 = Region(AERoom.W8L2RC.value, player, world)
    l824 = Region(AERoom.W8L2Lava.value, player, world)
    l825 = Region(AERoom.W8L2Conveyor.value, player, world)
    l826 = Region(AERoom.W8L2Mech.value, player, world)

    bigshow = Region(AERoom.W8L2BigShow.value, player, world)
    bigshow.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], bigshow) for loc_name in
                          get_array([159])]
    dreos = Region(AERoom.W8L2Dreos.value, player, world)
    dreos.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], dreos) for loc_name in
                        get_array([160])]
    reznor = Region(AERoom.W8L2Reznor.value, player, world)
    reznor.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], reznor) for loc_name in
                         get_array([161])]
    urkel = Region(AERoom.W8L2Urkel.value, player, world)
    urkel.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], urkel) for loc_name in
                        get_array([162])]
    vanillas = Region(AERoom.W8L2VanillaS.value, player, world)
    vanillas.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], vanillas) for loc_name in
                           get_array([163])]
    radd = Region(AERoom.W8L2Radd.value, player, world)
    radd.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], radd) for loc_name in
                       get_array([164])]
    shimbo = Region(AERoom.W8L2Shimbo.value, player, world)
    shimbo.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], shimbo) for loc_name in
                         get_array([165])]
    hurt = Region(AERoom.W8L2Hurt.value, player, world)
    hurt.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], hurt) for loc_name in
                       get_array([166])]
    strung = Region(AERoom.W8L2String.value, player, world)
    strung.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], strung) for loc_name in
                         get_array([167])]
    khamo = Region(AERoom.W8L2Khamo.value, player, world)
    khamo.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], khamo) for loc_name in
                        get_array([168])]

    # 8-3
    l831 = Region(AERoom.W8L3Outside.value, player, world)
    l832 = Region(AERoom.W8L3Water.value, player, world)
    l833 = Region(AERoom.W8L3Lobby.value, player, world)
    l834 = Region(AERoom.W8L3Tank.value, player, world)
    l835 = Region(AERoom.W8L3Fan.value, player, world)
    l836 = Region(AERoom.W8L3Boss.value, player, world)

    fredo = Region(AERoom.W8L3Fredo.value, player, world)
    fredo.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], fredo) for loc_name in
                        get_array([169])]
    charlee = Region(AERoom.W8L3Charlee.value, player, world)
    charlee.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], charlee) for loc_name in
                          get_array([170])]
    mach3 = Region(AERoom.W8L3Mach3.value, player, world)
    mach3.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], mach3) for loc_name in
                        get_array([171])]
    tortuss = Region(AERoom.W8L3Tortuss.value, player, world)
    tortuss.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], tortuss) for loc_name in
                          get_array([172])]
    manic = Region(AERoom.W8L3Manic.value, player, world)
    manic.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], manic) for loc_name in
                        get_array([173])]
    ruptdis = Region(AERoom.W8L3Ruptdis.value, player, world)
    ruptdis.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], ruptdis) for loc_name in
                          get_array([174])]
    eighty7 = Region(AERoom.W8L3Eighty7.value, player, world)
    eighty7.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], eighty7) for loc_name in
                          get_array([175])]
    danio = Region(AERoom.W8L3Danio.value, player, world)
    danio.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], danio) for loc_name in
                        get_array([176])]
    roosta = Region(AERoom.W8L3Roosta.value, player, world)
    roosta.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], roosta) for loc_name in
                         get_array([177])]
    tellis = Region(AERoom.W8L3Tellis.value, player, world)
    tellis.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], tellis) for loc_name in
                         get_array([178])]
    whack = Region(AERoom.W8L3Whack.value, player, world)
    whack.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], whack) for loc_name in
                        get_array([179])]
    frostee = Region(AERoom.W8L3Frostee.value, player, world)
    frostee.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], frostee) for loc_name in
                          get_array([180])]

    # 9-1
    l911 = Region(AERoom.W9L1Entry.value, player, world)
    l912 = Region(AERoom.W9L1Haunted.value, player, world)
    l913 = Region(AERoom.W9L1Coffin.value, player, world)
    l914 = Region(AERoom.W9L1Natalie.value, player, world)
    l915 = Region(AERoom.W9L1Professor.value, player, world)
    l916 = Region(AERoom.W9L1Jake.value, player, world)
    l917 = Region(AERoom.W9L1Western.value, player, world)
    l918 = Region(AERoom.W9L1Crater.value, player, world)
    l919 = Region(AERoom.W9L1Outside.value, player, world)
    l9110 = Region(AERoom.W9L1Castle.value, player, world)
    l9111 = Region(AERoom.W9L1Climb1.value, player, world)
    l9112 = Region(AERoom.W9L1Climb2.value, player, world)
    l9113 = Region(AERoom.W9L1Head.value, player, world)
    l9114 = Region(AERoom.W9L1Side.value, player, world)
    l9115 = Region(AERoom.W9L1Boss.value, player, world)
    l9115.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l9115) for loc_name in
                        get_array([205])]

    goopo = Region(AERoom.W9L1Goopo.value, player, world)
    goopo.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], goopo) for loc_name in
                        get_array([181])]
    porto = Region(AERoom.W9L1Porto.value, player, world)
    porto.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], porto) for loc_name in
                        get_array([182])]
    slam = Region(AERoom.W9L1Slam.value, player, world)
    slam.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], slam) for loc_name in
                       get_array([183])]
    junk = Region(AERoom.W9L1Junk.value, player, world)
    junk.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], junk) for loc_name in
                       get_array([184])]
    crib = Region(AERoom.W9L1Crib.value, player, world)
    crib.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], crib) for loc_name in
                       get_array([185])]
    nak = Region(AERoom.W9L1Nak.value, player, world)
    nak.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], nak) for loc_name in
                      get_array([186])]
    cloy = Region(AERoom.W9L1Cloy.value, player, world)
    cloy.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], cloy) for loc_name in
                       get_array([187])]
    shaw = Region(AERoom.W9L1Shaw.value, player, world)
    shaw.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], shaw) for loc_name in
                       get_array([188])]
    flea = Region(AERoom.W9L1Flea.value, player, world)
    flea.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], flea) for loc_name in
                       get_array([189])]
    schafette = Region(AERoom.W9L1Schafette.value, player, world)
    schafette.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], schafette) for loc_name in
                            get_array([190])]
    donovan = Region(AERoom.W9L1Donovan.value, player, world)
    donovan.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], donovan) for loc_name in
                          get_array([191])]
    laura = Region(AERoom.W9L1Laura.value, player, world)
    laura.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], laura) for loc_name in
                        get_array([192])]
    uribe = Region(AERoom.W9L1Uribe.value, player, world)
    uribe.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], uribe) for loc_name in
                        get_array([193])]
    gordo = Region(AERoom.W9L1Gordo.value, player, world)
    gordo.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], gordo) for loc_name in
                        get_array([194])]
    raeski = Region(AERoom.W9L1Raeski.value, player, world)
    raeski.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], raeski) for loc_name in
                         get_array([195])]
    poopie = Region(AERoom.W9L1Poopie.value, player, world)
    poopie.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], poopie) for loc_name in
                         get_array([196])]
    teacup = Region(AERoom.W9L1Teacup.value, player, world)
    teacup.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], teacup) for loc_name in
                         get_array([197])]
    shine = Region(AERoom.W9L1Shine.value, player, world)
    shine.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], shine) for loc_name in
                        get_array([198])]
    wrench = Region(AERoom.W9L1Wrench.value, player, world)
    wrench.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], wrench) for loc_name in
                         get_array([199])]
    bronson = Region(AERoom.W9L1Bronson.value, player, world)
    bronson.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], bronson) for loc_name in
                          get_array([200])]
    bungee = Region(AERoom.W9L1Bungee.value, player, world)
    bungee.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], bungee) for loc_name in
                         get_array([201])]
    carro = Region(AERoom.W9L1Carro.value, player, world)
    carro.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], carro) for loc_name in
                        get_array([202])]
    carlito = Region(AERoom.W9L1Carlito.value, player, world)
    carlito.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], carlito) for loc_name in
                          get_array([203])]
    bg = Region(AERoom.W9L1BG.value, player, world)
    bg.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], bg) for loc_name in
                     get_array([204])]

    regions = [menu,
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
               l51, popcicle, iced, rickets, skeens, denggoy, chilly,
               l521, l522, l523, storm, qube, ranix, sharpe, sticky, droog, gash, kundra, shadow,
               l531, l532, l533, punky, ameego, yoky, jory, crank, claxter, looza, roti, dissa,
               l711, l712, l713, taku, rocka, maralea, wog, mayi, owyang, long, elly, chunky, voti, queltin,
               phaldo,
               l721, l722, l723, l724, l725, minky, zobbro, xeeto, moops, zanabi, doxs, buddah, fooey, kong,
               phool,
               l731, l732, l733, l734, l735, l736, l737,
               robart, igor, naners, neeners, charles, gustav, wilhelm, emmanuel, sircutty, calligan, castalist,
               deveneom, astur, kilserack, ringo, densil, figero, fej, joey, donqui,
               l811, l812, l813, kaine, jaxx, gehry, alcatraz, tino, qbee, mcmanic, dywan, ckhutch, winky,
               bluv, camper, huener,
               l821, l822, l823, l824, l825, l826, bigshow, dreos, reznor, urkel, vanillas, radd, shimbo,
               hurt, strung, khamo,
               l831, l832, l833, l834, l835, l836, fredo, charlee, mach3, tortuss, manic, ruptdis, eighty7,
               danio, roosta, tellis, whack, frostee,
               l911, l912, l913, l914, l915, l916, l917, l918, l919, l9110, l9111, l9112, l9113, l9114,
               l9115,
               goopo, porto, slam, junk, crib, nak, cloy, shaw, flea, schafette, donovan, laura, uribe,
               gordo, raeski, poopie, teacup, shine, wrench, bronson, bungee, carro, carlito, bg]

    if world.goal[player].value == 0x01:
        # 9-2

        l92 = Region(AERoom.W9L2Boss.value, player, world)
        l92.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], l92) for loc_name in
                          get_array([206])]
        regions += [l92]

    if world.coin[player].value == 0x00:
        coin1 = Region(AERoom.Coin1.value, player, world)
        coin1.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin1) for loc_name
                            in get_array([301])]
        coin2 = Region(AERoom.Coin2.value, player, world)
        coin2.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin2) for loc_name
                            in get_array([302])]
        coin3 = Region(AERoom.Coin3.value, player, world)
        coin3.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin3) for loc_name
                            in get_array([303])]
        coin6 = Region(AERoom.Coin6.value, player, world)
        coin6.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin6) for loc_name
                            in get_array([306])]
        coin7 = Region(AERoom.Coin7.value, player, world)
        coin7.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin7) for loc_name
                            in get_array([307])]
        coin8 = Region(AERoom.Coin8.value, player, world)
        coin8.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin8) for loc_name
                            in get_array([308])]
        coin9 = Region(AERoom.Coin9.value, player, world)
        coin9.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin9) for loc_name
                            in get_array([309])]
        coin11 = Region(AERoom.Coin11.value, player, world)
        coin11.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin11) for loc_name
                             in get_array([311])]
        coin12 = Region(AERoom.Coin12.value, player, world)
        coin12.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin12) for loc_name
                             in get_array([312])]
        coin13 = Region(AERoom.Coin13.value, player, world)
        coin13.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin13) for loc_name
                             in get_array([313])]
        coin14 = Region(AERoom.Coin14.value, player, world)
        coin14.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin14) for loc_name
                             in get_array([314])]
        coin17 = Region(AERoom.Coin17.value, player, world)
        coin17.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin17) for loc_name
                             in get_array([317])]
        coin19 = Region(AERoom.Coin19.value, player, world)
        coin19.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin19) for loc_name
                             in get_array([295, 296, 297, 298, 299])]
        coin21 = Region(AERoom.Coin21.value, player, world)
        coin21.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin21) for loc_name
                             in get_array([321])]
        coin23 = Region(AERoom.Coin23.value, player, world)
        coin23.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin23) for loc_name
                             in get_array([323])]
        coin24 = Region(AERoom.Coin24.value, player, world)
        coin24.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin24) for loc_name
                             in get_array([324])]
        coin25 = Region(AERoom.Coin25.value, player, world)
        coin25.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin25) for loc_name
                             in get_array([325])]
        coin28 = Region(AERoom.Coin28.value, player, world)
        coin28.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin28) for loc_name
                             in get_array([328])]
        coin29 = Region(AERoom.Coin29.value, player, world)
        coin29.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin29) for loc_name
                             in get_array([329])]
        coin30 = Region(AERoom.Coin30.value, player, world)
        coin30.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin30) for loc_name
                             in get_array([330])]
        coin31 = Region(AERoom.Coin31.value, player, world)
        coin31.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin31) for loc_name
                             in get_array([331])]
        coin32 = Region(AERoom.Coin32.value, player, world)
        coin32.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin32) for loc_name
                             in get_array([332])]
        coin34 = Region(AERoom.Coin34.value, player, world)
        coin34.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin34) for loc_name
                             in get_array([334])]
        coin35 = Region(AERoom.Coin35.value, player, world)
        coin35.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin35) for loc_name
                             in get_array([335])]
        coin36 = Region(AERoom.Coin36.value, player, world)
        coin36.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin36) for loc_name
                             in get_array([290, 291, 292, 293, 294])]
        coin37 = Region(AERoom.Coin37.value, player, world)
        coin37.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin37) for loc_name
                             in get_array([337])]
        coin38 = Region(AERoom.Coin38.value, player, world)
        coin38.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin38) for loc_name
                             in get_array([338])]
        coin39 = Region(AERoom.Coin39.value, player, world)
        coin39.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin39) for loc_name
                             in get_array([339])]
        coin40 = Region(AERoom.Coin40.value, player, world)
        coin40.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin40) for loc_name
                             in get_array([340])]
        coin41 = Region(AERoom.Coin41.value, player, world)
        coin41.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin41) for loc_name
                             in get_array([341])]
        coin43 = Region(AERoom.Coin43.value, player, world)
        coin43.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin43) for loc_name
                             in get_array([343])]
        coin45 = Region(AERoom.Coin45.value, player, world)
        coin45.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin45) for loc_name
                             in get_array([345])]
        coin46 = Region(AERoom.Coin46.value, player, world)
        coin46.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin46) for loc_name
                             in get_array([346])]
        coin49 = Region(AERoom.Coin49.value, player, world)
        coin49.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin49) for loc_name
                             in get_array([349])]
        coin50 = Region(AERoom.Coin50.value, player, world)
        coin50.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin50) for loc_name
                             in get_array([350])]
        coin53 = Region(AERoom.Coin53.value, player, world)
        coin53.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin53) for loc_name
                             in get_array([353])]
        coin54 = Region(AERoom.Coin54.value, player, world)
        coin54.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin54) for loc_name
                             in get_array([354])]
        coin55 = Region(AERoom.Coin55.value, player, world)
        coin55.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin55) for loc_name
                             in get_array([355])]
        coin58 = Region(AERoom.Coin58.value, player, world)
        coin58.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin58) for loc_name
                             in get_array([358])]
        coin62 = Region(AERoom.Coin62.value, player, world)
        coin62.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin62) for loc_name
                             in get_array([362])]
        coin64 = Region(AERoom.Coin64.value, player, world)
        coin64.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin64) for loc_name
                             in get_array([364])]
        coin66 = Region(AERoom.Coin66.value, player, world)
        coin66.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin66) for loc_name
                             in get_array([366])]
        coin73 = Region(AERoom.Coin73.value, player, world)
        coin73.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin73) for loc_name
                             in get_array([373])]
        coin74 = Region(AERoom.Coin74.value, player, world)
        coin74.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin74) for loc_name
                             in get_array([374])]
        coin75 = Region(AERoom.Coin75.value, player, world)
        coin75.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin75) for loc_name
                             in get_array([375])]
        coin77 = Region(AERoom.Coin77.value, player, world)
        coin77.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin77) for loc_name
                             in get_array([377])]
        coin78 = Region(AERoom.Coin78.value, player, world)
        coin78.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin78) for loc_name
                             in get_array([378])]
        coin79 = Region(AERoom.Coin79.value, player, world)
        coin79.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin79) for loc_name
                             in get_array([379])]
        coin80 = Region(AERoom.Coin80.value, player, world)
        coin80.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin80) for loc_name
                             in get_array([380])]
        coin82 = Region(AERoom.Coin82.value, player, world)
        coin82.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin82) for loc_name
                             in get_array([382])]
        coin84 = Region(AERoom.Coin84.value, player, world)
        coin84.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin84) for loc_name
                             in get_array([384])]
        coin85 = Region(AERoom.Coin85.value, player, world)
        coin85.locations += [ApeEscapeLocation(player, loc_name, location_table[loc_name], coin85) for loc_name
                             in get_array([385])]
        regions += [coin1, coin2, coin3, coin6, coin7, coin8, coin9, coin11, coin12, coin13, coin14, coin17, coin19,
                    coin21, coin23, coin24, coin25, coin28, coin29, coin30, coin31, coin32, coin34, coin35, coin36,
                    coin37, coin38, coin39, coin40, coin41, coin43, coin45, coin46, coin49, coin50, coin53, coin54,
                    coin55, coin58, coin62, coin64, coin66, coin73, coin74, coin75, coin77, coin78, coin79, coin80,
                    coin82, coin84, coin85]

    world.regions.extend(regions)


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
        if i <= int(val) <= j:
            res[key] = val
    return res


def get_array(array):
    res = dict()
    for i in array:
        for key, val in location_table.items():
            if int(val) == i + 128000000:
                res[key] = val
    return res
