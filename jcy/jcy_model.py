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
            "display_features": { 
                "FEATURE_ID_100": "掉落光柱",
                "FEATURE_ID_101": "符文编号贴图",
                "FEATURE_ID_102": "箱子高亮",
                "FEATURE_ID_103": "入口/小站光柱",
                "FEATURE_ID_104": "马赛克护眼",
                "FEATURE_ID_105": "屏蔽地狱火炬火焰风暴特效",
                "FEATURE_ID_106": "屏蔽火焰之河岩浆特效",
                "FEATURE_ID_107": "屏蔽开门动画,极速进站",
                "FEATURE_ID_108": "弓箭/弩箭/老鼠刺/剥皮吹箭->火箭特效",
                "FEATURE_ID_109": "6BOSS钥匙皮肤+掉落光柱",
                "FEATURE_ID_110": "展示A2贤者之谷小站塔墓标记 屏蔽A3崔凡克议会墙屋 屏蔽A4混沌庇护所大门 屏蔽A5毁灭王座石柱",
                "FEATURE_ID_111": "经验条变色",
                "FEATURE_ID_112": "屏蔽影散隐身特效",
                "FEATURE_ID_113": "骷髅火焰刀+圣盾特效",
                "FEATURE_ID_114": "隐藏头盔类装备外观",
                "FEATURE_ID_115": "投掷标枪->闪电枪特效",
                "FEATURE_ID_116": "投掷飞刀->闪电尾特效",
                "FEATURE_ID_117": "画面变亮",
                "FEATURE_ID_118": "怪物血条加宽加高",
                "FEATURE_ID_119": "德鲁伊飓风术特效",
                "FEATURE_ID_120": "屏蔽雷云风暴吓人特效",
                "FEATURE_ID_121": "降低闪电新星亮度",

            },
            "function_features": { 
                "FEATURE_ID_200": "MINI方块",
                "FEATURE_ID_201": "屏蔽垃圾装备",
                "FEATURE_ID_202": "屏蔽垃圾杂物",
                "FEATURE_ID_203": "按ESC直接退回大厅",
                "FEATURE_ID_204": "变色精英怪",
                "FEATURE_ID_205": "特殊词缀装备变色",
                "FEATURE_ID_206": "咒符/符文/技能结束提示音",
                "FEATURE_ID_207": "尼拉塞克指示",
                "FEATURE_ID_208": "兵营指示",
                "FEATURE_ID_209": "屏蔽动画",
                "FEATURE_ID_210": "点击角色进游戏(最高难度)",
                "FEATURE_ID_211": "更大的好友菜单",
                "FEATURE_ID_212": "怪物光源+危险标识",
                "FEATURE_ID_213": "技能图标(附魔/速度爆发/影散/BO/刺客聚气/狼之印记/熊之印记)",
                "FEATURE_ID_214": "火焰之河信标",
                "FEATURE_ID_215": "任务BOSS红圈引导",
                "FEATURE_ID_216": "经验/宝石祭坛特效",
                
            },
            "group_features": {
                "FEATURE_ID_300": {
                    "text": "传送门皮肤",
                    "params": [
                        {"default":"原版蓝门"},
                        {"red":"原版红门"},
                        {"blue":"双圈蓝门"},
                        {"red2":"单圈红门"},
                    ],
                    "default_key": "default"
                },
                "FEATURE_ID_301": {
                    "text": "传送术皮肤",
                    "params": [
                        {"default":"原版"},
                        {"ice":"冰霜"},
                        {"fire":"火焰"},
                    ],
                    "default_key": "default"
                },
            },
            "range_features" : {
                "FEATURE_ID_400": "照亮范围"
            }
        }

        self.base_path = base_path
        self.dir_mod = os.path.join(self.base_path, "jcy.mpq")
        self.settings_file = os.path.join(self.dir_mod, "settings.json")

        # ---初始化默认功能状态---
        self.default_feature_states = {
            **{fid: False for fid in self.all_features_config["display_features"]},
            **{fid: False for fid in self.all_features_config["function_features"]},
        }
        
        for group_id, group_info in self.all_features_config["group_features"].items(): 
            if group_info["params"]: 
                first_param_dict = group_info["params"][0]
                first_param_key = next(iter(first_param_dict.keys()))
                self.default_feature_states[group_id] = first_param_key
            else:
                self.default_feature_states[group_id] = None
        
        for fid in self.all_features_config["range_features"]:
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

                for fid in self.config.all_features_config["display_features"]:
                    if fid not in self.loaded_states:
                        self.loaded_states[fid] = False

                for fid in self.config.all_features_config["function_features"]:
                    if fid not in self.loaded_states:
                        self.loaded_states[fid] = False

                for group_id, group_info in self.config.all_features_config["group_features"].items():
                    if group_id not in self.loaded_states: 
                        if group_info["params"]: 
                            first_param_dict = group_info["params"][0]
                            first_param_key = next(iter(first_param_dict.keys()))
                            self.loaded_states[group_id] = first_param_key
                        else:
                            self.loaded_states[group_id] = None

                for fid in self.config.all_features_config["range_features"]:
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
            for fid in self.config.all_features_config["display_features"]:
                if fid in current_states:
                    states_to_save[fid] = current_states[fid]

            for fid in self.config.all_features_config["function_features"]:
                if fid in current_states:
                    states_to_save[fid] = current_states[fid]

            for group_id in self.config.all_features_config["group_features"]:
                if group_id in current_states:
                    states_to_save[group_id] = current_states[group_id]
            
            for fid in self.config.all_features_config["range_features"]:
                if fid in current_states:
                    states_to_save[fid] = current_states[fid]

            with open(self.settings_file, 'w', encoding='utf-8') as f:
                json.dump(states_to_save, f, indent=4)
        except Exception as e:
            messagebox.showerror("错误", f"保存配置文件失败：{e}")