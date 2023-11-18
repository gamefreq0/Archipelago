
class RAM():
    monkeyListGlobal = {
        1: 0x0DF828,
        2: 0x0DF829,
        3: 0x0DF82A,
        4: 0x0DF82B,
        5: 0x0DF830,
        6: 0x0DF831,
        8: 0x0DF832,
        7: 0x0DF833,
        10: 0x0DF834,
        9: 0x0DF835,
        11: 0x0DF838,
        12: 0x0DF839,
        13: 0x0DF83A,
        17: 0x0DF83B,
        15: 0x0DF840,
        14: 0x0DF841,
        16: 0x0DF848,
        18: 0x0DF850,
        19: 0x0DF851,
        20: 0x0DF852,
        29: 0x0DF858,
        31: 0x0DF859,
        30: 0x0DF85A,
        21: 0x0DF860,
        22: 0x0DF861,
        23: 0x0DF862,
        25: 0x0DF868,
        24: 0x0DF869,
        26: 0x0DF86A,
        28: 0x0DF870,
        27: 0x0DF871,
        33: 0x0DF878,
        37: 0x0DF879,
        42: 0x0DF87A,
        34: 0x0DF87B,
        32: 0x0DF87C,
        35: 0x0DF880,
        36: 0x0DF881,
        41: 0x0DF888,
        43: 0x0DF889,
        38: 0x0DF88A,
        39: 0x0DF890,
        40: 0x0DF891,
        44: 0x0DF892,
        51: 0x0DF898,
        49: 0x0DF899,
        45: 0x0DF8A0,
        47: 0x0DF8A8,
        46: 0x0DF8A9,
        50: 0x0DF8AA,
        48: 0x0DF8B0,
        52: 0x0DF8B1,
        53: 0x0DF8C0,
        54: 0x0DF8C1,
        55: 0x0DF8C2,
        56: 0x0DF8C3,
        57: 0x0DF8C8,
        60: 0x0DFDC9,
        58: 0x0DF8CA,
        59: 0x0DF8CB,
        61: 0x0DF8D0,
        62: 0x0DF8D1,
        63: 0x0DF8D2,
        64: 0x0DF8D3,
        65: 0x0DF8D8,
        67: 0x0DF8D9,
        66: 0x0DF8DA,
        68: 0x0DF8DB,
        70: 0x0DF8E0,
        69: 0x0DF8E1,
        77: 0x0DF8E8,
        71: 0x0DF8E9,
        78: 0x0DF8EA,
        72: 0x0DF8F0,
        73: 0x0DF8F1,
        74: 0x0DF8F2,
        75: 0x0DF8F3,
        76: 0x0DF8F4,
        79: 0x0DF8F8,
        80: 0x0DF908,
        81: 0x0DF909,
        84: 0x0DF90A,
        82: 0x0DF90B,
        83: 0x0DF90C,
        85: 0x0DF90D,
        86: 0x0DF910,
        87: 0x0DF911,
        91: 0x0DF918,
        93: 0x0DF919,
        92: 0x0DF91A,
        94: 0x0DF91B,
        88: 0x0DF920,
        89: 0x0DF921,
        90: 0x0DF922,
        95: 0x0DF928,
        96: 0x0DF929,
        99: 0x0DF92A,
        100: 0x0DF92B,
        101: 0x0DF930,
        102: 0x0DF931,
        103: 0x0DF932,
        97: 0x0DF938,
        98: 0x0DF939,
        104: 0x0DF948,
        105: 0x0DF949,
        106: 0x0DF94A,
        107: 0x0DF94B,
        109: 0x0DF958,
        110: 0x0DF959,
        108: 0x0DF95A,
        114: 0x0DF95B,
        115: 0x0DF95C,
        113: 0x0DF950,
        111: 0x0DF951,
        112: 0x0DF952,
        116: 0x0DF960,
        117: 0x0DF961,
        118: 0x0DF968,
        119: 0x0DF969,
        120: 0x0DF96A,
        123: 0x0DF970,
        121: 0x0DF978,
        122: 0x0DF979,
        124: 0x0DF97A,
        125: 0x0DF97B,
        127: 0x0DF988,
        136: 0x0DF989,
        126: 0x0DF98A,
        128: 0x0DF98B,
        137: 0x0DF98C,
        129: 0x0DF990,
        132: 0x0DF991,
        130: 0x0DF992,
        131: 0x0DF993,
        133: 0x0DF998,
        134: 0x0DF999,
        135: 0x0DF99A,
        138: 0x0DF9A8,
        139: 0x0DF9A9,
        140: 0x0DF9B0,
        141: 0x0DF9B1,
        142: 0x0DF9B2,
        143: 0x0DF9B8,
        144: 0x0DF9B9,
        145: 0x0DF9BA,
        146: 0x0DF9C8,
        147: 0x0DF9C9,
        148: 0x0DF9CA,
        149: 0x0DF9CB,
        152: 0x0DF9D0,
        151: 0x0DF9D1,
        150: 0x0DF9D2,
        153: 0x0DF9D8,
        154: 0x0DF9D9,
        155: 0x0DF9DA,
        156: 0x0DF9DB,
        157: 0x0DF9DC,
        158: 0x0DF9DE,
        159: 0x0DF9E0,
        160: 0x0DF9E1,
        161: 0x0DF9E8,
        162: 0x0DF9F0,
        168: 0x0DF9F8,
        164: 0x0DF9F9,
        167: 0x0DF9FA,
        166: 0x0DFA08,
        165: 0x0DFA09,
        163: 0x0DFA10,
        169: 0x0DFA18,
        170: 0x0DFA20,
        171: 0x0DFA21,
        172: 0x0DFA28,
        173: 0x0DFA29,
        174: 0x0DFA30,
        175: 0x0DFA31,
        176: 0x0DFA32,
        177: 0x0DFA38,
        178: 0x0DFA39,
        179: 0x0DFA3A,
        180: 0x0DFA3B,
        181: 0x0DFA60,
        182: 0x0DFA78,
        183: 0x0DFA80,
        184: 0x0DFA81,
        185: 0x0DFA82,
        186: 0x0DFA90,
        187: 0x0DFA91,
        188: 0x0DFA92,
        189: 0x0DFA93,
        190: 0x0DFAA0,
        192: 0x0DFAA8,
        193: 0x0DFAA9,
        194: 0x0DFAB0,
        196: 0x0DFAB1,
        195: 0x0DFAB2,
        197: 0x0DFAB3,
        201: 0x0DFAB8,
        202: 0x0DFAB9,
        203: 0x0DFAC0,
        204: 0x0DFAC1,
        198: 0x0DFAD0,
        199: 0x0DFAD1,
        200: 0x0DFAD2,
        191: 0x0DFAD8
    }

    monkeyListLocal = {
        1: {  # 1-1
            1: 0x0DFE00,
            3: 0x0DFE02,
            2: 0x0DFE01,
            4: 0x0DFE03
        },
        2: {  # 1-2
            5: 0x0DFE00,
            6: 0x0DFE01,
            7: 0x0DFE03,
            10: 0x0DFE04,
            9: 0x0DFE05,
            8: 0x0DFE02
        },
        3: {  # 1-3
            11: 0x0DFE00,
            12: 0x0DFE01,
            17: 0x0DFE03,
            13: 0x0DFE02
        },
        4: {  # 3 sub area
            14: 0x0DFE19,
            15: 0x0DFE18
        },
        5: {  # 3 sub area
            16: 0x0DFE30
        },
        6: {  # 2-1
            18: 0x0DFE00,
            19: 0x0DFE01,
            20: 0x0DFE02
        },
        7: {  # 6 sub area
            29: 0x0DFE18,
            30: 0x0DFE1A,
            31: 0x0DFE19
        },
        8: {  # 6 sub area
            23: 0x0DFE32,
            21: 0x0DFE30,
            22: 0x0DFE31
        },
        9: {  # 6 sub area
            24: 0x0DFE49,
            25: 0x0DFE48,
            26: 0x0DFE4A
        },
        10: {  # 6 sub area
            27: 0x0DFE61,
            28: 0x0DFE60
        },
        11: {  # 2-2
            32: 0x0DFE04,
            33: 0x0DFE00,
            34: 0x0DFE03,
            37: 0x0DFE01,
            42: 0x0DFE02
        },
        12: {  # sub area of 11
            35: 0x0DFE18,
            36: 0x0DFE19
        },
        13: {  # sub area of 11
            38: 0x0DFE32,
            41: 0x0DFE30,
            43: 0x0DFE31
        },
        14: {  # sub area of 11
            39: 0x0DFE48,
            40: 0x0DFE49,
            44: 0x0DFE4A
        },
        15: {  # 2-3
            49: 0x0DFE01,
            51: 0x0DFE00
        },
        16: {  # sub area of 15
            45: 0x0DFE18
        },
        17: {  # sub area of 15
            47: 0x0DFE30,
            50: 0x0DFE32,
            46: 0x0DFE31
        },
        18: {  # sub area of 16
            48: 0x0DFE48,
            52: 0x0DFE49
        },
        19: {

        },
        20: {  # 4-1
            53: 0x0DFE00,
            54: 0x0DFE01,
            55: 0x0DFE02,
            56: 0x0DFE03
        },
        21: {  # sub area of 20
            57: 0x0DFE18,
            58: 0x0DFE1A,
            59: 0x0DFE1B,
            60: 0x0DFE19
        },
        22: {  # 4-2
            61: 0x0DFE00,
            62: 0x0DFE01,
            63: 0x0DFE02,  # doesn't match ign
            64: 0x0DFE03
        },
        23: {  # sub area 22
            65: 0x0DFE18,
            67: 0x0DFE19,  # doesn't match ign
            68: 0x0DFE1B,
            66: 0x0DFE1A
        },
        24: {  # 4-3
            69: 0x0DFE01,
            70: 0x0DFE00
        },
        25: {
            71: 0x0DFE19,
            77: 0x0DFE18,
            78: 0x0DFE1A
        },
        26: {
            72: 0x0DFE30,
            73: 0x0DFE31,
            74: 0x0DFE32,
            75: 0x0DFE33,
            76: 0x0DFE34
        },
        27: {
            79: 0x0DFE48
        },
        28: {

        },
        29: {  # 5-1
            80: 0x0DFE00,
            81: 0x0DFE01,
            84: 0x0DFE02,
            83: 0x0DFE04,
            85: 0x0DFE05,
            82: 0x0DFE03
        },
        30: {  # 5-2
            86: 0x0DFE00,
            87: 0x0DFE01
        },
        31: {
            91: 0x0DFE18,
            92: 0x0DFE1A,
            93: 0x0DFE19,
            94: 0x0DFE1B
        },
        32: {
            88: 0x0DFE30,
            90: 0x0DFE32,
            89: 0x0DFE31
        },
        33: {  # 5-3
            95: 0x0DFE00,
            96: 0x0DFE01,
            99: 0x0DFE02,
            100: 0x0DFE03
        },
        34: {
            101: 0x0DFE18,
            102: 0x0DFE19,
            103: 0x0DFE1A
        },
        35: {
            98: 0x0DFE31,
            97: 0x0DFE30
        },
        36: {

        },
        37: {  # 7-1
            104: 0x0DFE00,
            105: 0x0DFE01,
            106: 0x0DFE02,
            107: 0x0DFE03
        },
        38: {
            108: 0x0DFE1A,
            110: 0x0DFE19,
            109: 0x0DFE18,
            114: 0x0DFE1B,
            115: 0x0DFE1C
        },
        39: {
            111: 0x0DFE31,
            112: 0x0DFE32,
            113: 0x0DFE30
        },
        40: {  # 7-2
            116: 0x0DFE00,
            117: 0x0DFE01
        },
        41: {
            118: 0x0DFE18,
            119: 0x0DFE19,
            120: 0x0DFE1A
        },
        42: {
            123: 0x0DFE30
        },
        43: {
            122: 0x0DFE49,
            121: 0x0DFE48,
            124: 0x0DFE60,
            125: 0x0DFE61
        },
        44: {

        },
        45: {  # 7-3
            126: 0x0DFE02,
            127: 0x0DFE00,
            128: 0x0DFE03,  #
            137: 0x0DFE04,
            136: 0x0DFE01
        },
        46: {
            129: 0x0DFE18,  #
            131: 0x0DFE1B,  #
            130: 0x0DFE1A,  #
            135: 0x0DFE19
        },
        47: {
            133: 0x0DFE30,  #
            134: 0x0DFE31,  #
            135: 0x0DFE32  #
        },
        48: {

        },
        49: {
            139: 0x0DFE61,  #
            138: 0x0DFE60  #
        },
        50: {
            140: 0x0DFE78,  #
            141: 0x0DFE79,  #
            142: 0x0DFE7A  #
        },
        51: {
            145: 0x0DFE92,  #
            144: 0x0DFE91,  #
            143: 0x0DFE90  #
        },
        52: {

        },
        53: {  # 8-1
            146: 0x0DFE00,
            149: 0x0DFE03,
            147: 0x0DFE01,
            148: 0x0DFE02
        },
        54: {
            151: 0x0DFE19,
            152: 0x0DFE18,
            150: 0x0DFE1A
        },
        55: {
            155: 0x0DFE32,
            153: 0x0DFE30,
            156: 0x0DFE33,
            157: 0x0DFE34,
            154: 0x0DFE31,
            158: 0x0DFE35
        },
        56: {  # 8-2
            159: 0x0DFE00,
            160: 0x0DFE01
        },
        57: {
            161: 0x0DFE18
        },
        58: {
            162: 0x0DFE30
        },
        59: {
            164: 0x0DFE49,
            167: 0x0DFE4A,
            168: 0x0DFE48
        },
        60: {

        },
        61: {
            165: 0x0DFE79,
            166: 0x0DFE78
        },
        62: {
            163: 0x0DFE90
        },
        63: {  # 8-3
            169: 0x0DFE00
        },
        64: {
            171: 0x0DFE19,
            170: 0x0DFE18
        },
        65: {
            172: 0x0DFE30,
            173: 0x0DFE31
        },
        66: {
            174: 0x0DFE48,
            175: 0x0DFE49,
            176: 0x0DFE4A
        },
        67: {
            177: 0x0DFE60,
            179: 0x0DFE62,  #
            180: 0x0DFE63,  #
            178: 0x0DFE61  #
        },
        68: {

        },
        69: {

        },
        70: {

        },
        71: {

        },
        72: {
            181: 0x0DFE00  #
        },
        73: {

        },
        74: {

        },
        75: {
            182: 0x0DFE48
        },
        76: {
            183: 0x0DFE60,  # ?
            184: 0x0DFE61,  #
            185: 0x0DFE62  # ?
        },
        77: {
            187: 0x0DFE01,  #
            186: 0x0DFE00,
            188: 0x0DFE02,  #
            189: 0x0DFE03  #
        },
        78: {
            190: 0x0DFE00
        },
        79: {
            192: 0x0DFE18,
            193: 0x0DFE19
        },
        80: {
            194: 0x0DFE30,
            195: 0x0DFE32,
            196: 0x0DFE31,
            197: 0x0DFE33
        },
        81: {
            201: 0x0DFE48,
            202: 0x0DFE49
        },
        82: {
            203: 0x0DFE60,
            204: 0x0DFE61
        },
        83: {

        },
        84: {
            198: 0x0DFE90,
            199: 0x0DFE91,
            200: 0x0DFE92
        },
        85: {
            191: 0x0DFEA8
        },
        86: {

        }
    }

    items = {
        "Club": 0x1,
        "Net": 0x2,
        "Radar": 0x4,
        "Sling": 0x8,
        "Hoop": 0x10,
        "Punch": 0x20,
        "Flyer": 0x40,
        "Car": 0x80,
        "Key": 0x100,
        "Victory": 0x200,
        "Nothing": 0x0
    }

    caughtStatus = {
        "Unloaded": 0x0,
        "Uncaught": 0x4,
        "Caught": 0x2
    }

    levelStatus = {
        "Locked": 0x00,
        "Complete": 0x01,
        "Hundo": 0x02,
        "Open": 0x03
    }

    gameState = {
        "Sony": 0x0,
        "Menu": 0x3,
        "Cutscene": 0x8,
        "LevelSelect": 0x9,
        "LevelIntro": 0xA,
        "InLevel": 0xB,
        "Cleared": 0xC,
        "TimeStation": 0xD,
        "Save/Load": 0xE,
        "GameOver": 0xF,
        "NewGadget": 0x11,
        "LevelIntroTT": 0x12,
        "InLevelTT": 0x13,
        "ClearedTT": 0x14,
        "Memory": 0x15,
        "JakeIntro": 0x17,
        "Jake": 0x18,
        "JakeCleared": 0x19,
        "Cutscene2": 0x1A,
        "Book": 0x1C,
        "Credits1": 0x1D,
        "Credits2": 0x1E,
        "PostCredits": 0x23
    }

    levelAddresses = {
        11: 0xdfc71,
        12: 0xdfc72,
        13: 0xdfc73,
        21: 0xdfc74,
        22: 0xdfc75,
        23: 0xdfc76,
        31: 0xdfc77,
        41: 0xdfc78,
        42: 0xdfc79,
        43: 0xdfc7A,
        51: 0xdfc7B,
        52: 0xdfc7C,
        53: 0xdfc7D,
        61: 0xdfc7E,
        71: 0xdfc7F,
        72: 0xdfc80,
        73: 0xdfc81,
        81: 0xdfc82,
        82: 0xdfc85,
        83: 0xdfc86,
        91: 0xdfc88,
        92: 0xdfc8e

    }

    unlockedGadgetsAddress = 0x0F51C4
    trainingRoomProgressAddress = 0x0DFDCC
    currentRoomIdAddress = 0x0F4476
    gameStateAddress = 0x0F4470
    unlockedLevelAdress = 0x0DFC70
    requiredApesAddress = 0x0F44D8
    hundoApesAdress = 0x0F44D6

