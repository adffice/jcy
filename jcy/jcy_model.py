import json
import os
import shutil
import sys
from tkinter import messagebox

class FeatureConfig:
    """
    管理所有功能配置、默认状态以及与功能相关的资源文件路径。
    """
    def __init__(self, base_path):
        self.all_features_config = {
            "checkbutton": {
                "101": "点击角色快速建立最高难度游戏",
                "102": "Esc=存儲並離開",
                "103": "更大的好友菜单",
                "104": "特殊词缀蓝装变色(红/绿)",
                "105": "入口/小站 箭头指引",
                "106": "经验祭坛/宝石祭坛 特效标识",
                "107": "暗黑2百科",
                "108": "物品栏+精品词缀",
                "109": "储物箱+精品词缀",
                "110": "赫拉迪姆方塊+符文升级公式",


                "111": "MINI方块常开 在蓝球之前",
                "112": "画面变亮",
                "113": "蓝色/金色/暗金色精英怪随机染色",
                "114": "怪物光源+危险标识",
                "115": "屏蔽 劣等的/損壞的/破舊的武器装备",
                "116": "屏蔽 杂物道具",
                "117": "咒符/22#+符文增加掉落光柱",
                "118": "咒符/22#+符文增加掉落提示音 & 技能结束提示音",
                "119": "技能图标(头顶:熊之印记/狼之印记 脚下:附魔/速度爆发+影散/BO 右侧:刺客聚气)",
                "120": "A1兵营/A4火焰之河/A5尼拉塞克/BOSS 指引",
                

                "121": "交互对象增加蓝色火苗",
                "122": "马赛克护眼",
                "123": "符文编号贴图",
                "124": "6BOSS钥匙皮肤+掉落光柱",
                "125": "屏蔽 开场/过场/结束动画",
                "126": "屏蔽 地狱火炬火焰风暴特效",
                "127": "屏蔽 A4火焰之河岩浆特效",
                "128": "屏蔽 A5督军山克死亡特效",
                "129": "屏蔽 开门动画,极速进站",
                "130": "展示 A2贤者之谷小站塔墓标记 & 屏蔽 A3崔凡克议会墙屋/A4混沌庇护所大门/A5毁灭王座石柱",


                "131": "经验条变色",
                "132": "屏蔽 影散隐身特效",
                "133": "屏蔽 头环类装备外观",
                "134": "屏蔽 雷云风暴吓人特效",
                "135": "降低 闪电新星亮度",
                "136": "怪物血条加宽加高",
                "137": "死灵召唤骷髅 火焰刀+圣盾特效",
                "138": "投掷标枪->闪电枪特效",
                "139": "投掷飞刀->闪电尾特效",
                "140": "德鲁伊飓风术 特效",
            },
            "radiobutton": {
                "201": {
                    "text": "佣兵图标位置",
                    "params": [
                        {"default":"原版"},
                        {"1":"左上角缩进"},
                        {"2":"红球之上"},
                        {"3":"红球之上上"},
                    ],
                    "default_key": "default"
                },
                "202": {
                    "text": "传送门皮肤",
                    "params": [
                        {"default":"原版蓝门"},
                        {"1":"原版红门"},
                        {"2":"双圈蓝门"},
                        {"3":"单圈红门"},
                    ],
                    "default_key": "default"
                },
                "203": {
                    "text": "传送术皮肤",
                    "params": [
                        {"default":"原版"},
                        {"1":"冰霜"},
                        {"2":"火焰"},
                    ],
                    "default_key": "default"
                },
                "204": {
                    "text": "弩/箭皮肤",
                    "params": [
                        {"default":"原皮"},
                        {"1":"魔法箭"},
                        {"2":"冷霜箭"},
                        {"3":"火焰箭"},
                    ],
                    "default_key": "default"
                },
                "205": {
                    "text": "老鼠刺针/剥皮吹箭皮肤",
                    "params": [
                        {"default":"原皮"},
                        {"1":"魔法箭"},
                        {"2":"冷霜箭"},
                        {"3":"火焰箭"},
                    ],
                    "default_key": "default"
                },
            },
            "spinbox" : {
                "301": "照亮范围"
            }
        }

        self.base_path = base_path
        self.dir_mod = os.path.join(self.base_path, "jcy.mpq")
        self.settings_file = os.path.join(self.dir_mod, "settings.json")

        # ---初始化默认功能状态---
        self.default_feature_states = {
            **{fid: False for fid in self.all_features_config["checkbutton"]}
        }
        
        for group_id, group_info in self.all_features_config["radiobutton"].items(): 
            if group_info["params"]: 
                first_param_dict = group_info["params"][0]
                first_param_key = next(iter(first_param_dict.keys()))
                self.default_feature_states[group_id] = first_param_key
            else:
                self.default_feature_states[group_id] = None
        
        for fid in self.all_features_config["spinbox"]:
            self.default_feature_states[fid] = 0
        

class FeatureStateManager:
    """
    配置文件操作类
    """
    def __init__(self, config: FeatureConfig):
        self.config = config
        self.settings_file = config.settings_file
        self.loaded_states = {}

    def load_settings(self):
        """
        读取配置文件
        """
        if os.path.exists(self.settings_file):
            try:
                with open(self.settings_file, 'r', encoding='utf-8') as f:
                    self.loaded_states = json.load(f)

                for fid in self.config.all_features_config["checkbutton"]:
                    if fid not in self.loaded_states:
                        self.loaded_states[fid] = False

                for group_id, group_info in self.config.all_features_config["radiobutton"].items():
                    if group_id not in self.loaded_states: 
                        if group_info["params"]: 
                            first_param_dict = group_info["params"][0]
                            first_param_key = next(iter(first_param_dict.keys()))
                            self.loaded_states[group_id] = first_param_key
                        else:
                            self.loaded_states[group_id] = None

                for fid in self.config.all_features_config["spinbox"]:
                    if fid not in self.loaded_states:
                        self.loaded_states[fid] = 0

            except json.JSONDecodeError:
                messagebox.showerror("错误", "配置文件损坏，已重置为默认设置。")
                self.loaded_states = self.config.default_feature_states.copy()
            except Exception as e:
                messagebox.showerror("错误", f"读取配置文件失败：{e}\n已重置为默认设置。")
                self.loaded_states = self.config.default_feature_states.copy()
        else:
            # 首次加载时保存默认设置
            self.loaded_states = self.config.default_feature_states.copy()
            self.save_settings(self.loaded_states) 

    def save_settings(self, current_states):
        """
        保存配置文件
        """
        try:
            # 过滤掉不是功能ID或分组名称的键，以防保存不必要的临时状态
            states_to_save = {}
            for fid in self.config.all_features_config["checkbutton"]:
                if fid in current_states:
                    states_to_save[fid] = current_states[fid]

            for group_id in self.config.all_features_config["radiobutton"]:
                if group_id in current_states:
                    states_to_save[group_id] = current_states[group_id]
            
            for fid in self.config.all_features_config["spinbox"]:
                if fid in current_states:
                    states_to_save[fid] = current_states[fid]

            with open(self.settings_file, 'w', encoding='utf-8') as f:
                json.dump(states_to_save, f, indent=4)
        except Exception as e:
            messagebox.showerror("错误", f"保存配置文件失败：{e}")