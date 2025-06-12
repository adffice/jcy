import tkinter as tk
import sys
import os
import shutil
import json
from tkinter import messagebox

# 从拆分后的 Model 和 View 文件中导入
from jcy_model import FeatureConfig, FeatureStateManager
from file_operations import FileOperations
from jcy_view import FeatureView

class FeatureController:
    def __init__(self, master):
        self.master = master
        self.base_path = self._get_base_path()

        self.feature_config = FeatureConfig(self.base_path)
        self.file_operations = FileOperations(self.feature_config)
        self.feature_state_manager = FeatureStateManager(self.feature_config)

        self.feature_view = FeatureView(master, self.feature_config.all_features_config, self)

        self.current_states = {}
        # 保持用户原有的 toggle_handlers 命名
        self.toggle_handlers = {}
        # 初始化 group_handlers
        self.group_handlers = {} 
        self._setup_feature_handlers()
        self.dialogs = "" 

        self.feature_state_manager.load_settings()
        self.current_states.update(self.feature_state_manager.loaded_states)
        self.feature_view.update_ui_state(self.current_states)

    def _get_base_path(self):
        """获取应用程序的根目录。"""
        if getattr(sys, 'frozen', False):
            # 当应用程序被打包成 exe 时
            return os.path.dirname(sys.executable)
        else:
            # 当从 Python 脚本运行时
            return os.path.dirname(os.path.abspath(__file__))

    def _setup_feature_handlers(self):
        """
        设置功能ID与对应的操作方法的映射。
        """
        # 独立功能
        self.toggle_handlers = {
            # "MINI方块"
            "FEATURE_ID_01": self.file_operations.toggle_mini_cube,
            # "掉落光柱"
            "FEATURE_ID_02": self.file_operations.toggle_droped_highlight,
            # "符文编号贴图"
            "FEATURE_ID_03": self.file_operations.toggle_rune_sprite,
            # "箱子高亮"
            "FEATURE_ID_04": self.file_operations.toggle_chest_highlight,
            # "入口/小站光柱"
            "FEATURE_ID_05": self.file_operations.toggle_entrance_arrow,
            # "屏蔽垃圾装备"
            "FEATURE_ID_06": self.file_operations.toggle_low_quality,
            # "屏蔽垃圾杂物" 
            "FEATURE_ID_07": self.file_operations.toggle_other_misc, 
            # "照亮玩家四周"
            "FEATURE_ID_08": self.file_operations.toggle_player_light,
            # "马赛克护眼"
            "FEATURE_ID_09": self.file_operations.toggle_no_mosaic_sin,
            # "按ESC直接退回大厅"
            "FEATURE_ID_10": self.file_operations.toggle_escape,
            # "屏蔽地狱火炬火焰风暴特效"
            "FEATURE_ID_11": self.file_operations.toggle_hellfire_torch,
            # "屏蔽火焰之河岩浆特效"
            "FEATURE_ID_12": self.file_operations.toggle_lava_river_flow,
            # "删除开门动画,极速进站",
            "FEATURE_ID_13": self.file_operations.toggle_load_screen_panel,
            # "魔法箭特效"
            "FEATURE_ID_14": self.file_operations.toggle_magic_arrow,
            # "6BOSS钥匙皮肤"
            "FEATURE_ID_15": self.file_operations.toggle_mephisto_key,
            # "A2贤者之谷小站增加塔墓标记 A3拆除崔凡克议会墙屋 A4拆除混沌庇护所大门 A5拆除毁灭王座石柱"
            "FEATURE_ID_16": self.file_operations.toggle_hd_env_presets,
            # "变色精英怪"
            "FEATURE_ID_17": self.file_operations.toggle_hd_global_palette_randtransforms_json,
            # "特殊词缀装备变色"
            "FEATURE_ID_18": self.file_operations.toggle_global_excel_affixes,
            # "经验条变色"
            "FEATURE_ID_19": self.file_operations.toggle_experience_bar,
            # "咒符/符文/技能提示音"
            "FEATURE_ID_20": self.file_operations.toggle_sound,
            # "尼拉塞克指示"
            "FEATURE_ID_21": self.file_operations.toggle_nihlathak_pointer,
            # "兵营指示"
            "FEATURE_ID_22": self.file_operations.toggle_barracks_pointer,
            # "屏蔽动画"
            "FEATURE_ID_23": self.file_operations.toggle_hd_local_video,
            # "点击角色进游戏(最高难度)"
            "FEATURE_ID_24": self.file_operations.toggle_quick_game,
        }

        # 分组功能处理函数 - 使用新的 group_id (适配 jcy_model.py 的新结构)
        # 键是 group_id (例如 "GROUP_FEATURES_01")，值是处理该组选中的函数
        self.group_handlers = {
            # "传送门皮肤"
            "GROUP_FEATURES_01": self.file_operations.toggle_town_portal,
        }

    def apply_settings(self):
        """
        应用所有功能设置，执行文件操作。
        此方法被“应用设置”按钮调用。
        保留用户原有的比较逻辑和对话框显示机制。
        """
        self.dialogs = "" # 每次应用设置前清空 dialogs
        changes_detected = False

        # -------------------- 独立功能 (Checkbutton) --------------------
        for feature_id, description in self.feature_config.all_features_config["display_features"].items():
            current_value = self.current_states.get(feature_id)
            loaded_value = self.feature_state_manager.loaded_states.get(feature_id)
            # 只有当 current_value 存在且与 loaded_value 不同时才处理
            if current_value is not None and current_value != loaded_value:
                changes_detected = True
                if feature_id in self.toggle_handlers:
                    # 执行实际的文件操作
                    result = self.toggle_handlers[feature_id](current_value) # current_value 即 enable/disable
                    self.dialogs += f"{description} = {"开启" if current_value else "关闭"} 操作文件数量 {result[0]}/{result[1]} \n"

        for feature_id, description in self.feature_config.all_features_config["function_features"].items():
            current_value = self.current_states.get(feature_id)
            loaded_value = self.feature_state_manager.loaded_states.get(feature_id)
            # 只有当 current_value 存在且与 loaded_value 不同时才处理
            if current_value is not None and current_value != loaded_value:
                changes_detected = True
                if feature_id in self.toggle_handlers:
                    # 执行实际的文件操作
                    result = self.toggle_handlers[feature_id](current_value) # current_value 即 enable/disable
                    self.dialogs += f"{description} = {"开启" if current_value else "关闭"} 操作文件数量 {result[0]}/{result[1]} \n"

        # -------------------- 分组功能 (Radiobutton) --------------------
        for group_id, group_info in self.feature_config.all_features_config["group_features"].items():
            current_value = self.current_states.get(group_id) # 获取选中项的 param_key
            loaded_value = self.feature_state_manager.loaded_states.get(group_id)

            # 只有当 current_value 存在且与 loaded_value 不同时才处理
            if current_value is not None and current_value != loaded_value:
                changes_detected = True
                # 找到选中参数的描述文本
                selected_description = next((param_dict[current_value] for param_dict in group_info["params"] if current_value in param_dict), current_value)
                if group_id in self.group_handlers:
                    # 执行实际的文件操作
                    result = self.group_handlers[group_id](current_value) # current_value 即 selected_param_key
                    self.dialogs += f"{group_info['text']} = {selected_description} 操作文件数量 {result[0]}/{result[1]} \n"

        # 保存当前状态到 settings.json
        self.feature_state_manager.save_settings(self.current_states)
        # 核心：保存后，立即更新 loaded_states，使其反映当前已保存的状态
        self.feature_state_manager.loaded_states.update(self.current_states) # 使用 update 方法

        # 显示结果
        if changes_detected:
            messagebox.showinfo("设置已应用", self.dialogs)
        else:
            messagebox.showinfo("完成", "无变化!")

    def execute_feature_action(self, feature_id: str, enable: bool):
        """
        执行独立功能的开关操作。此方法由 jcy_view.py 直接调用。
        它现在只更新内存中的 current_states，不执行文件操作。
        """
        self.current_states[feature_id] = enable
        # 此时不进行文件操作，不累加 self.dialogs

    def execute_group_action(self, group_id: str, selected_param_key: str):
        """
        执行分组功能的选中操作。此方法由 jcy_view.py 直接调用。
        它现在只更新内存中的 current_states，不执行文件操作。
        """
        self.current_states[group_id] = selected_param_key
        # 此时不进行文件操作，不累加 self.dialogs

    

if __name__ == "__main__":
    root = tk.Tk()
    app = FeatureController(root)
    root.mainloop()