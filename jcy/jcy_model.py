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
                # "FEATURE_ID_13": "屏蔽督军山克死亡特效", 文件内容尚未分析清楚
                "FEATURE_ID_14": "魔法箭特效",
                "FEATURE_ID_15": "6BOSS钥匙皮肤",
                "FEATURE_ID_16": "A2贤者之谷小站增加塔墓标记 A3拆除崔凡克议会墙屋 A4拆除混沌庇护所大门 A5拆除毁灭王座石柱",
                "FEATURE_ID_17": "变色精英怪",
                "FEATURE_ID_18": "特殊词缀装备变色",
                "FEATURE_ID_19": "经验条变色",
                "FEATURE_ID_20": "咒符/符文/技能提示音",
                # "FEATURE_ID_21": "隐藏角色/物品装饰面板",
            },
            "feature_groups": { # 分组的互斥功能 (外层用 Checkbutton 开关，内层用 Radiobutton)
                # "显示模式": {
                #     "description": "开发测试中...不用点", # 为组添加一个描述，用于主开关的文本
                #     "features": { # 实际的 Radiobutton 选项
                #         "GROUP_ID_DISPLAY_A": "性能优先 (开发测试中...不用点)",
                #         "GROUP_ID_DISPLAY_B": "平衡模式 (开发测试中...不用点)",
                #         "GROUP_ID_DISPLAY_C": "外观优先 (开发测试中...不用点)",
                #     }
                # },
            }
        }
        
        self.default_feature_states = self._generate_default_states()
        self.base_path = base_path
        self.dir_mod = os.path.join(self.base_path, "jcy.mpq")

    def _generate_default_states(self):
        """生成默认功能状态字典。"""
        default_feature_states = {}
        # 独立功能
        for fid in self.all_features_config["standalone_features"].keys():
            default_feature_states[fid] = False
        
        # 分组功能：为每个组添加一个布尔开关的状态，以及一个选择值
        for group_name, group_info in self.all_features_config["feature_groups"].items():
            default_feature_states[f"_{group_name}_enabled"] = False # 组开关，默认禁用
            if group_info["features"]: # 确保 group_info["features"] 不为空
                first_feature_id = next(iter(group_info["features"].keys()))
                default_feature_states[group_name] = first_feature_id # 组内的默认选择
            else:
                default_feature_states[group_name] = None # 如果没有功能，设置None
        return default_feature_states

class FeatureStateManager:
    """
    负责加载和保存应用程序的功能设置状态。
    """
    def __init__(self, config: FeatureConfig):
        self.config = config
        self.config_dir = os.path.join(config.base_path, "jcy.mpq")
        self.settings_file = os.path.join(self.config_dir, "settings.json")
        os.makedirs(self.config_dir, exist_ok=True)
        self.loaded_states = {}

    def load_settings(self):
        """从 conf 目录加载上次保存的功能状态，如果不存在则使用默认值"""
        if os.path.exists(self.settings_file):
            try:
                with open(self.settings_file, 'r', encoding='utf-8') as f:
                    self.loaded_states = json.load(f)
                
                # 独立功能
                for fid in self.config.all_features_config["standalone_features"].keys():
                    if fid not in self.loaded_states:
                        self.loaded_states[fid] = False
                
                # 分组功能：加载开关状态和选择值
                for group_name, group_info in self.config.all_features_config["feature_groups"].items():
                    if f"_{group_name}_enabled" not in self.loaded_states: # 检查开关状态
                        self.loaded_states[f"_{group_name}_enabled"] = False 
                    if group_name not in self.loaded_states: # 检查选择值
                        if group_info["features"]:
                            self.loaded_states[group_name] = next(iter(group_info["features"].keys()))
                        else:
                            self.loaded_states[group_name] = None

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
            with open(self.settings_file, 'w', encoding='utf-8') as f:
                json.dump(current_states, f, indent=4)
        except IOError as e:
            messagebox.showerror("保存错误", f"无法保存设置：{e}\n请检查 '{self.config_dir}' 目录的写入权限。")