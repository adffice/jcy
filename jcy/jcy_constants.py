"""
常量模块
"""

# 互斥体名称
MUTEX_NAME = "Global\\D2R_MOD_JCY_MUTEX"

# 互斥错误 183, 表示互斥体已存在（即已有实例）
ERROR_ALREADY_EXISTS = 183

# 自定义消息ID(通知已有实例, restore窗口)
WM_SHOW_WINDOW = 0x5000

# 语言
LANG = "zhCN"

# 控制器名称
APP_NAME = "jcy控制器"

# MOD版本
APP_VERSION = "v1.1.3"

# 控制器全称
APP_FULL_NAME = f"{APP_NAME}_{APP_VERSION}"

# 发布日期
APP_DATE = "20250809"

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

TERROR_ZONE_API = (
    "https://asia.d2tz.info/terror_zone?mode=online",
    "https://api.d2tz.info/terror_zone?mode=online",
)

# 恐怖地带
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

# 词缀缩写
AFFIX_ABBREVIATION = {
    "enUS": {
        "%d%% Better Chance of Getting Magic Items": "(MF)",
        "Physical Damage Received Increased by": "(DI)",
        "%+d to Attack Rating against Demons": "(ARD)",
        "%+d to Attack Rating against Undead": "(ARU)",
        "-%d%% to Enemy Lightning Resistance": "(-LR)",
        "Physical Damage Received Reduced by": "(DR)",
        "%d%% Increased Chance of Blocking": "(CTB)",
        "%+d%% to Maximum Lightning Resist": "(Max LR)",
        "-%d%% to Enemy Poison Resistance": "(-PR)",
        "%+d to Maximum Lightning Damage": "(Max LD)",
        "%+d to Minimum Lightning Damage": "(Min LD)",
        "%+d to Necromancer Skill Levels": "(NEC)",
        "%+d%% Damage Taken Goes To Mana": "(DTM)",
        "Slightly Increased Attack Speed": "(IAS)",
        "%+d%% to Lightning Skill Damage": "(LD)",
        "Greatly Increased Attack Speed": "(IAS)",
        "%+d%% to Maximum Poison Resist": "(Max PR)",
        "%+d Life after each Demon Kill": "(DLK)",
        "-%d%% to Enemy Cold Resistance": "(-CR)",
        "-%d%% to Enemy Fire Resistance": "(-FR)",
        "%+d to Sorceress Skill Levels": "(SOR)",
        "%+d to Barbarian Skill Levels": "(BAR)",
        "%+d%% Chance of Crushing Blow": "(CB)",
        "%+d%% to Maximum Magic Resist": "(Max MR)",
        "%d%% Extra Gold from Monsters": "(EG)",
        "%+d to Maximum Poison Damage": "(Max PD)",
        "%+d to Minimum Poison Damage": "(Min PD)",
        "%+d%% Increased Attack Speed": "(IAS)",
        "%+d%% to Maximum Fire Resist": "(Max FR)",
        "%+d%% to Maximum Cold Resist": "(Max CR)",
        "%+d Absorbs Lightning Damage": "(LDA)",
        "Slain Monsters Rest in Peace": "(RIP)",
        "%+d%% to Poison Skill Damage": "(PD)",
        "%+d to Assassin Skill Levels": "(ASN)",
        "Increase Maximum Durability": "(Max DUR)",
        "%+d to Paladin Skill Levels": "(PAL)",
        "%+d%% Chance of Open Wounds": "(OW)",
        "%+d to Mana after each Kill": "(EK)",
        "Adds %d-%d lightning damage": "(LD)",
        "Lightning Damage Reduced by": "(LDR)",
        "%d%% Bonus to Attack Rating": "(AR)",
        "to Attack Rating vs. Demons": "(ARD)",
        "to Attack Rating vs. Undead": "(ARU)",
        "%+d to Maximum Fire Damage": "(Max FD)",
        "%+d to Minimum Fire Damage": "(Min FD)",
        "%+d to Maximum Cold Damage": "(Max CD)",
        "%+d to Minimum Cold Damage": "(Min CD)",
        "%+d to Amazon Skill Levels": "(AMA)",
        "%+d%% to Experience Gained": "(EXP)",
        "%+d%% to Fire Skill Damage": "(FD)",
        "%+d%% to Cold Skill Damage": "(CD)",
        "Hit Causes Monster to Flee": "(Flee)",
        "%+d%% Faster Hit Recovery": "(FHR)",
        "%+d Absorbs Poison Damage": "(PDA)",
        "Reduces all Vendor Prices": "(-Price)",
        "%+d to Druid Skill Levels": "(DRU)",
        "%d%% Mana stolen per hit": "(LM)",
        "%d%% Life stolen per hit": "(LL)",
        "Poison Length Reduced by": "(PLR)",
        "Adds %d-%d poison damage": "(PD)",
        "Poison Damage Reduced by": "(PDR)",
        "%+d Absorbs Magic Damage": "(MDA)",
        "%+d Life after each Kill": "(LK)",
        "percent to Attack Rating": "(AR)",
        "Magic Damage Reduced by": "(MDR)",
        "Ignore Target's Defense": "(ITD)",
        "%+d%% Faster Block Rate": "(FBR)",
        "%+d to All Skill Levels": "(All Skill)",
        "Adds %d-%d magic damage": "(MD)",
        "%+d Absorbs Fire Damage": "(FDA)",
        "%+d Absorbs Cold Damage": "(CDA)",
        "%+d%% Enhanced Defense": "(EDef)",
        "%+d%% Damage to Demons": "(DTD)",
        "%+d%% Damage to Undead": "(DTU)",
        "%+d%% Faster Cast Rate": "(FCR)",
        "Improved Attack Rating": "(AR)",
        "Adds %d-%d fire damage": "(FD)",
        "Adds %d-%d cold damage": "(CD)",
        "Fire Damage Reduced by": "(FDR)",
        "Cold Damage Reduced by": "(CDR)",
        "%+d to Maximum Damage": "(MAX)",
        "%+d to Minimum Damage": "(MIN)",
        "Increase Maximum Life": "(Max Life)",
        "Increase Maximum Mana": "(Max Mana)",
        "%+d%% Faster Run/Walk": "(FRW)",
        "%+d%% Enhanced Damage": "(EDmg)",
        "%+d to all Attributes": "(ATTR)",
        "%d%% to Attack Rating": "(AR)",
        "%+d to Attack Rating": "(AR)",
        "Half Poison Duration": "(HPD)",
        "Prevent Monster Heal": "(PMH)",
        "Half Freeze Duration": "(HFD)",
        "Fastest Hit Recovery": "(FHR)",
        "%+d Lightning Absorb": "(LA)",
        "%+d lightning damage": "(LD)",
        "to Damage vs. Demons": "(DTD)",
        "%+d to Light Radius": "(Light Radius)",
        "%+d%% Deadly Strike": "(DS)",
        "%+d Maximum Stamina": "(Max STA)",
        "Fastest Block Rate": "(FBR)",
        "Damage Reduced by": "(DR)",
        "%+d to All Skills": "(All Skills)",
        "Heal Stamina Plus": "(Heal STA)",
        "Fast Hit Recovery": "(FHR)",
        "Fastest Cast Rate": "(FCR)",
        "%+d poison damage": "(PD)",
        "Adds %d-%d damage": "(DMG)",
        "Hit Blinds Target": "(HBT)",
        "%+d to Dexterity": "(DEX)",
        "Lightning Resist": "(LR)",
        "Fastest Run/Walk": "(FRW)",
        "Lightning Absorb": "(LA)",
        "%+d Magic Absorb": "(MA)",
        "Cannot Be Frozen": "(CBF)",
        "%+d magic damage": "(MD)",
        "%+d to Strength": "(STR)",
        "%+d to Vitality": "(VIT)",
        "Regenerate Mana": "(Reg Mana)",
        "Fast Block Rate": "(FBR)",
        "%+d Fire Absorb": "(FA)",
        "%+d Cold Absorb": "(CA)",
        "All Resistances": "(RES)",
        "%+d fire damage": "(FD)",
        "%+d cold damage": "(CD)",
        "Chance to Block": "(CTB)",
        "Slows Target by": "(Slow)",
        "Replenish Life": "(Life Rep)",
        "Replenish Mana": "(Mana Rep)",
        "Freezes target": "(FT)",
        "Fast Cast Rate": "(FCR)",
        "%d%% to Damage": "(DMG)",
        "%+d to Energy": "(ENG)",
        "Poison Resist": "(PR)",
        "Fast Run/Walk": "(FRW)",
        "Magic Resist": "(MR)",
        "Requirements": "(REQ)",
        "Magic Absorb": "(MA)",
        "%+d to Mana": "(Mana)",
        "%+d Defense": "(DEF)",
        "Fire Resist": "(FR)",
        "Cold Resist": "(CR)",
        "%+d to Life": "(Life)",
        "Fire Absorb": "(FA)",
        "Cold Absorb": "(CA)",
        "Level %d %s": "(%d/%d Charges)",
        "Durability": "(DUR)",
        "%+d damage": "(DMG)",
        "Knockback": "(KB)",
        "Damage": "(DMG)",
    },
    "zhCN": {
        "%+d%% 受到的伤害转换为法力": "(DTM)",
        "%+d%% 几率造成开创性伤口": "(OW)",
        "%+d 每次消灭恶魔恢复的生命": "(DLK)",
        "%d%% 额外几率获得魔法物品": "(MF)",
        "%+d%% 几率命中使怪物逃跑": "(Flee)",
        "%+d%% 更快速跑步/步行": "(FRW)",
        "%+d%% 更快速打击回复": "(FHR)",
        "%+d 每次消灭恢复的法力": "(EK)",
        "%+d 每次消灭恢复的生命": "(LK)",
        "-%d%% 敌人的冰霜抗性": "(-CR)",
        "-%d%% 敌人的火焰抗性": "(-FR)",
        "-%d%% 敌人的闪电抗性": "(-LR)",
        "-%d%% 敌人的毒素抗性": "(-PR)",
        "%d%% 怪物额外掉落金币": "(EG)",
        "%d%% 击中时偷取法力": "(LM)",
        "%d%% 击中时偷取生命": "(LL)",
        "%+d 死灵法师技能等级": "(NEC)",
        "%+d%% 对恶魔的伤害": "(DTD)",
        "%+d%% 对亡灵的伤害": "(DTU)",
        "%+d%% 提高攻击速度": "(IAS)",
        "%+d%% 几率粉碎打击": "(CB)",
        "%+d%% 火焰抗性上限": "(Max FR)",
        "%+d%% 冰霜抗性上限": "(Max CR)",
        "%+d%% 闪电抗性上限": "(Max LR)",
        "%+d%% 魔法抗性上限": "(Max MR)",
        "%+d%% 毒素抗性上限": "(Max PR)",
        "+ %d-%d 火焰伤害": "(FD)",
        "+ %d-%d 冰霜伤害": "(CD)",
        "+ %d-%d 闪电伤害": "(LD)",
        "+ %d-%d 魔法伤害": "(MD)",
        "+ %d-%d 毒素伤害": "(PD)",
        "%+d%% 火焰技能伤害": "(FD)",
        "%+d%% 冰霜技能伤害": "(CD)",
        "%+d%% 闪电技能伤害": "(LD)",
        "%+d%% 毒素技能伤害": "(PD)",
        "+%d%% 生命最大值": "(Max Life)",
        "+%d%% 法力最大值": "(Max Mana)",
        "+%d%% 最大耐久度": "(Max DUR)",
        "%+d 亚马逊技能等级": "(AMA)",
        "%+d 圣骑士技能等级": "(PAL)",
        "%+d 野蛮人技能等级": "(BAR)",
        "%d%% 格挡几率提高": "(CTB)",
        "%+d 对恶魔的命中值": "(ARD)",
        "%+d 对亡灵的命中值": "(ARU)",
        "%+d%% 更快速施法": "(FCR)",
        "%+d%% 更快速格挡": "(FBR)",
        "%+d%% 获得的经验": "(EXP)",
        "%+d 德鲁伊技能等级": "(DRU)",
        "%+d 最大火焰伤害": "(Max FD)",
        "%+d 最小火焰伤害": "(Min FD)",
        "%+d 最大闪电伤害": "(Max LD)",
        "%+d 最小闪电伤害": "(Min LD)",
        "%+d 最大冰霜伤害": "(Max CD)",
        "%+d 最小冰霜伤害": "(Min CD)",
        "%+d%% 强化防御": "(EDef)",
        "%+d 巫师技能等级": "(SOR)",
        "%+d 最大毒素伤害": "(Max PD)",
        "%+d 最小毒素伤害": "(Min PD)",
        "%+d 火焰伤害吸收": "(FA)",
        "%+d 闪电伤害吸收": "(LA)",
        "%+d 魔法伤害吸收": "(MA)",
        "%+d 冰霜伤害吸收": "(CA)",
        "%+d%% 致死打击": "(DS)",
        "%+d%% 强化伤害": "(EDmg)",
        "%+d 所有技能等级": "(All Skill)",
        "+ %d-%d 伤害": "(DMG)",
        "%+d 吸收魔法伤害": "(MDA)",
        "%+d 吸收火焰伤害": "(FDA)",
        "%+d 吸收冰霜伤害": "(CDA)",
        "%+d 吸收闪电伤害": "(LDA)",
        "%+d 吸收毒素伤害": "(PDA)",
        "%d%% 提高命中值": "(AR)",
        "%d%% 加成命中值": "(AR)",
        "%+d 刺客技能等级": "(ASN)",
        "%d%% 法力回复": "(Reg Mana)",
        "所有商人的收费减少": "(-Price)",
        "消灭的怪物就此安息": "(RIP)",
        "%d%% 提高伤害": "(DMG)",
        "受到的物理伤害降低": "(DR)",
        "受到的物理伤害提高": "(DI)",
        "%+d 最大伤害": "(MAX)",
        "%+d 最小伤害": "(MIN)",
        "%+d 照亮范围": "(Light Radius)",
        "%+d 所有技能": "(All Skills)",
        "轻微提升攻击速度": "(IAS)",
        "大幅提高攻击速度": "(IAS)",
        "最快速跑步/步行": "(FRW)",
        "%+d 最大耐力": "(Max STA)",
        "%+d 所有抗性": "(RES)",
        "%+d 火焰伤害": "(FD)",
        "%+d 冰霜伤害": "(CD)",
        "%+d 闪电伤害": "(LD)",
        "%+d 魔法伤害": "(MD)",
        "%+d 毒素伤害": "(PD)",
        "%+d 所有属性": "(ATTR)",
        "%+d 命中值": "(AR)",
        "忽略目标的防御": "(ITD)",
        "最快速打击回复": "(FHR)",
        "命中可致盲目标": "(HBT)",
        "对恶魔的命中值": "(ARD)",
        "对亡灵的命中值": "(ARU)",
        "%+d 力量": "(STR)",
        "%+d 敏捷": "(DEX)",
        "%+d 活力": "(VIT)",
        "%+d 能量": "(ENG)",
        "%+d 法力": "(Mana)",
        "%+d 防御": "(DEF)",
        "%+d 生命": "(Life)",
        "魔法伤害降低": "(MDR)",
        "中毒时间缩短": "(PLR)",
        "治愈耐力外加": "(Heal STA)",
        "中毒时间减半": "(HPD)",
        "防止怪物治愈": "(PMH)",
        "冻结时间减半": "(HFD)",
        "快速打击回复": "(FHR)",
        "火焰伤害吸收": "(FA)",
        "闪电伤害吸收": "(LA)",
        "魔法伤害吸收": "(MA)",
        "冰霜伤害吸收": "(CA)",
        "%+d 伤害": "(DMG)",
        "火焰伤害降低": "(FDR)",
        "冰霜伤害降低": "(CDR)",
        "闪电伤害降低": "(LDR)",
        "毒素伤害降低": "(PDR)",
        "对恶魔的伤害": "(DTD)",
        "跑步/步行": "(FRW)",
        "最快速施法": "(FCR)",
        "最快速格挡": "(FBR)",
        "无法被冻结": "(CBF)",
        "提高命中值": "(AR)",
        "使目标减速": "(Slow)",
        "%到命中值": "(AR)",
        "%d级%s": "(%d/%d 次充能)",
        "火焰抗性": "(FR)",
        "冰霜抗性": "(CR)",
        "闪电抗性": "(LR)",
        "魔法抗性": "(MR)",
        "毒素抗性": "(PR)",
        "补充生命": "(Life Rep)",
        "补充法力": "(Mana Rep)",
        "伤害降低": "(DR)",
        "冻结目标": "(FT)",
        "快速施法": "(FCR)",
        "快速格挡": "(FBR)",
        "格挡几率": "(CTB)",
        "耐久度": "(DUR)",
        "无形的": "(无法修复)",
        "击退": "(KB)",
        "需求": "(REQ)",
        "伤害": "(DMG)",
    },
    "zhTW": {
        "%+d%% 受到的傷害轉為法力": "(DTM)",
        "%+d%% 跑步 / 行走速度": "(FRW)",
        "附加 %d - %d 火焰傷害": "(FD)",
        "附加 %d - %d 冰寒傷害": "(CD)",
        "附加 %d - %d 電擊傷害": "(LD)",
        "附加 %d - %d 魔法傷害": "(MD)",
        "附加 %d - %d 毒素傷害": "(PD)",
        "%+d%% 機率擊中使怪物逃跑": "(Flee)",
        "%+d%% 機率造成開放傷口": "(OW)",
        "%+d%% 對不死怪物的傷害": "(DTU)",
        "%+d%% 機率造成粉碎打擊": "(CB)",
        "%+d 對不死怪物的準確率": "(ARU)",
        "附加 %d - %d 傷害": "(DMG)",
        "擊中竊取 %d%% 法力": "(LM)",
        "擊中竊取 %d%% 生命": "(LL)",
        "%+d 死靈法師技能等級": "(NEC)",
        "%+d%% 對惡魔的傷害": "(DTD)",
        "快速的跑步 / 行走速度": "(FRW)",
        "最快的跑步 / 行走速度": "(FRW)",
        "%+d 擊殺惡魔生命恢復": "(DLK)",
        "%+d%% 火焰技能傷害": "(FD)",
        "%+d%% 冰寒技能傷害": "(CD)",
        "%+d%% 閃電技能傷害": "(LD)",
        "%+d%% 毒素技能傷害": "(PD)",
        "%+d 火焰傷害最大值": "(Max FD)",
        "%+d 火焰傷害最小值": "(Min FD)",
        "%+d 電擊傷害最大值": "(Max LD)",
        "%+d 電擊傷害最小值": "(Min LD)",
        "%+d 冰寒傷害最大值": "(Max CD)",
        "%+d 冰寒傷害最小值": "(Min CD)",
        "%+d 亞馬遜技能等級": "(AMA)",
        "%+d 聖騎士技能等級": "(PAL)",
        "%+d 魔法使技能等級": "(SOR)",
        "%+d 野蠻人技能等級": "(BAR)",
        "%+d 毒素傷害最大值": "(Max PD)",
        "%+d 毒素傷害最小值": "(Min PD)",
        "%+d 對惡魔的準確率": "(ARD)",
        "%+d 德魯伊技能等級": "(DRU)",
        "%+d%% 防禦強化": "(EDef)",
        "%+d%% 打擊恢復": "(FHR)",
        "%+d%% 施法速度": "(FCR)",
        "%+d%% 格擋速度": "(FBR)",
        "%+d 擊殺法力恢復": "(EK)",
        "%+d%% 致命打擊": "(DS)",
        "%+d%% 傷害強化": "(EDmg)",
        "%+d 所有技能等級": "(All Skill)",
        "%+d 魔法傷害吸收": "(MDA)",
        "%+d 火焰傷害吸收": "(FDA)",
        "%+d 冰寒傷害吸收": "(CDA)",
        "%+d 電擊傷害吸收": "(LDA)",
        "%+d 毒素傷害吸收": "(PDA)",
        "%+d 擊殺生命恢復": "(LK)",
        "尋獲魔法物品機率提高": "(MF)",
        "%d%% 準確率加成": "(AR)",
        "%+d 刺客技能等級": "(ASN)",
        "所有商人的價格降低": "(-Price)",
        "殺死的怪物就此安息": "(RIP)",
        "怪物金幣掉落量提高": "(EG)",
        "對不死怪物的準確率": "(ARU)",
        "受到的物理傷害降低": "(DR)",
        "受到的物理傷害提高": "(DI)",
        "%+d 最大傷害": "(MAX)",
        "%+d 最小傷害": "(MIN)",
        "%+d 所有技能": "(All Skills)",
        "被凍結的時效減半": "(HFD)",
        "小幅攻擊速度提高": "(IAS)",
        "大幅攻擊速度提高": "(IAS)",
        "%+d 火焰吸收": "(FA)",
        "%+d 電擊吸收": "(LA)",
        "%+d 魔法吸收": "(MA)",
        "%+d 冰寒吸收": "(CA)",
        "%+d 精力上限": "(Max STA)",
        "%+d 火焰傷害": "(FD)",
        "%+d 冰寒傷害": "(CD)",
        "%+d 電擊傷害": "(LD)",
        "%+d 魔法傷害": "(MD)",
        "%+d 毒素傷害": "(PD)",
        "%+d 所有屬性": "(ATTR)",
        "%d%% 準確率": "(AR)",
        "%+d 準確率": "(AR)",
        "耐久度上限提高": "(Max DUR)",
        "中毒的時效縮短": "(PLR)",
        "中毒的時效減半": "(HPD)",
        "快速的打擊恢復": "(FHR)",
        "最快的打擊恢復": "(FHR)",
        "快速的施法速度": "(FCR)",
        "最快的施法速度": "(FCR)",
        "快速的格擋速度": "(FBR)",
        "最快的格擋速度": "(FBR)",
        "%d%% 傷害": "(DMG)",
        "擊中使目標目盲": "(HBT)",
        "對惡魔的準確率": "(ARD)",
        "%+d 力量": "(STR)",
        "%+d 敏捷": "(DEX)",
        "%+d 體能": "(VIT)",
        "%+d 能量": "(ENG)",
        "%+d 法力": "(Mana)",
        "%+d 防禦": "(DEF)",
        "%+d 生命": "(Life)",
        "生命上限提高": "(Max Life)",
        "法力上限提高": "(Max Mana)",
        "魔法傷害降低": "(MDR)",
        "格擋機率提高": "(CTB)",
        "無視目標防禦": "(ITD)",
        "防止怪物自療": "(PMH)",
        "火焰抗性上限": "(Max FR)",
        "冰寒抗性上限": "(Max CR)",
        "電擊抗性上限": "(Max LR)",
        "魔法抗性上限": "(Max MR)",
        "毒素抗性上限": "(Max PR)",
        "%+d 傷害": "(DMG)",
        "火焰傷害降低": "(FDR)",
        "冰寒傷害降低": "(CDR)",
        "電擊傷害降低": "(LDR)",
        "毒素傷害降低": "(PDR)",
        "獲得的經驗值": "(EXP)",
        "敵人冰寒抗性": "(-CR)",
        "敵人火焰抗性": "(-FR)",
        "敵人電擊抗性": "(-LR)",
        "敵人毒素抗性": "(-PR)",
        "對惡魔的傷害": "(DTD)",
        "加強準確率": "(AR)",
        "使目標減慢": "(Slow)",
        "% 準確率": "(AR)",
        "火焰抗性": "(FR)",
        "冰寒抗性": "(CR)",
        "電擊抗性": "(LR)",
        "魔法抗性": "(MR)",
        "毒素抗性": "(PR)",
        "生命回復": "(Life Rep)",
        "回復法力": "(Mana Rep)",
        "傷害降低": "(DR)",
        "照亮範圍": "(Light Radius)",
        "凍結目標": "(FT)",
        "精力恢復": "(Heal STA)",
        "法力恢復": "(Reg Mana)",
        "攻擊速度": "(IAS)",
        "火焰吸收": "(FA)",
        "電擊吸收": "(LA)",
        "魔法吸收": "(MA)",
        "冰寒吸收": "(CA)",
        "無法凍結": "(CBF)",
        "所有抗性": "(RES)",
        "格擋機率": "(CTB)",
        "耐久度": "(DUR)",
        "擊退": "(KB)",
        "需求": "(REQ)",
        "傷害": "(DMG)"
    }
}