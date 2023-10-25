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
    "Monkey Radar": 0xB,
    "Slingback Shooter": 0xC,
    "Dash Hoop": 0xD,
    "Sky Flyer": 0xA,
    "R.C. Car": 0x11,
    "Magic Punch": 0x12,

    #Keys
    "World Key": 0x13,

    "Victory": 0x14,

    "nothing": 0x0
}

event_table = {
}