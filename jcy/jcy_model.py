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
            "standalone_features": { # 不分组的独立功能 (使用 Checkbutton)
                "FEATURE_ID_01": "MINI方块",
                "FEATURE_ID_02": "掉落光柱",
                "FEATURE_ID_03": "符文编号贴图",
                "FEATURE_ID_04": "箱子高亮",
                "FEATURE_ID_05": "入口/小站光柱",
                "FEATURE_ID_06": "屏蔽垃圾装备",
                "FEATURE_ID_07": "屏蔽垃圾杂物",
                "FEATURE_ID_08": "照亮玩家四周",
                "FEATURE_ID_09": "马赛克护眼",
                "FEATURE_ID_10": "按ESC直接退回大厅",
                "FEATURE_ID_11": "屏蔽地狱火炬火焰风暴特效",
                "FEATURE_ID_12": "屏蔽火焰之河岩浆特效",
                "FEATURE_ID_13": "屏蔽开门动画,极速进站",
                "FEATURE_ID_14": "魔法箭特效",
                "FEATURE_ID_15": "6BOSS钥匙皮肤+掉落光柱",
                "FEATURE_ID_16": "展示A2贤者之谷小站塔墓标记 屏蔽A3崔凡克议会墙屋 屏蔽A4混沌庇护所大门 屏蔽A5毁灭王座石柱",
                "FEATURE_ID_17": "变色精英怪",
                "FEATURE_ID_18": "特殊词缀装备变色",
                "FEATURE_ID_19": "经验条变色",
                "FEATURE_ID_20": "咒符/符文/技能提示音",
            },
            "group_features": { # 分组的互斥功能 (使用 Radiobutton)
                "GROUP_FEATURES_01": {
                    "text": "传送门皮肤",
                    "params": [
                        {"default":"原版蓝门"},
                        {"red":"原版红门"},
                        {"blue":"双圈蓝门"},
                        {"red2":"单圈红门"}
                    ]
                },
            }
        }

        self.base_path = base_path
        self.dir_mod = os.path.join(self.base_path, "jcy.mpq")
        self.settings_file = os.path.join(self.dir_mod, "settings.json")

        # 初始化默认功能状态
        self.default_feature_states = {}
        for fid in self.all_features_config["standalone_features"]:
            self.default_feature_states[fid] = False # 独立功能默认关闭

        # 分组功能：默认选中每个组的第一个选项的“参数对象key”
        for group_id, group_info in self.all_features_config["group_features"].items(): # 遍历组ID和组信息字典
            if group_info["params"]: # 如果组内有参数
                # 默认选中该组的第一个参数对象的key
                first_param_dict = group_info["params"][0]
                first_param_key = next(iter(first_param_dict.keys()))
                self.default_feature_states[group_id] = first_param_key
            else:
                self.default_feature_states[group_id] = None # 如果组内无功能，则为 None

class FeatureStateManager:
    """
    负责加载和保存功能的状态到文件。
    """
    def __init__(self, config: FeatureConfig):
        self.config = config
        self.settings_file = config.settings_file
        self.loaded_states = {}

    def load_settings(self):
        """从文件加载所有功能的状态"""
        if os.path.exists(self.settings_file):
            try:
                with open(self.settings_file, 'r', encoding='utf-8') as f:
                    self.loaded_states = json.load(f)

                # 确保所有独立功能都有状态，如果配置文件中缺少则使用默认值
                for fid in self.config.all_features_config["standalone_features"]:
                    if fid not in self.loaded_states:
                        self.loaded_states[fid] = False

                # 确保所有分组功能都有选中值，如果配置文件中缺少则使用默认值
                for group_id, group_info in self.config.all_features_config["group_features"].items():
                    if group_id not in self.loaded_states: # 检查选择值
                        if group_info["params"]: # 如果组内有参数
                            first_param_dict = group_info["params"][0]
                            first_param_key = next(iter(first_param_dict.keys()))
                            self.loaded_states[group_id] = first_param_key
                        else:
                            self.loaded_states[group_id] = None

            except json.JSONDecodeError:
                messagebox.showerror("错误", "配置文件损坏，已重置为默认设置。")
                self.loaded_states = self.config.default_feature_states.copy()
            except Exception as e:
                messagebox.showerror("错误", f"读取配置文件失败：{e}\n已重置为默认设置。")
                self.loaded_states = self.config.default_feature_states.copy()
        else:
            self.loaded_states = self.config.default_feature_states.copy()
            self.save_settings(self.loaded_states) # 首次加载时保存默认设置

    def save_settings(self, current_states):
        """将当前所有控制的状态保存到文件"""
        try:
            # 过滤掉不是功能ID或分组名称的键，以防保存不必要的临时状态
            states_to_save = {}
            for fid in self.config.all_features_config["standalone_features"]:
                if fid in current_states:
                    states_to_save[fid] = current_states[fid]

            for group_id in self.config.all_features_config["group_features"]:
                if group_id in current_states:
                    states_to_save[group_id] = current_states[group_id] # 只保存选中的 parameter object key

            with open(self.settings_file, 'w', encoding='utf-8') as f:
                json.dump(states_to_save, f, indent=4)
        except Exception as e:
            messagebox.showerror("错误", f"保存配置文件失败：{e}")