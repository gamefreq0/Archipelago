from typing import final
from BaseClasses import Item

BASE_SPYRO_ITEM_ID = 1000


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
goal_item = ["Victory"]
trap_items = [
    "Flop Trap",
    "Roll Trap",
    "Faint Trap"
]
filler_items = [
    "Extra Life",
    "Butterfly"
]

full_item_list = homeworld_access + level_access + boss_items + goal_item
full_item_list += trap_items + filler_items
item_table = dict(enumerate(full_item_list, start=BASE_SPYRO_ITEM_ID))

grouped_items = {
    "worlds": set(homeworld_access),
    "boss items": set(boss_items),
    "levels": set(level_access),
    "traps": set(trap_items),
    "filler": set(filler_items)
}
