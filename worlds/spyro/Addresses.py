class RAM:
    curLevelID: int = 0x7596c
    destLevelID: int = 0x758b4
    curGameState: int = 0x757d8
    balloonistMenuChoice: int = 0x777f0
    unlockedWorlds: int = 0x758d0
    startingLevelID: int = 0x2d4f0
    worldTextOffsets: dict[str, int] = {
        "artisans": 0x1006c,
        "keepers": 0x1005c,
        "crafters": 0x1004c,
        "makers": 0x1003c,
        "weavers": 0x1002c,
        "gnasty": 0x1001c
    }
    nestorUnskippable: int = 0x1747f4
    spyroCurAnimation: int = 0x78ad0
    spyroColorFilter: int = 0x78a80
    spyroStates: dict[str, int] = {
        "standing": 0x00,
        "flop": 0x06,
        "roll": 0x13,
        "death_spin": 0x1e
    }
    gameStates: dict[str, int] = {
        "gameplay": 0x00,
        "loading": 0x01,
        "paused": 0x02,
        "inventory": 0x03,
        "death": 0x04,
        "game_over": 0x05,
        "flight_menu": 0x07,
        "dragon_cutscene": 0x08,
        "fly_in": 0x09,
        "exiting_level": 0x0a,
        "fairy_textbox": 0x0b,
        "balloonist": 0x0c,
        "title_screen": 0x0d,
        "cutscene": 0x0e,
        "credits": 0x0f
    }
