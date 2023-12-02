from worlds.apeescape import location_table
from worlds.generic.Rules import add_rule, set_rule, forbid_item
from BaseClasses import LocationProgressType
from .Regions import connect_regions
from .Strings import AEItem, AEWorld, AERoom


class IJ():
    def set_rules(self, world, player: int, coins: bool):

        # Worlds
        connect_regions(world, player, "Menu", AEWorld.W1.value, lambda state: NoRequirement())
        connect_regions(world, player, "Menu", AEWorld.W2.value, lambda state: Keys(state, player, 1))
        connect_regions(world, player, "Menu", AEWorld.W3.value, lambda state: CanSwim(state, player))
        connect_regions(world, player, "Menu", AEWorld.W4.value, lambda state: Keys(state, player, 2))
        connect_regions(world, player, "Menu", AEWorld.W5.value, lambda state: Keys(state, player, 3))
        connect_regions(world, player, "Menu", AEWorld.W6.value, lambda state: HasFlyer(state, player))
        connect_regions(world, player, "Menu", AEWorld.W7.value, lambda state: Keys(state, player, 4))
        connect_regions(world, player, "Menu", AEWorld.W8.value, lambda state: Keys(state, player, 5))
        connect_regions(world, player, "Menu", AEWorld.W9.value, lambda state: Keys(state, player, 6))

        if world.goal[player].value == 0x01:
            connect_regions(world, player, "Menu", AERoom.W9L2Boss.value,
                            lambda state: Keys(state, player, 6) and HasSling(state, player)
                            and HasHoop(state, player) and HasFlyer(state, player) and CanHitMultiple(state, player)
                            and HasRC(state, player))

        # 1-1
        connect_regions(world, player, AEWorld.W1.value, AERoom.W1L1Main.value, lambda state: True)

        connect_regions(world, player, AERoom.W1L1Main.value, AERoom.W1L1Noonan.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W1L1Main.value, AERoom.W1L1Jorjy.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W1L1Main.value, AERoom.W1L1Nati.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W1L1Main.value, AERoom.W1L1TrayC.value, lambda state: NoRequirement())

        # 1-2
        connect_regions(world, player, AEWorld.W1.value, AERoom.W1L2Main.value, lambda state: True)

        connect_regions(world, player, AERoom.W1L2Main.value, AERoom.W1L2Shay.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W1L2Main.value, AERoom.W1L2DrMonk.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W1L2Main.value, AERoom.W1L2Grunt.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W1L2Main.value, AERoom.W1L2Ahchoo.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W1L2Main.value, AERoom.W1L2Gornif.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W1L2Main.value, AERoom.W1L2Tyrone.value, lambda state: NoRequirement())

        # 1-3
        connect_regions(world, player, AEWorld.W1.value, AERoom.W1L3Entry.value, lambda state: True)
        connect_regions(world, player, AERoom.W1L3Entry.value, AERoom.W1L3Volcano.value, lambda state: True)
        connect_regions(world, player, AERoom.W1L3Entry.value, AERoom.W1L3Triceratops.value,
                        lambda state: HasSling(state, player))

        connect_regions(world, player, AERoom.W1L3Entry.value, AERoom.W1L3Scotty.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W1L3Entry.value, AERoom.W1L3Coco.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W1L3Entry.value, AERoom.W1L3JThomas.value,
                        lambda state: CanHitOnce(state, player))
        connect_regions(world, player, AERoom.W1L3Entry.value, AERoom.W1L3Moggan.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W1L3Volcano.value, AERoom.W1L3Barney.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W1L3Volcano.value, AERoom.W1L3Mattie.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W1L3Triceratops.value, AERoom.W1L3Rocky.value,
                        lambda state: HasSling(state, player))

        # 2-1
        connect_regions(world, player, AEWorld.W2.value, AERoom.W2L1Entry.value, lambda state: True)
        connect_regions(world, player, AERoom.W2L1Entry.value, AERoom.W2L1Mushroom.value, lambda state: True)
        connect_regions(world, player, AERoom.W2L1Entry.value, AERoom.W2L1Fish.value, lambda state: True)
        connect_regions(world, player, AERoom.W2L1Fish.value, AERoom.W2L1Tent.value, lambda state: True)
        connect_regions(world, player, AERoom.W2L1Entry.value, AERoom.W2L1Boulder.value, lambda state: True)

        connect_regions(world, player, AERoom.W2L1Entry.value, AERoom.W2L1Marquez.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W2L1Entry.value, AERoom.W2L1Livinston.value,
                        lambda state: CanHitOnce(state, player))
        connect_regions(world, player, AERoom.W2L1Entry.value, AERoom.W2L1George.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W2L1Mushroom.value, AERoom.W2L1Gonzo.value,
                        lambda state: TJ_Mushroom(state, player) and CanHitMultiple(state, player))
        connect_regions(world, player, AERoom.W2L1Mushroom.value, AERoom.W2L1Zanzibar.value,
                        lambda state: TJ_Mushroom(state, player) and CanHitMultiple(state, player))
        connect_regions(world, player, AERoom.W2L1Mushroom.value, AERoom.W2L1Alphonse.value,
                        lambda state: TJ_Mushroom(state, player) and CanHitMultiple(state, player))
        connect_regions(world, player, AERoom.W2L1Fish.value, AERoom.W2L1Maki.value,
                        lambda state: TJ_FishEntry(state, player) and (
                                HasSling(state, player) or HasFlyer(state, player)))
        connect_regions(world, player, AERoom.W2L1Fish.value, AERoom.W2L1Herb.value,
                        lambda state: TJ_FishEntry(state, player))
        connect_regions(world, player, AERoom.W2L1Fish.value, AERoom.W2L1Dilweed.value,
                        lambda state: (TJ_FishEntry(state, player) and CanHitMultiple(state, player)) or (
                                TJ_UFOEntry(state, player) and TJ_UFOCliff(state, player)))
        connect_regions(world, player, AERoom.W2L1Tent.value, AERoom.W2L1Stoddy.value,
                        lambda state: (TJ_FishEntry(state, player) and CanHitMultiple(state, player)) or (
                                TJ_UFOEntry(state, player) and TJ_UFOCliff(state, player)))
        connect_regions(world, player, AERoom.W2L1Tent.value, AERoom.W2L1Mitong.value,
                        lambda state: (TJ_FishEntry(state, player) and CanHitMultiple(state, player)) or (
                                TJ_UFOEntry(state, player) and TJ_UFOCliff(state, player)))
        connect_regions(world, player, AERoom.W2L1Tent.value, AERoom.W2L1Nasus.value, lambda state: ((TJ_FishEntry(
            state, player) or (TJ_UFOEntry(state, player) and TJ_UFOCliff(state, player))) and CanHitMultiple(state,
                                                                                                              player)))
        connect_regions(world, player, AERoom.W2L1Boulder.value, AERoom.W2L1Elehcim.value, lambda state: (
                TJ_UFOEntry(state, player) or (TJ_FishEntry(state, player)) and CanHitMultiple(state, player)))
        connect_regions(world, player, AERoom.W2L1Boulder.value, AERoom.W2L1Selur.value, lambda state: (
                (TJ_UFOEntry(state, player) and TJ_UFOCliff(state, player)) or (TJ_FishEntry(state, player))
                and CanHitMultiple(state, player)) and (HasClub(state, player) or HasSling(state, player)
                                                        or HasFlyer(state, player)))

        # 2-2
        connect_regions(world, player, AEWorld.W2.value, AERoom.W2L2Outside.value, lambda state: True)
        connect_regions(world, player, AERoom.W2L2Outside.value, AERoom.W2L2Fan.value, lambda state: True)
        connect_regions(world, player, AERoom.W2L2Outside.value, AERoom.W2L2Obelisk.value, lambda state: True)
        connect_regions(world, player, AERoom.W2L2Outside.value, AERoom.W2L2Water.value, lambda state: True)

        connect_regions(world, player, AERoom.W2L2Outside.value, AERoom.W2L2Kyle.value,
                        lambda state: CanHitOnce(state, player))
        connect_regions(world, player, AERoom.W2L2Outside.value, AERoom.W2L2Stan.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W2L2Outside.value, AERoom.W2L2Kenny.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W2L2Outside.value, AERoom.W2L2Cratman.value,
                        lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W2L2Outside.value, AERoom.W2L2Mooshy.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W2L2Fan.value, AERoom.W2L2Nuzzy.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W2L2Fan.value, AERoom.W2L2Mav.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W2L2Obelisk.value, AERoom.W2L2Papou.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W2L2Obelisk.value, AERoom.W2L2Trance.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W2L2Obelisk.value, AERoom.W2L2Bernt.value,
                        lambda state: HasSling(state, player) or HasPunch(state, player))
        connect_regions(world, player, AERoom.W2L2Water.value, AERoom.W2L2Runt.value,
                        lambda state: (CanSwim(state, player) and CanHitOnce(state, player)) or HasSling(state, player)
                        or HasHoop(state, player))
        connect_regions(world, player, AERoom.W2L2Water.value, AERoom.W2L2Hoolah.value,
                        lambda state: CanHitMultiple(state, player))
        connect_regions(world, player, AERoom.W2L2Water.value, AERoom.W2L2Chino.value,
                        lambda state: (CanSwim(state, player) and CanHitOnce(state, player)) or HasSling(state, player)
                        or HasHoop(state, player))

        #2-3
        connect_regions(world, player, AEWorld.W2.value, AERoom.W2L3Outside.value, lambda state: True)
        connect_regions(world, player, AERoom.W2L3Outside.value, AERoom.W2L3Side.value, lambda state: True)
        connect_regions(world, player, AERoom.W2L3Outside.value, AERoom.W2L3Main.value, lambda state: True)
        connect_regions(world, player, AERoom.W2L3Main.value, AERoom.W2L3Pillar.value, lambda state: True)

        connect_regions(world, player, AERoom.W2L3Outside.value, AERoom.W2L3Bazzle.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W2L3Outside.value, AERoom.W2L3Freeto.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W2L3Side.value, AERoom.W2L3Troopa.value,
                        lambda state: (HasSling(state, player) or HasHoop(state, player) or HasFlyer(state, player)))
        connect_regions(world, player, AERoom.W2L3Main.value, AERoom.W2L3Stymie.value,
                        lambda state: CR_Inside(state, player))
        connect_regions(world, player, AERoom.W2L3Main.value, AERoom.W2L3Spanky.value,
                        lambda state: CR_Inside(state, player) and (
                                (CanSwim(state, player) and CanHitMultiple(state, player)) or HasSling(state, player)
                                or HasFlyer(state, player)))
        connect_regions(world, player, AERoom.W2L3Main.value, AERoom.W2L3Jesta.value,
                        lambda state: CR_Inside(state, player) and (CanHitMultiple(state, player) or (
                                CanSwim(state, player) and HasMobility(state, player))))
        connect_regions(world, player, AERoom.W2L3Pillar.value, AERoom.W2L3Pally.value,
                        lambda state: CR_Inside(state, player))
        connect_regions(world, player, AERoom.W2L3Pillar.value, AERoom.W2L3Crash.value,
                        lambda state: CR_Inside(state, player) and RCMonkey(state, player))

        # 4-1
        connect_regions(world, player, AEWorld.W4.value, AERoom.W4L1FirstRoom.value, lambda state: True)
        connect_regions(world, player, AERoom.W4L1FirstRoom.value, AERoom.W4L1SecondRoom.value, lambda state: True)

        connect_regions(world, player, AERoom.W4L1FirstRoom.value, AERoom.W4L1CoolBlue.value,
                        lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W4L1FirstRoom.value, AERoom.W4L1Sandy.value,
                        lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W4L1FirstRoom.value, AERoom.W4L1ShellE.value,
                        lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W4L1FirstRoom.value, AERoom.W4L1Gidget.value,
                        lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W4L1SecondRoom.value, AERoom.W4L1Shaka.value,
                        lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W4L1SecondRoom.value, AERoom.W4L1Puka.value,
                        lambda state: CanHitMultiple(state, player) or HasHoop(state, player)
                        or HasFlyer(state, player))
        connect_regions(world, player, AERoom.W4L1SecondRoom.value, AERoom.W4L1MaxMahalo.value,
                        lambda state: HasHoop(state, player) or HasSling(state, player))
        connect_regions(world, player, AERoom.W4L1SecondRoom.value, AERoom.W4L1Moko.value,
                        lambda state: HasSling(state, player) or HasFlyer(state, player))

        # 4-2
        connect_regions(world, player, AEWorld.W4.value, AERoom.W4L2FirstRoom.value, lambda state: True)
        connect_regions(world, player, AERoom.W4L2FirstRoom.value, AERoom.W4L2SecondRoom.value, lambda state: True)

        connect_regions(world, player, AERoom.W4L2FirstRoom.value, AERoom.W4L2Chip.value,
                        lambda state: CanSwim(state, player))
        connect_regions(world, player, AERoom.W4L2FirstRoom.value, AERoom.W4L2Oreo.value,
                        lambda state: (HasMobility(state, player)))
        connect_regions(world, player, AERoom.W4L2FirstRoom.value, AERoom.W4L2Puddles.value,
                        lambda state: CanDive(state, player) or HasSling(state, player) or (
                                HasHoop(state, player) and HasFlyer(state, player)))
        connect_regions(world, player, AERoom.W4L2FirstRoom.value, AERoom.W4L2Kalama.value,
                        lambda state: (HasMobility(state, player)))
        connect_regions(world, player, AERoom.W4L2SecondRoom.value, AERoom.W4L2Iz.value,
                        lambda state: CanSwim(state, player) or HasSling(state, player))
        connect_regions(world, player, AERoom.W4L2SecondRoom.value, AERoom.W4L2BongBong.value,
                        lambda state: CanSwim(state, player) or HasSling(state, player))
        connect_regions(world, player, AERoom.W4L2SecondRoom.value, AERoom.W4L2Jux.value,
                        lambda state: CanSwim(state, player) or HasSling(state, player))
        connect_regions(world, player, AERoom.W4L2SecondRoom.value, AERoom.W4L2Pickles.value,
                        lambda state: (CanSwim(state, player) and CanHitMultiple(state, player))
                        or HasSling(state, player))

        # 4-3
        connect_regions(world, player, AEWorld.W4.value, AERoom.W4L3Outside.value, lambda state: True)
        connect_regions(world, player, AERoom.W4L3Outside.value, AERoom.W4L3Stomach.value, lambda state: True)
        connect_regions(world, player, AERoom.W4L3Stomach.value, AERoom.W4L3Slide.value, lambda state: True)
        connect_regions(world, player, AERoom.W4L3Slide.value, AERoom.W4L3Gallery.value, lambda state: True)
        connect_regions(world, player, AERoom.W4L3Gallery.value, AERoom.W4L3Tentacle.value, lambda state: True)

        connect_regions(world, player, AERoom.W4L3Outside.value, AERoom.W4L3TonTon.value,
                        lambda state: CanHitOnce(state, player))
        connect_regions(world, player, AERoom.W4L3Outside.value, AERoom.W4L3Stuw.value,
                        lambda state: CanSwim(state, player) or CanHitOnce(state, player))
        connect_regions(world, player, AERoom.W4L3Stomach.value, AERoom.W4L3Mars.value,
                        lambda state: HasRC(state, player))
        connect_regions(world, player, AERoom.W4L3Stomach.value, AERoom.W4L3Murky.value,
                        lambda state: CanHitOnce(state, player))
        connect_regions(world, player, AERoom.W4L3Stomach.value, AERoom.W4L3Horke.value,
                        lambda state: CanHitOnce(state, player) and (
                                CanSwim(state, player) or HasSling(state, player) or HasFlyer(state, player)))
        connect_regions(world, player, AERoom.W4L3Gallery.value, AERoom.W4L3Howeerd.value,
                        lambda state: DI_SecondHalf(state, player) and (
                                HasSling(state, player) or HasFlyer(state, player)))
        connect_regions(world, player, AERoom.W4L3Gallery.value, AERoom.W4L3Robbin.value,
                        lambda state: DI_SecondHalf(state, player) and (
                                HasSling(state, player) or HasFlyer(state, player)))
        connect_regions(world, player, AERoom.W4L3Gallery.value, AERoom.W4L3Jakkee.value,
                        lambda state: DI_SecondHalf(state, player) and DI_Boulders(state, player))
        connect_regions(world, player, AERoom.W4L3Gallery.value, AERoom.W4L3Frederic.value,
                        lambda state: DI_SecondHalf(state, player) and DI_Boulders(state, player))
        connect_regions(world, player, AERoom.W4L3Gallery.value, AERoom.W4L3Baba.value,
                        lambda state: DI_SecondHalf(state, player) and DI_Boulders(state, player))
        connect_regions(world, player, AERoom.W4L3Tentacle.value, AERoom.W4L3Quirck.value,
                        lambda state: DI_SecondHalf(state, player) and DI_Boulders(state, player))

        # 5-1
        connect_regions(world, player, AEWorld.W5.value, AERoom.W5L1Main.value, lambda state: True)

        connect_regions(world, player, AERoom.W5L1Main.value, AERoom.W5L1Popcicle.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W5L1Main.value, AERoom.W5L1Iced.value,
                        lambda state: CanHitOnce(state, player))
        connect_regions(world, player, AERoom.W5L1Main.value, AERoom.W5L1Rickets.value,
                        lambda state: HasSling(state, player) or HasPunch(state, player) or (
                                HasClub(state, player) and HasFlyer(state, player)))
        connect_regions(world, player, AERoom.W5L1Main.value, AERoom.W5L1Skeens.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W5L1Main.value, AERoom.W5L1Chilly.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W5L1Main.value, AERoom.W5L1Denggoy.value, lambda state: NoRequirement())

        # 5-2
        connect_regions(world, player, AEWorld.W5.value, AERoom.W5L2Entry.value, lambda state: True)
        connect_regions(world, player, AERoom.W5L2Caverns.value, AERoom.W5L2Water.value, lambda state: True)
        connect_regions(world, player, AERoom.W5L2Entry.value, AERoom.W5L2Caverns.value, lambda state: True)

        connect_regions(world, player, AERoom.W5L2Entry.value, AERoom.W5L2Storm.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W5L2Entry.value, AERoom.W5L2Qube.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W5L2Water.value, AERoom.W5L2Ranix.value,
                        lambda state: CanSwim(state, player) or HasSling(state, player) or (
                                HasHoop(state, player) and HasFlyer(state, player)))
        connect_regions(world, player, AERoom.W5L2Water.value, AERoom.W5L2Sharpe.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W5L2Water.value, AERoom.W5L2Sticky.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W5L2Water.value, AERoom.W5L2Droog.value,
                        lambda state: CanDive(state, player) or HasFlyer(state, player) or HasSling(state, player))
        connect_regions(world, player, AERoom.W5L2Caverns.value, AERoom.W5L2Gash.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W5L2Caverns.value, AERoom.W5L2Kundra.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W5L2Caverns.value, AERoom.W5L2Shadow.value, lambda state: NoRequirement())

        # 5-3
        connect_regions(world, player, AEWorld.W5.value, AERoom.W5L3Outside.value, lambda state: True)
        connect_regions(world, player, AERoom.W5L3Outside.value, AERoom.W5L3Spring.value, lambda state: True)
        connect_regions(world, player, AERoom.W5L3Outside.value, AERoom.W5L3Cave.value, lambda state: True)

        connect_regions(world, player, AERoom.W5L3Outside.value, AERoom.W5L3Punky.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W5L3Outside.value, AERoom.W5L3Ameego.value,
                        lambda state: CanDive(state, player))
        connect_regions(world, player, AERoom.W5L3Outside.value, AERoom.W5L3Yoky.value,
                        lambda state: HasSling(state, player) or HasFlyer(state, player))
        connect_regions(world, player, AERoom.W5L3Outside.value, AERoom.W5L3Jory.value,
                        lambda state: HasSling(state, player) or HasFlyer(state, player))
        connect_regions(world, player, AERoom.W5L3Spring.value, AERoom.W5L3Crank.value,
                        lambda state: HasSling(state, player) or HasFlyer(state, player))
        connect_regions(world, player, AERoom.W5L3Spring.value, AERoom.W5L3Claxter.value,
                        lambda state: HasSling(state, player) or HasFlyer(state, player))
        connect_regions(world, player, AERoom.W5L3Spring.value, AERoom.W5L3Looza.value,
                        lambda state: HasSling(state, player) or HasFlyer(state, player))
        connect_regions(world, player, AERoom.W5L3Cave.value, AERoom.W5L3Roti.value,
                        lambda state: CanHitOnce(state, player))
        connect_regions(world, player, AERoom.W5L3Cave.value, AERoom.W5L3Dissa.value,
                        lambda state: CanHitOnce(state, player))

        # 7-1
        connect_regions(world, player, AEWorld.W7.value, AERoom.W7L1Outside.value, lambda state: True)
        connect_regions(world, player, AERoom.W7L1Outside.value, AERoom.W7L1Temple.value, lambda state: True)
        connect_regions(world, player, AERoom.W7L1Outside.value, AERoom.W7L1Well.value, lambda state: True)

        connect_regions(world, player, AERoom.W7L1Outside.value, AERoom.W7L1Taku.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W7L1Outside.value, AERoom.W7L1Rocka.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W7L1Outside.value, AERoom.W7L1Maralea.value,
                        lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W7L1Outside.value, AERoom.W7L1Wog.value,
                        lambda state: HasClub(state, player) or HasSling(state, player) or HasFlyer(state, player))
        connect_regions(world, player, AERoom.W7L1Temple.value, AERoom.W7L1Mayi.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W7L1Temple.value, AERoom.W7L1Owyang.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W7L1Temple.value, AERoom.W7L1Long.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W7L1Temple.value, AERoom.W7L1Elly.value,
                        lambda state: HasSling(state, player) or HasFlyer(state, player))
        connect_regions(world, player, AERoom.W7L1Temple.value, AERoom.W7L1Chunky.value,
                        lambda state: HasSling(state, player) or HasFlyer(state, player))
        connect_regions(world, player, AERoom.W7L1Well.value, AERoom.W7L1Voti.value,
                        lambda state: HasSling(state, player) or (HasHoop(state, player) and HasFlyer(state, player)))
        connect_regions(world, player, AERoom.W7L1Well.value, AERoom.W7L1QuelTin.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W7L1Well.value, AERoom.W7L1Phaldo.value, lambda state: NoRequirement())

        # 7-2
        connect_regions(world, player, AEWorld.W7.value, AERoom.W7L2First.value, lambda state: True)
        connect_regions(world, player, AERoom.W7L2First.value, AERoom.W7L2Gong.value, lambda state: True)
        connect_regions(world, player, AERoom.W7L2Gong.value, AERoom.W7L2Middle.value, lambda state: True)
        connect_regions(world, player, AERoom.W7L2Middle.value, AERoom.W7L2Course.value, lambda state: True)
        connect_regions(world, player, AERoom.W7L2Course.value, AERoom.W7L2Barrel.value, lambda state: True)

        connect_regions(world, player, AERoom.W7L2First.value, AERoom.W7L2Minky.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W7L2First.value, AERoom.W7L2Zobbro.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W7L2Gong.value, AERoom.W7L2Xeeto.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W7L2Gong.value, AERoom.W7L2Moops.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W7L2Gong.value, AERoom.W7L2Zanabi.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W7L2Middle.value, AERoom.W7L2Doxs.value,
                        lambda state: WSW_ThirdRoom(state, player))
        connect_regions(world, player, AERoom.W7L2Course.value, AERoom.W7L2Buddha.value,
                        lambda state: WSW_ThirdRoom(state, player) and WSW_FourthRoom(state, player))
        connect_regions(world, player, AERoom.W7L2Course.value, AERoom.W7L2Fooey.value,
                        lambda state: WSW_ThirdRoom(state, player) and RCMonkey(state, player))
        connect_regions(world, player, AERoom.W7L2Barrel.value, AERoom.W7L2Kong.value,
                        lambda state: WSW_ThirdRoom(state, player) and WSW_FourthRoom(state, player) and (
                                HasSling(state, player) or HasHoop(state, player)))
        connect_regions(world, player, AERoom.W7L2Barrel.value, AERoom.W7L2Phool.value,
                        lambda state: WSW_ThirdRoom(state, player) and WSW_FourthRoom(state, player) and (
                                HasSling(state, player) or HasHoop(state, player) or HasFlyer(state, player)))

        # 7-3
        connect_regions(world, player, AEWorld.W7.value, AERoom.W7L3Outside.value, lambda state: True)
        connect_regions(world, player, AERoom.W7L3Outside.value, AERoom.W7L3Castle.value, lambda state: True)
        connect_regions(world, player, AERoom.W7L3Castle.value, AERoom.W7L3Basement.value, lambda state: True)
        connect_regions(world, player, AERoom.W7L3Elevator.value, AERoom.W7L3Button.value, lambda state: True)
        connect_regions(world, player, AERoom.W7L3Castle.value, AERoom.W7L3Elevator.value, lambda state: True)
        connect_regions(world, player, AERoom.W7L3Castle.value, AERoom.W7L3Bell.value, lambda state: True)

        connect_regions(world, player, AERoom.W7L3Outside.value, AERoom.W7L3Robart.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W7L3Outside.value, AERoom.W7L3Igor.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W7L3Outside.value, AERoom.W7L3Naners.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W7L3Outside.value, AERoom.W7L3Neeners.value,
                        lambda state: CC_5Monkeys(state, player))
        connect_regions(world, player, AERoom.W7L3Outside.value, AERoom.W7L3Charles.value,
                        lambda state: HasPunch(state, player))
        connect_regions(world, player, AERoom.W7L3Castle.value, AERoom.W7L3Gustav.value,
                        lambda state: CC_5Monkeys(state, player))
        connect_regions(world, player, AERoom.W7L3Castle.value, AERoom.W7L3Wilhelm.value,
                        lambda state: CC_5Monkeys(state, player))
        connect_regions(world, player, AERoom.W7L3Castle.value, AERoom.W7L3Emmanuel.value,
                        lambda state: CC_5Monkeys(state, player))
        connect_regions(world, player, AERoom.W7L3Castle.value, AERoom.W7L3SirCutty.value,
                        lambda state: CC_5Monkeys(state, player))
        connect_regions(world, player, AERoom.W7L3Basement.value, AERoom.W7L3Calligan.value,
                        lambda state: CC_WaterRoom(state, player) and (
                                CanDive(state, player) or HasPunch(state, player)))
        connect_regions(world, player, AERoom.W7L3Basement.value, AERoom.W7L3Castalist.value,
                        lambda state: CC_WaterRoom(state, player) and CanDive(state, player))
        connect_regions(world, player, AERoom.W7L3Basement.value, AERoom.W7L3Deveneom.value,
                        lambda state: CC_WaterRoom(state, player))
        connect_regions(world, player, AERoom.W7L3Button.value, AERoom.W7L3Astur.value,
                        lambda state: CC_ButtonRoom(state, player))
        connect_regions(world, player, AERoom.W7L3Button.value, AERoom.W7L3Kilserack.value,
                        lambda state: CC_ButtonRoom(state, player))
        connect_regions(world, player, AERoom.W7L3Elevator.value, AERoom.W7L3Ringo.value,
                        lambda state: CC_5Monkeys(state, player))
        connect_regions(world, player, AERoom.W7L3Elevator.value, AERoom.W7L3Densil.value,
                        lambda state: CC_5Monkeys(state, player))
        connect_regions(world, player, AERoom.W7L3Elevator.value, AERoom.W7L3Figero.value,
                        lambda state: CC_5Monkeys(state, player))
        connect_regions(world, player, AERoom.W7L3Bell.value, AERoom.W7L3Fej.value,
                        lambda state: CC_5Monkeys(state, player))
        connect_regions(world, player, AERoom.W7L3Bell.value, AERoom.W7L3Joey.value,
                        lambda state: HasMobility(state, player))
        connect_regions(world, player, AERoom.W7L3Bell.value, AERoom.W7L3Donqui.value, lambda state: NoRequirement())

        # 8-1
        connect_regions(world, player, AEWorld.W8.value, AERoom.W8L1Outside.value, lambda state: True)
        connect_regions(world, player, AERoom.W8L1Outside.value, AERoom.W8L1Sewers.value, lambda state: True)
        connect_regions(world, player, AERoom.W8L1Sewers.value, AERoom.W8L1Barrel.value, lambda state: True)

        connect_regions(world, player, AERoom.W8L1Outside.value, AERoom.W8L1Kaine.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W8L1Outside.value, AERoom.W8L1Jaxx.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W8L1Outside.value, AERoom.W8L1Gehry.value,
                        lambda state: (CP_FrontBarrels(state, player) and CanDive(state, player))
                        or HasSling(state, player) or HasFlyer(state, player))
        connect_regions(world, player, AERoom.W8L1Outside.value, AERoom.W8L1Alcatraz.value,
                        lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W8L1Sewers.value, AERoom.W8L1Tino.value,
                        lambda state: (CP_FrontSewer(state, player) or CP_BackSewer(state, player))
                        and HasRC(state, player))
        connect_regions(world, player, AERoom.W8L1Sewers.value, AERoom.W8L1QBee.value,
                        lambda state: (CP_FrontSewer(state, player) and HasRC(state, player))
                        or CP_BackSewer(state, player))
        connect_regions(world, player, AERoom.W8L1Sewers.value, AERoom.W8L1McManic.value,
                        lambda state: ((CP_FrontSewer(state, player) or CP_BackSewer(state, player))
                                       and HasRC(state, player)) or HasSling(state,player) or HasFlyer(state, player))
        connect_regions(world, player, AERoom.W8L1Barrel.value, AERoom.W8L1Dywan.value,
                        lambda state: CP_FrontBarrels(state, player) or CP_BackSewer(state, player))
        connect_regions(world, player, AERoom.W8L1Barrel.value, AERoom.W8L1CKHutch.value,
                        lambda state: (CP_FrontBarrels(state, player) or CP_BackSewer(state, player))
                        and CanDive(state, player))
        connect_regions(world, player, AERoom.W8L1Barrel.value, AERoom.W8L1Winky.value,
                        lambda state: CP_FrontBarrels(state, player) or CP_BackSewer(state, player))
        connect_regions(world, player, AERoom.W8L1Barrel.value, AERoom.W8L1BLuv.value,
                        lambda state: (CP_FrontBarrels(state, player) and (CanSwim(state, player)
                                                                           or HasSling(state, player)
                                                                           or HasFlyer(state, player)))
                        or CP_BackSewer(state, player))
        connect_regions(world, player, AERoom.W8L1Barrel.value, AERoom.W8L1Camper.value,
                        lambda state: ((CP_FrontBarrels(state, player) or CP_BackSewer(state, player))
                                       and CanDive(state, player)) or (HasSling(state, player)
                                                                       and HasRC(state, player)))
        connect_regions(world, player, AERoom.W8L1Barrel.value, AERoom.W8L1Huener.value,
                        lambda state: (CP_FrontBarrels(state, player)
                                       and (HasHoop(state, player) or CanSwim(state, player))
                                       and HasFlyer(state, player)) or CP_BackSewer(state, player)
                        or HasSling(state, player))

        # 8-2
        connect_regions(world, player, AEWorld.W8.value, AERoom.W8L2Outside.value, lambda state: True)
        connect_regions(world, player, AERoom.W8L2Outside.value, AERoom.W8L2Factory.value, lambda state: True)
        connect_regions(world, player, AERoom.W8L2Factory.value, AERoom.W8L2RC.value, lambda state: True)
        connect_regions(world, player, AERoom.W8L2Mech.value, AERoom.W8L2Lava.value, lambda state: True)
        connect_regions(world, player, AERoom.W8L2Lava.value, AERoom.W8L2Conveyor.value, lambda state: True)
        connect_regions(world, player, AERoom.W8L2Factory.value, AERoom.W8L2Mech.value, lambda state: True)

        connect_regions(world, player, AERoom.W8L2Outside.value, AERoom.W8L2BigShow.value,
                        lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W8L2Outside.value, AERoom.W8L2Dreos.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W8L2Factory.value, AERoom.W8L2Reznor.value,
                        lambda state: SF_MechRoom(state, player))
        connect_regions(world, player, AERoom.W8L2RC.value, AERoom.W8L2Urkel.value,
                        lambda state: SF_CarRoom(state, player))
        connect_regions(world, player, AERoom.W8L2Lava.value, AERoom.W8L2VanillaS.value,
                        lambda state: SF_MechRoom(state, player) and HasPunch(state, player))
        connect_regions(world, player, AERoom.W8L2Lava.value, AERoom.W8L2Radd.value,
                        lambda state: SF_MechRoom(state, player))
        connect_regions(world, player, AERoom.W8L2Lava.value, AERoom.W8L2Shimbo.value,
                        lambda state: SF_MechRoom(state, player) and RCMonkey(state, player))
        connect_regions(world, player, AERoom.W8L2Conveyor.value, AERoom.W8L2Hurt.value,
                        lambda state: SF_MechRoom(state, player) and CanHitMultiple(state, player))
        connect_regions(world, player, AERoom.W8L2Conveyor.value, AERoom.W8L2String.value,
                        lambda state: SF_MechRoom(state, player))
        connect_regions(world, player, AERoom.W8L2Mech.value, AERoom.W8L2Khamo.value,
                        lambda state: SF_MechRoom(state, player) and CanHitMultiple(state, player))

        # 8-3
        connect_regions(world, player, AEWorld.W8.value, AERoom.W8L3Outside.value, lambda state: True)
        connect_regions(world, player, AERoom.W8L3Lobby.value, AERoom.W8L3Water.value, lambda state: True)
        connect_regions(world, player, AERoom.W8L3Outside.value, AERoom.W8L3Lobby.value, lambda state: True)
        connect_regions(world, player, AERoom.W8L3Lobby.value, AERoom.W8L3Tank.value, lambda state: True)
        connect_regions(world, player, AERoom.W8L3Tank.value, AERoom.W8L3Fan.value, lambda state: True)

        connect_regions(world, player, AERoom.W8L3Outside.value, AERoom.W8L3Fredo.value,
                        lambda state: HasPunch(state, player))
        connect_regions(world, player, AERoom.W8L3Water.value, AERoom.W8L3Charlee.value,
                        lambda state: TVT_HitButton(state, player))
        connect_regions(world, player, AERoom.W8L3Water.value, AERoom.W8L3Mach3.value,
                        lambda state: TVT_HitButton(state, player))
        connect_regions(world, player, AERoom.W8L3Lobby.value, AERoom.W8L3Tortuss.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W8L3Lobby.value, AERoom.W8L3Manic.value,
                        lambda state: HasSling(state, player) or HasFlyer(state, player))
        connect_regions(world, player, AERoom.W8L3Tank.value, AERoom.W8L3Ruptdis.value,
                        lambda state: TVT_TankRoom(state, player))
        connect_regions(world, player, AERoom.W8L3Tank.value, AERoom.W8L3Eighty7.value,
                        lambda state: TVT_TankRoom(state, player))
        connect_regions(world, player, AERoom.W8L3Tank.value, AERoom.W8L3Danio.value,
                        lambda state: TVT_TankRoom(state, player))
        connect_regions(world, player, AERoom.W8L3Fan.value, AERoom.W8L3Roosta.value,
                        lambda state: TVT_TankRoom(state, player))
        connect_regions(world, player, AERoom.W8L3Fan.value, AERoom.W8L3Tellis.value,
                        lambda state: TVT_TankRoom(state, player))
        connect_regions(world, player, AERoom.W8L3Fan.value, AERoom.W8L3Whack.value,
                        lambda state: TVT_TankRoom(state, player))
        connect_regions(world, player, AERoom.W8L3Fan.value, AERoom.W8L3Frostee.value,
                        lambda state: TVT_TankRoom(state, player))

        # 9-1
        connect_regions(world, player, AEWorld.W9.value, AERoom.W9L1Entry.value, lambda state: True)
        connect_regions(world, player, AERoom.W9L1Entry.value, AERoom.W9L1Haunted.value, lambda state: True)
        connect_regions(world, player, AERoom.W9L1Haunted.value, AERoom.W9L1Coffin.value, lambda state: True)
        connect_regions(world, player, AERoom.W9L1Coffin.value, AERoom.W9L1Natalie.value,
                        lambda state: MM_Natalie(state, player))
        connect_regions(world, player, AERoom.W9L1Entry.value, AERoom.W9L1Professor.value,
                        lambda state: MM_Professor(state, player))
        connect_regions(world, player, AERoom.W9L1Entry.value, AERoom.W9L1Jake.value,
                        lambda state: MM_Jake(state, player))
        connect_regions(world, player, AERoom.W9L1Entry.value, AERoom.W9L1Western.value, lambda state: True)
        connect_regions(world, player, AERoom.W9L1Entry.value, AERoom.W9L1Crater.value, lambda state: True)
        connect_regions(world, player, AERoom.W9L1Crater.value, AERoom.W9L1Outside.value, lambda state: True)
        connect_regions(world, player, AERoom.W9L1Outside.value, AERoom.W9L1Castle.value, lambda state: True)
        connect_regions(world, player, AERoom.W9L1Castle.value, AERoom.W9L1Climb1.value, lambda state: True)
        connect_regions(world, player, AERoom.W9L1Climb1.value, AERoom.W9L1Climb2.value, lambda state: True)
        connect_regions(world, player, AERoom.W9L1Castle.value, AERoom.W9L1Head.value, lambda state: True)
        connect_regions(world, player, AERoom.W9L1Outside.value, AERoom.W9L1Side.value, lambda state: True)
        connect_regions(world, player, AERoom.W9L1Castle.value, AERoom.W9L1Boss.value,
                        lambda state: MM_FinalBoss(state, player))

        connect_regions(world, player, AERoom.W9L1Entry.value, AERoom.W9L1Goopo.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W9L1Haunted.value, AERoom.W9L1Porto.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W9L1Coffin.value, AERoom.W9L1Slam.value,
                        lambda state: CanHitOnce(state, player))
        connect_regions(world, player, AERoom.W9L1Coffin.value, AERoom.W9L1Junk.value,
                        lambda state: CanHitOnce(state, player))
        connect_regions(world, player, AERoom.W9L1Coffin.value, AERoom.W9L1Crib.value,
                        lambda state: CanHitOnce(state, player))
        connect_regions(world, player, AERoom.W9L1Western.value, AERoom.W9L1Nak.value,
                        lambda state: HasSling(state, player) or HasHoop(state, player))
        connect_regions(world, player, AERoom.W9L1Western.value, AERoom.W9L1Cloy.value, lambda state: NoRequirement())
        connect_regions(world, player, AERoom.W9L1Western.value, AERoom.W9L1Shaw.value,
                        lambda state: HasSling(state, player) or HasHoop(state, player))
        connect_regions(world, player, AERoom.W9L1Western.value, AERoom.W9L1Flea.value,
                        lambda state: HasSling(state, player) or HasHoop(state, player))
        connect_regions(world, player, AERoom.W9L1Crater.value, AERoom.W9L1Schafette.value,
                        lambda state: MM_SHA(state, player) and HasFlyer(state, player))
        connect_regions(world, player, AERoom.W9L1Outside.value, AERoom.W9L1Donovan.value,
                        lambda state: MM_UFODoor(state, player))
        connect_regions(world, player, AERoom.W9L1Outside.value, AERoom.W9L1Laura.value,
                        lambda state: MM_UFODoor(state, player))
        connect_regions(world, player, AERoom.W9L1Castle.value, AERoom.W9L1Uribe.value,
                        lambda state: MM_UFODoor(state, player) and HasPunch(state, player))
        connect_regions(world, player, AERoom.W9L1Castle.value, AERoom.W9L1Gordo.value,
                        lambda state: MM_UFODoor(state, player) and (HasFlyer(state, player) or HasRC(state, player)))
        connect_regions(world, player, AERoom.W9L1Castle.value, AERoom.W9L1Raeski.value,
                        lambda state: MM_UFODoor(state, player))
        connect_regions(world, player, AERoom.W9L1Castle.value, AERoom.W9L1Poopie.value,
                        lambda state: MM_UFODoor(state, player))
        connect_regions(world, player, AERoom.W9L1Climb1.value, AERoom.W9L1Teacup.value,
                        lambda state: MM_DoubleDoor(state, player))
        connect_regions(world, player, AERoom.W9L1Climb1.value, AERoom.W9L1Shine.value,
                        lambda state: MM_DoubleDoor(state, player))
        connect_regions(world, player, AERoom.W9L1Climb2.value, AERoom.W9L1Wrench.value,
                        lambda state: MM_SpaceMonkeys(state, player))
        connect_regions(world, player, AERoom.W9L1Climb2.value, AERoom.W9L1Bronson.value,
                        lambda state: MM_SpaceMonkeys(state, player))
        connect_regions(world, player, AERoom.W9L1Head.value, AERoom.W9L1Bungee.value,
                        lambda state: MM_DoubleDoor(state, player))
        connect_regions(world, player, AERoom.W9L1Head.value, AERoom.W9L1Carro.value,
                        lambda state: MM_DoubleDoor(state, player))
        connect_regions(world, player, AERoom.W9L1Head.value, AERoom.W9L1Carlito.value,
                        lambda state: MM_DoubleDoor(state, player))
        connect_regions(world, player, AERoom.W9L1Side.value, AERoom.W9L1BG.value,
                        lambda state: MM_SHA(state, player) and (HasSling(state, player) or HasFlyer(state, player)))

        world.completion_condition[player] = lambda state: state.has("Victory", player, 1)

        if coins:
            # Coins
            # 1-1
            connect_regions(world, player, AERoom.W1L1Main.value, AERoom.Coin1.value, lambda state: NoRequirement())
            # 1-2
            connect_regions(world, player, AERoom.W1L2Main.value, AERoom.Coin2.value,
                            lambda state: CanDive(state, player))
            # 1-3
            connect_regions(world, player, AERoom.W1L3Entry.value, AERoom.Coin3.value, lambda state: NoRequirement())
            # 2-1
            connect_regions(world, player, AERoom.W2L1Entry.value, AERoom.Coin6.value,
                            lambda state: HasMobility(state, player))
            connect_regions(world, player, AERoom.W2L1Mushroom.value, AERoom.Coin7.value,
                            lambda state: TJ_Mushroom(state, player) and CanHitMultiple(state, player))
            connect_regions(world, player, AERoom.W2L1Fish.value, AERoom.Coin8.value,
                            lambda state: (TJ_FishEntry(state, player)))
            connect_regions(world, player, AERoom.W2L1Tent.value, AERoom.Coin9.value,
                            lambda state: (TJ_FishEntry(state, player) and CanHitMultiple(state, player)) or (
                                    (TJ_UFOEntry(state, player)) and (TJ_UFOCliff(state, player))))
            # 2-2
            connect_regions(world, player, AERoom.W2L2Outside.value, AERoom.Coin11.value, lambda state: NoRequirement())
            connect_regions(world, player, AERoom.W2L2Fan.value, AERoom.Coin12.value, lambda state: NoRequirement())
            connect_regions(world, player, AERoom.W2L2Obelisk.value, AERoom.Coin13.value,
                            lambda state: HasRC(state, player) or HasPunch(state, player))
            connect_regions(world, player, AERoom.W2L2Water.value, AERoom.Coin14.value,
                            lambda state: (CanDive(state, player)) and (
                                    (CanHitOnce(state, player)) or (HasFlyer(state, player))))
            # 2-3
            connect_regions(world, player, AERoom.W2L3Main.value, AERoom.Coin17.value,
                            lambda state: (CR_Inside(state, player)) and (
                                    (CanHitMultiple(state, player)) and (CanSwim(state, player))) or (
                                              HasMobility(state, player)))
            # 3-1
            connect_regions(world, player, AEWorld.W3.value, AERoom.Coin19.value, lambda state: NoRequirement())

            # 4-1
            connect_regions(world, player, AERoom.W4L1SecondRoom.value, AERoom.Coin21.value,
                            lambda state: NoRequirement())

            # 4-2
            connect_regions(world, player, AERoom.W4L2SecondRoom.value, AERoom.Coin23.value,
                            lambda state: CanDive(state, player))

            # 4-3
            connect_regions(world, player, AERoom.W4L3Outside.value, AERoom.Coin24.value,
                            lambda state: CanSwim(state, player) or CanHitOnce(state, player))
            connect_regions(world, player, AERoom.W4L3Stomach.value, AERoom.Coin25.value,
                            lambda state: CanDive(state, player) and CanHitOnce(state, player))
            connect_regions(world, player, AERoom.W4L3Slide.value, AERoom.Coin28.value,
                            lambda state: (CanSwim(state, player)) and (
                                    (CanHitOnce(state, player)) or (HasPunch(state, player))))

            # 5-1
            connect_regions(world, player, AERoom.W5L1Main.value, AERoom.Coin29.value,
                            lambda state: NoRequirement())

            # 5-2
            connect_regions(world, player, AERoom.W5L2Entry.value, AERoom.Coin30.value,
                            lambda state: HasFlyer(state, player))
            connect_regions(world, player, AERoom.W5L2Water.value, AERoom.Coin31.value,
                            lambda state: HasFlyer(state, player) and CanDive(state, player))
            connect_regions(world, player, AERoom.W5L2Caverns.value, AERoom.Coin32.value,
                            lambda state: HasFlyer(state, player))

            # 5-3
            connect_regions(world, player, AERoom.W5L3Spring.value, AERoom.Coin34.value,
                            lambda state: HasFlyer(state, player))
            connect_regions(world, player, AERoom.W5L3Cave.value, AERoom.Coin35.value,
                            lambda state: CanHitMultiple(state, player))

            # 6-1
            connect_regions(world, player, AEWorld.W6.value, AERoom.Coin36.value, lambda state: HasFlyer(state, player))

            # 7-1
            connect_regions(world, player, AERoom.W7L1Outside.value, AERoom.Coin37.value,
                            lambda state: NoRequirement())
            connect_regions(world, player, AERoom.W7L1Temple.value, AERoom.Coin38.value,
                            lambda state: NoRequirement())
            connect_regions(world, player, AERoom.W7L1Well.value, AERoom.Coin39.value,
                            lambda state: HasFlyer(state, player))

            # 7-2
            connect_regions(world, player, AERoom.W7L2First.value, AERoom.Coin40.value,
                            lambda state: NoRequirement())
            connect_regions(world, player, AERoom.W7L2Gong.value, AERoom.Coin41.value,
                            lambda state: NoRequirement())
            connect_regions(world, player, AERoom.W7L2Barrel.value, AERoom.Coin43.value,
                            lambda state: HasFlyer(state, player))

            # 7-3
            connect_regions(world, player, AERoom.W7L3Outside.value, AERoom.Coin45.value,
                            lambda state: HasClub(state, player) or HasFlyer(state, player) or HasPunch(state, player))
            connect_regions(world, player, AERoom.W7L3Castle.value, AERoom.Coin46.value,
                            lambda state: CC_5Monkeys(state, player))
            connect_regions(world, player, AERoom.W7L3Button.value, AERoom.Coin49.value,
                            lambda state: CC_ButtonRoom(state, player))
            connect_regions(world, player, AERoom.W7L3Elevator.value, AERoom.Coin50.value,
                            lambda state: CC_5Monkeys(state, player) or CC_WaterRoom(state, player))

            # 8-1
            connect_regions(world, player, AERoom.W8L1Outside.value, AERoom.Coin53.value,
                            lambda state: CP_FrontBarrels(state, player) and CanDive(state, player)
                            and HasFlyer(state,player))
            connect_regions(world, player, AERoom.W8L1Sewers.value, AERoom.Coin54.value,
                            lambda state: CP_FrontSewer(state, player) and HasRC(state, player))
            connect_regions(world, player, AERoom.W8L1Barrel.value, AERoom.Coin55.value,
                            lambda state: CP_FrontBarrels(state, player) and HasFlyer(state, player))

            # 8-2
            connect_regions(world, player, AERoom.W8L2RC.value, AERoom.Coin58.value,
                            lambda state: SF_CarRoom(state, player))
            connect_regions(world, player, AERoom.W8L2Lava.value, AERoom.Coin62.value,
                            lambda state: SF_MechRoom(state, player))

            # 8-3
            connect_regions(world, player, AERoom.W8L3Water.value, AERoom.Coin64.value,
                            lambda state: HasFlyer(state, player))
            connect_regions(world, player, AERoom.W8L3Tank.value, AERoom.Coin66.value,
                            lambda state: TVT_TankRoom(state, player))

            # 9-1
            connect_regions(world, player, AERoom.W9L1Entry.value, AERoom.Coin73.value,
                            lambda state: NoRequirement())
            connect_regions(world, player, AERoom.W9L1Entry.value, AERoom.Coin74.value,
                            lambda state: NoRequirement())
            connect_regions(world, player, AERoom.W9L1Haunted.value, AERoom.Coin75.value,
                            lambda state: HasFlyer(state, player))
            connect_regions(world, player, AERoom.W9L1Western.value, AERoom.Coin77.value,
                            lambda state: NoRequirement())
            connect_regions(world, player, AERoom.W9L1Crater.value, AERoom.Coin78.value,
                            lambda state: MM_SHA(state, player) and HasFlyer(state, player))
            connect_regions(world, player, AERoom.W9L1Outside.value, AERoom.Coin79.value,
                            lambda state: MM_SHA(state, player))
            connect_regions(world, player, AERoom.W9L1Castle.value, AERoom.Coin80.value,
                            lambda state: MM_UFODoor(state, player))
            connect_regions(world, player, AERoom.W9L1Head.value, AERoom.Coin81.value,
                            lambda state: MM_DoubleDoor(state, player))
            connect_regions(world, player, AERoom.W9L1Side.value, AERoom.Coin82.value,
                            lambda state: MM_SHA(state, player) and HasFlyer(state, player))
            connect_regions(world, player, AERoom.W9L1Climb2.value, AERoom.Coin83.value,
                            lambda state: MM_SpaceMonkeys(state, player))


def Keys(state, player, count):
    return state.has(AEItem.Key.value, player, count)


def NoRequirement():
    return True


def CanHitOnce(state, player):
    return HasClub(state, player) or HasRadar(state, player) or HasSling(state, player) or HasHoop(state,player) \
        or HasFlyer(state, player) or HasRC(state, player) or HasPunch(state, player)


def CanHitMultiple(state, player):
    return HasClub(state, player) or HasSling(state, player) or HasHoop(state, player) or HasPunch(state, player)


def HasMobility(state, player):
    return HasSling(state, player) or HasHoop(state, player) or HasFlyer(state, player)


def RCMonkey(state, player):
    return HasSling(state, player) or HasRC(state, player)


def CanSwim(state, player):
    return HasWaterNet(state, player)


def CanDive(state, player):
    return HasWaterNet(state, player)


def CanWaterCatch(state, player):
    return HasWaterNet(state, player)


def TJ_UFOEntry(state, player):
    return CanDive(state, player)


def TJ_UFOCliff(state, player):
    return True


def TJ_FishEntry(state, player):
    return CanSwim(state, player) or HasFlyer(state, player)


def TJ_Mushroom(state, player):
    return HasMobility(state, player)


def CR_Inside(state, player):
    return HasSling(state, player) or HasPunch(state, player)


def DI_SecondHalf(state, player):
    return HasSling(state, player) or (CanHitMultiple(state, player) and CanDive(state, player))


def DI_Boulders(state, player):
    return HasSling(state, player) or HasHoop(state, player) or HasFlyer(state, player) or HasRC(state, player)


def WSW_ThirdRoom(state, player):
    return HasSling(state, player) or HasHoop(state, player) or HasFlyer(state, player)


def WSW_FourthRoom(state, player):
    return True


def CC_5Monkeys(state, player):
    return HasClub(state, player) or HasSling(state, player) or HasHoop(state, player) or HasFlyer(state, player) \
        or HasPunch(state, player)


def CC_WaterRoom(state, player):
    return CanHitMultiple(state, player) or (CanDive(state, player) and (
            HasSling(state, player) or HasFlyer(state, player) or HasPunch(state, player)))


def CC_ButtonRoom(state, player):
    return CC_WaterRoom(state, player) and (CanSwim(state, player) or HasFlyer(state, player))


def CP_FrontSewer(state, player):
    return HasSling(state, player) or HasRC(state, player)


def CP_FrontBarrels(state, player):
    return CP_FrontSewer(state, player) and (CanSwim(state, player) or HasMobility(state, player))


def CP_BackSewer(state, player):
    return (HasSling(state, player) or HasFlyer(state, player)) and CanDive(state, player)


def SF_CarRoom(state, player):
    return HasSling(state, player) or (HasHoop(state, player) and HasFlyer(state, player)) or HasRC(state, player) \
        or HasPunch(state, player)


def SF_MechRoom(state, player):
    return HasSling(state, player) or (HasHoop(state, player) and HasFlyer(state, player)) or (
            HasClub(state, player) and HasRC(state, player)) or HasPunch(state, player)


def TVT_HitButton(state, player):
    return HasClub(state, player) or HasSling(state, player) or HasFlyer(state, player)


def TVT_TankRoom(state, player):
    return TVT_HitButton(state, player)


def MM_Natalie(state, player):
    return CanHitMultiple(state, player)


def MM_Professor(state, player):
    return HasSling(state, player) or (HasFlyer(state, player) and (HasClub(state, player) or HasPunch(state, player)))


def Jake_Open(state, player):
    return MM_Natalie(state, player) and MM_Professor(state, player)


def MM_Jake(state, player):
    return CanHitMultiple(state, player) and (HasSling(state, player) or Jake_Open(state, player))


def MM_SHA(state, player):
    return MM_Natalie(state, player) and MM_Professor(state, player) and MM_Jake(state, player)


def MM_UFODoor(state, player):
    return MM_SHA(state, player) and (HasClub(state, player) or HasSling(state, player) or HasPunch(state, player))


def MM_DoubleDoor(state, player):
    return MM_UFODoor(state, player) and HasHoop(state, player) and HasRC(state, player)


def MM_SpaceMonkeys(state, player):
    return MM_DoubleDoor(state, player) and (HasSling(state, player) or HasFlyer(state, player))


def MM_FinalBoss(state, player):
    return MM_UFODoor(state, player) and HasSling(state, player)


def HasClub(state, player):
    return state.has(AEItem.Club.value, player, 1)


def HasNet(state, player):
    return state.has(AEItem.Net.value, player, 1)


def HasRadar(state, player):
    return state.has(AEItem.Radar.value, player, 1)


def HasSling(state, player):
    return state.has(AEItem.Sling.value, player, 1)


def HasHoop(state, player):
    return state.has(AEItem.Hoop.value, player, 1)


def HasFlyer(state, player):
    return state.has(AEItem.Flyer.value, player, 1)


def HasRC(state, player):
    return state.has(AEItem.Car.value, player, 1)


def HasPunch(state, player):
    return state.has(AEItem.Punch.value, player, 1)


def HasWaterNet(state, player):
    return state.has(AEItem.WaterNet.value, player, 1)
