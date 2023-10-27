import os
import json
from typing import Any, ClassVar, Dict, List, Optional, Set, Tuple

from BaseClasses import Entrance, Item, ItemClassification, MultiWorld, Region, Tutorial, \
    LocationProgressType
from Options import Choice
from worlds.AutoWorld import WebWorld, World
from .Items import item_table, ItemData, nothing_item_id, event_table, ApeEscapeItem
from .Locations import location_table, base_location_id
from .Regions import create_regions
from .Rules import set_rules
from .Client import ApeEscapeClient

from worlds.LauncherComponents import Component, components, SuffixIdentifier

# Adventure
components.append(Component('Ape Escape Client', 'ApeEscapeClient', file_identifier=SuffixIdentifier('.apae')))


class ApeEscapeWeb(WebWorld):
    theme = "dirt"

    setup = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Adventure for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["JusticePS"]
    )

    setup_fr = Tutorial(
        "Guide de configuration Multimonde",
        "Un guide pour configurer Adventure MultiWorld",
        "Français",
        "setup_fr.md",
        "setup/fr",
        ["TheLynk"]
    )

    tutorials = [setup, setup_fr]


class ApeEscapeWorld(World):
    """
    Funni monke game
    """
    game = "Ape Escape"
    web: ClassVar[WebWorld] = ApeEscapeWeb()

    item_name_to_id = item_table

    for key, value in item_name_to_id.items():
        item_name_to_id[key] = value + 128000000

    location_name_to_id = location_table

    for key, value in location_name_to_id.items():
        location_name_to_id[key] = value + 128000000

    def __init__(self, world: MultiWorld, player: int):
        super().__init__(world, player)
        self.game = "Ape Escape"

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

        radar = self.create_item("Monkey Radar")
        shooter = self.create_item("Slingback Shooter")
        hoop = self.create_item("Dash Hoop")
        flyer = self.create_item("Sky Flyer")
        car = self.create_item("R.C. Car")
        punch = self.create_item("Magic Punch")
        victory = self.create_item("Victory")

        self.multiworld.itempool += [radar, shooter, hoop, flyer, car, punch]

        self.multiworld.itempool += [self.create_item("World Key") for i in range(0, 6)]

        self.multiworld.get_location("9-1 Specter", self.player).place_locked_item(victory)

        remaining = 360#(len(location_table) - len(self.multiworld.itempool))-25
        self.multiworld.itempool += [self.create_item_filler("nothing") for i in range(0, remaining)]

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
