from typing import Optional
from BaseClasses import ItemClassification, Item
from .Strings import AEItem

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
    AEItem.Club.value: 0x1,
    AEItem.Net.value: 0x2,
    AEItem.Radar.value: 0x4,
    AEItem.Sling.value: 0x8,
    AEItem.Hoop.value: 0x10,
    AEItem.Punch.value: 0x20,
    AEItem.Flyer.value: 0x40,
    AEItem.Car.value: 0x80,

    AEItem.WaterNet.value: 0x400,

    #Keys
    AEItem.Key.value: 0x100,
    AEItem.Victory.value: 0x200,
    AEItem.Nothing.value: 0x0
}

event_table = {
}