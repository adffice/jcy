"""
常量模块
"""

# 互斥体名称
MUTEX_NAME = "Global\\D2R_MOD_JCY_MUTEX"

# 互斥错误 183, 表示互斥体已存在（即已有实例）
ERROR_ALREADY_EXISTS = 183

# 语言
LANG = "zhCN"

# 控制器名称
APP_NAME = "jcy控制器"

# MOD版本
APP_VERSION = "v1.1.1"

# 控制器全称
APP_FULL_NAME = f"{APP_NAME}_{APP_VERSION}"

# 发布日期
APP_DATE = "20250723"

# APP大小
APP_SIZE = "750x700"

# MOD目录
MOD_DIR = "jcy.mpq"

# APP数据目录
APP_DATA_DIR = "D2R_Mod_jcy"

# 配置文件
SETTINGS_FILE = "settings.json"

# 账号文件
ACCOUNTS_FILE = "accounts.json"

# 区服地址
REGION_DOMAIN_MAP = {
    "kr": "kr.actual.battle.net",
    "us": "us.actual.battle.net",
    "eu": "eu.actual.battle.net"
}

# 区服名称
REGION_NAME_MAP = {
    "kr": "亚服",
    "us": "美服",
    "eu": "欧服"
}

# Unicode私有区字符 for 屏蔽道具
UE01A = "" * 41

TERROR_ZONE = {
  "1-1": {
    "zhCN": "鲜血荒地、 邪恶洞窟",
    "zhTW": "鮮血荒地、 邪惡洞窟",
    "enUS": "Blood Moor and Den of Evil"
  },
  "1-2": {
    "zhCN": "冰冷之原、洞穴",
    "zhTW": "冰冷之原、洞穴",
    "enUS": "Cold Plains and The Cave"
  },
  "1-3": {
    "zhCN": "埋骨之地、墓穴、大陵墓",
    "zhTW": "埋骨之地、墓穴、大陵墓",
    "enUS": "Burial Grounds, The Crypt, and The Mausoleum"
  },
  "1-4": {
    "zhCN": "乱石旷野",
    "zhTW": "亂石曠野",
    "enUS": "Stony Field"
  },
  "1-5": {
    "zhCN": "崔斯特姆",
    "zhTW": "崔斯特姆",
    "enUS": "Tristram"
  },
  "1-6": {
    "zhCN": "黑暗森林、地底通道",
    "zhTW": "黑暗森林、地底通道",
    "enUS": "Dark Wood and Underground Passage"
  },
  "1-7": {
    "zhCN": "黑色荒地、 地洞",
    "zhTW": "黑色荒地、 地洞",
    "enUS": "Black Marsh and The Hole"
  },
  "1-8": {
    "zhCN": "遗忘之塔",
    "zhTW": "遺忘之塔",
    "enUS": "The Forgotten Tower"
  },
  "1-9": {
    "zhCN": "地穴",
    "zhTW": "地穴",
    "enUS": "The Pit"
  },
  "1-10": {
    "zhCN": "监牢、兵营",
    "zhTW": "監牢、兵營",
    "enUS": "Jail and Barracks"
  },
  "1-11": {
    "zhCN": "大教堂、地下墓穴",
    "zhTW": "大教堂、地下墓穴",
    "enUS": "Cathedral and Catacombs"
  },
  "1-12": {
    "zhCN": "哞哞农场",
    "zhTW": "哞哞農場",
    "enUS": "Moo Moo Farm"
  },
  "2-1": {
    "zhCN": "鲁高因下水道",
    "zhTW": "鲁高因下水道",
    "enUS": "Lut Gholein Sewers"
  },
  "2-2": {
    "zhCN": "碎石荒地、古老石墓",
    "zhTW": "碎石荒地、古老石墓",
    "enUS": "Rocky Waste and Stony Tomb"
  },
  "2-3": {
    "zhCN": "干土高地、死亡之殿",
    "zhTW": "乾土高地、死亡之殿",
    "enUS": "Dry Hills and Halls of the Dead"
  },
  "2-4": {
    "zhCN": "遥远的绿洲",
    "zhTW": "遙遠的綠洲",
    "enUS": "Far Oasis"
  },
  "2-5": {
    "zhCN": "古代通道",
    "zhTW": "古代通道",
    "enUS": "Ancient Tunnels"
  },
  "2-6": {
    "zhCN": "失落古城、群蛇峡谷、利爪蛇魔神殿",
    "zhTW": "失落古城、群蛇峽谷、利爪蛇魔神殿",
    "enUS": "Lost City, Valley of Snakes, and Claw Viper Temple"
  },
  "2-7": {
    "zhCN": "秘法圣殿",
    "zhTW": "秘法聖殿",
    "enUS": "Arcane Sanctuary"
  },
  "2-8": {
    "zhCN": "塔拉夏的古墓、塔拉夏的密室",
    "zhTW": "塔拉夏的古墓、塔拉夏的密室",
    "enUS": "Tal Rasha's Tombs and Tal Rasha's Chamber"
  },
  "3-1": {
    "zhCN": "蜘蛛森林、蜘蛛洞窟",
    "zhTW": "蜘蛛森林、蜘蛛洞窟",
    "enUS": "Spider Forest and Spider Cavern"
  },
  "3-2": {
    "zhCN": "剥皮丛林、剥皮地牢",
    "zhTW": "剝皮叢林、剝皮地牢",
    "enUS": "Flayer Jungle and Flayer Dungeon"
  },
  "3-3": {
    "zhCN": "大沼泽",
    "zhTW": "大沼澤",
    "enUS": "Great Marsh"
  },
  "3-4": {
    "zhCN": "库拉斯特市集、荒废的神殿、废弃的寺院",
    "zhTW": "庫拉斯特市集、荒廢的神殿、廢棄的寺院",
    "enUS": "Kurast Bazaar, Ruined Temple, and Disused Fane"
  },
  "3-5": {
    "zhCN": "崔凡克",
    "zhTW": "崔凡克",
    "enUS": "Travincal"
  },
  "3-6": {
    "zhCN": "憎恨的囚牢",
    "zhTW": "憎恨的囚牢",
    "enUS": "Durance of Hate"
  },
  "4-1": {
    "zhCN": "外圍荒原、絕望平原",
    "zhTW": "外圍荒原、絕望平原",
    "enUS": "Outer Steppes and Plains of Despair"
  },
  "4-2": {
    "zhCN": "火焰之河、罪罚之城",
    "zhTW": "火焰之河、罪罰之城",
    "enUS": "River of Flame and City of the Damned"
  },
  "4-3": {
    "zhCN": "混沌避难所",
    "zhTW": "混沌庇難所",
    "enUS": "Chaos Sanctuary"
  },
  "5-1": {
    "zhCN": "血腥丘陵、冰冻高地、亚巴顿",
    "zhTW": "血腥丘陵、冰凍高地、亞巴頓",
    "enUS": "Bloody Foothills, Frigid Highlands and Abaddon"
  },
  "5-2": {
    "zhCN": "冰河小径、漂泊者洞窟",
    "zhTW": "冰河小径、漂泊者洞窟",
    "enUS": "Glacial Trail and Drifter Cavern"
  },
  "5-3": {
    "zhCN": "先祖之路、冰窖",
    "zhTW": "先祖之路、冰窖",
    "enUS": "Ancient's Way and Icy Cellar"
  },
  "5-4": {
    "zhCN": "亚瑞特高原、冥河地穴",
    "zhTW": "亞瑞特高原、冥河地穴",
    "enUS": "Arreat Plateau and Pit of Acheron"
  },
  "5-5": {
    "zhCN": "水晶通道、冰冻之河",
    "zhTW": "水晶通道、冰凍之河",
    "enUS": "Crystalline Passage and Frozen River"
  },
  "5-6": {
    "zhCN": "尼拉塞克神殿、怨恸之厅、苦痛之厅、沃特之厅",
    "zhTW": "尼拉塞克神殿、怨慟之廳、苦痛之廳、沃特之廳",
    "enUS": "Nihlathak's Temple and Temple Halls"
  },
  "5-7": {
    "zhCN": "世界之石要塞、毁灭王座、世界之石大殿",
    "zhTW": "世界之石要塞、毀滅王座、世界之石大殿",
    "enUS": "Worldstone Keep, Throne of Destruction, and Worldstone Chamber"
  }
}
