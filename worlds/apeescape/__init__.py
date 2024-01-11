import math
import os
import json
from typing import Any, ClassVar, Dict, List, Optional, Set, Tuple

from BaseClasses import Item, ItemClassification, MultiWorld, Tutorial
from worlds.AutoWorld import WebWorld, World
from .Items import item_table, ItemData, nothing_item_id, event_table, ApeEscapeItem
from .Locations import location_table, base_location_id
from .Regions import create_regions
from .Rules import set_rules
from .Client import ApeEscapeClient
from .Strings import AEItem, AELocation
from .RAMAddress import RAM
from .Options import apeescape_option_definitions, DebugOption, GoalOption, LogicOption, CoinOption
from Options import AssembleOptions


class ApeEscapeWeb(WebWorld):
    theme = "dirt"

    setup = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Adventure for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["CDRomatron"]
    )

    tutorials = [setup]


class ApeEscapeWorld(World):
    """
    Funni monke game
    """
    game = "Ape Escape"
    web: ClassVar[WebWorld] = ApeEscapeWeb()
    topology_present = True

    option_definitions: ClassVar[Dict[str, AssembleOptions]] = apeescape_option_definitions

    item_name_to_id = item_table

    for key, value in item_name_to_id.items():
        item_name_to_id[key] = value + 128000000

    location_name_to_id = location_table

    for key, value in location_name_to_id.items():
        location_name_to_id[key] = value + 128000000

    def __init__(self, world: MultiWorld, player: int):
        super().__init__(world, player)
        self.game = "Ape Escape"
        self.debug: Optional[int] = 0
        self.goal: Optional[int] = 0
        self.logic: Optional[int] = 0
        self.coin: Optional[int] = 0

    def generate_early(self) -> None:
        self.goal = self.multiworld.goal[self.player].value
        self.debug = self.multiworld.debug[self.player].value
        self.logic = self.multiworld.logic[self.player].value
        self.coin = self.multiworld.coin[self.player].value

    def create_regions(self):
        create_regions(self.multiworld, self.player)

    def set_rules(self):
        set_rules(self.multiworld, self.player)

    def create_item(self, name: str) -> Item:
        item_id = item_table[name]
        classification = ItemClassification.progression

        item = ApeEscapeItem(name, classification, item_id, self.player)
        return item

    def create_item_filler(self, name: str) -> Item:
        item_id = item_table[name]
        classification = ItemClassification.filler

        item = ApeEscapeItem(name, classification, item_id, self.player)
        return item


    def create_items(self):
        numberoflocations = len(location_table)

        radar = self.create_item(AEItem.Radar.value)
        shooter = self.create_item(AEItem.Sling.value)
        hoop = self.create_item(AEItem.Hoop.value)
        flyer = self.create_item(AEItem.Flyer.value)
        car = self.create_item(AEItem.Car.value)
        punch = self.create_item(AEItem.Punch.value)
        victory = self.create_item(AEItem.Victory.value)

        waternet = self.create_item(AEItem.WaterNet.value)
        club = self.create_item(AEItem.Club.value)
        numberoflocations -= 1

        self.multiworld.push_precollected(waternet)
        self.multiworld.push_precollected(club)

        if self.multiworld.debug[self.player].value == 0x00:
            self.multiworld.itempool += [radar, shooter, hoop, flyer, car, punch]
            self.multiworld.itempool += [self.create_item(AEItem.Key.value) for i in range(0, 6)]
            numberoflocations -= 12
        # DEBUG
        elif self.multiworld.debug[self.player].value == 0x01:
            self.multiworld.get_location(AELocation.Noonan.value, self.player).place_locked_item(radar)
            self.multiworld.get_location(AELocation.Jorjy.value, self.player).place_locked_item(shooter)
            self.multiworld.get_location(AELocation.Nati.value, self.player).place_locked_item(hoop)
            self.multiworld.get_location(AELocation.Shay.value, self.player).place_locked_item(flyer)
            self.multiworld.get_location(AELocation.DrMonk.value, self.player).place_locked_item(car)
            self.multiworld.get_location(AELocation.Ahchoo.value, self.player).place_locked_item(punch)
            self.multiworld.itempool += [self.create_item(AEItem.Key.value) for i in range(0, 6)]
            numberoflocations -= 12
        # DEBUG
        elif self.multiworld.debug[self.player].value == 0x02:
            self.multiworld.itempool += [radar, shooter, hoop, flyer, car, punch]
            key1 = self.create_item("World Key")
            key2 = self.create_item("World Key")
            key3 = self.create_item("World Key")
            key4 = self.create_item("World Key")
            key5 = self.create_item("World Key")
            key6 = self.create_item("World Key")
            self.multiworld.get_location(AELocation.Noonan.value, self.player).place_locked_item(key1)
            self.multiworld.get_location(AELocation.Jorjy.value, self.player).place_locked_item(key2)
            self.multiworld.get_location(AELocation.Nati.value, self.player).place_locked_item(key3)
            self.multiworld.get_location(AELocation.Shay.value, self.player).place_locked_item(key4)
            self.multiworld.get_location(AELocation.DrMonk.value, self.player).place_locked_item(key5)
            self.multiworld.get_location(AELocation.Ahchoo.value, self.player).place_locked_item(key6)
            numberoflocations -= 12


        if self.multiworld.coin[self.player].value == 0x01:
            numberoflocations -= 60



        if self.multiworld.goal[self.player].value == 0x00:
            self.multiworld.get_location(AELocation.Specter.value, self.player).place_locked_item(victory)
            numberoflocations -= 1
        else:
            self.multiworld.get_location(AELocation.Specter2.value, self.player).place_locked_item(victory)

        sixth = math.floor(numberoflocations/6)

        self.multiworld.itempool += [self.create_item_filler(AEItem.Shirt.value) for i in range(0, sixth)]
        numberoflocations -= sixth

        self.multiworld.itempool += [self.create_item_filler(AEItem.Triangle.value) for i in range(0, sixth)]
        numberoflocations -= sixth

        self.multiworld.itempool += [self.create_item_filler(AEItem.BigTriangle.value) for i in range(0, sixth)]
        numberoflocations -= sixth

        self.multiworld.itempool += [self.create_item_filler(AEItem.Cookie.value) for i in range(0, sixth)]
        numberoflocations -= sixth

        self.multiworld.itempool += [self.create_item_filler(AEItem.Flash.value) for i in range(0, sixth)]
        numberoflocations -= sixth

        self.multiworld.itempool += [self.create_item_filler(AEItem.Rocket.value) for i in range(0, sixth)]
        numberoflocations -= sixth

        self.multiworld.itempool += [self.create_item_filler(AEItem.Nothing.value) for i in range(0, numberoflocations)]

    def fill_slot_data(self):
        return {}

    def generate_output(self, output_directory: str):
        if self.multiworld.players != 1:
            return
        data = {
            "slot_data": self.fill_slot_data(),
            "location_to_item": {self.location_name_to_id[i.name]: item_table[i.item.name] for i in
                                 self.multiworld.get_locations()},
            "data_package": {
                "data": {
                    "games": {
                        self.game: {
                            "item_name_to_id": self.item_name_to_id,
                            "location_name_to_id": self.location_name_to_id
                        }
                    }
                }
            }
        }
        filename = f"{self.multiworld.get_out_file_name_base(self.player)}.apae"
        with open(os.path.join(output_directory, filename), 'w') as f:
            json.dump(data, f)
