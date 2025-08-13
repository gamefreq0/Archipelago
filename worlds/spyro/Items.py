from typing import final
from BaseClasses import Item
from .Addresses import RAM

base_spyro_item_id = 1000


@final
class SpyroItem(Item):
    game: str = "Spyro the Dragon"


homeworld_access = [
    "Artisans",
    "Peace Keepers",
    "Magic Crafters",
    "Beast Makers",
    "Dream Weavers"
]
level_access = [
    "Stone Hill",
    "Dark Hollow",
    "Town Square",
    "Toasty",
    "Sunny Flight",
    "Dry Canyon",
    "Cliff Town",
    "Ice Cavern",
    "Doctor Shemp",
    "Night Flight",
    "Alpine Ridge",
    "High Caves",
    "Wizard Peak",
    "Blowhard",
    "Crystal Flight",
    "Terrace Village",
    "Misty Bog",
    "Tree Tops",
    "Metalhead",
    "Wild Flight",
    "Dark Passage",
    "Lofty Castle",
    "Haunted Towers",
    "Jacques",
    "Icy Flight",
    "Gnorc Cove",
    "Twilight Harbor",
    "Gnasty Gnorc",
    "Gnasty's Loot"
]
boss_items = [
    "Toasty's Stilts",
    "Shemp's Staff",
    "Blowhard's Beard",
    "Metalhead's Mohawk",
    "Jacques' Ribbon"
]
trap_items = [
    "Flop Trap",
    "Roll Trap",
    "Faint Trap"
]
filler_items = [
    "Extra Life",
    "Butterfly"
]

full_item_list = homeworld_access + level_access + boss_items + trap_items
item_table = {index: value for index, value in enumerate(full_item_list)}

item_name_groups = {
    "worlds": {
        "Artisans",
        "Peace Keepers",
        "Magic Crafters",
        "Beast Makers",
        "Dream Weavers"
    },
    "boss items": {
        "Toasty's Stilts",
        "Shemp's Staff",
        "Blowhard's Beard",
        "Metalhead's Mohawk",
        "Jacques' Ribbon"
    },
    "levels": {
        "Stone Hill",
        "Dark Hollow",
        "Town Square",
        "Toasty",
        "Sunny Flight",
        "Dry Canyon",
        "Cliff Town",
        "Ice Cavern",
        "Doctor Shemp",
        "Night Flight",
        "Alpine Ridge",
        "High Caves",
        "Wizard Peak",
        "Blowhard",
        "Crystal Flight",
        "Terrace Village",
        "Misty Bog",
        "Tree Tops",
        "Metalhead",
        "Wild Flight",
        "Dark Passage",
        "Lofty Castle",
        "Haunted Towers",
        "Jacques",
        "Icy Flight",
        "Gnorc Cove",
        "Twilight Harbor",
        "Gnasty Gnorc",
        "Gnasty's Loot"
    }
}
