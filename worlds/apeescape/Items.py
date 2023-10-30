from typing import Optional
from BaseClasses import ItemClassification, Item

base_apeescape_item_id = 128000000


class ApeEscapeItem(Item):
    def __init__(self, name: str, classification: ItemClassification, code: Optional[int], player: int):
        super().__init__(name, classification, code, player)


class ItemData:
    def __init__(self, id: int, classification: ItemClassification):
        self.classification = classification
        self.id = None if id is None else id + base_apeescape_item_id
        self.table_index = id


nothing_item_id = base_apeescape_item_id

# base IDs are the index in the static item data table, which is
# not the same order as the items in RAM (but offset 0 is a 16-bit address of
# location of room and position data)
item_table = {
    #Gadgets
    #"Stun Club": 0x1,
    #"Time Net": 0x2,
    "Monkey Radar": 0x4,
    "Slingback Shooter": 0x8,
    "Super Hoop": 0x10,
    "Magic Punch": 0x20,
    "Sky Flyer": 0x40,
    "R.C. Car": 0x80,


    #Keys
    "World Key": 0x100,

    "Victory": 0x200,

    "nothing": 0x0
}

event_table = {
}