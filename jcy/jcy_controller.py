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
        
        self._handlers = {
            # 掉落光柱
            "FEATURE_ID_100": self.file_operations.toggle_droped_highlight, 
            # 符文编号贴图
            "FEATURE_ID_101": self.file_operations.toggle_rune_sprite, 
            # 箱子高亮
            "FEATURE_ID_102": self.file_operations.toggle_chest_highlight, 
            # 入口/小站光柱
            "FEATURE_ID_103": self.file_operations.toggle_entrance_arrow,
            # 马赛克护眼
            "FEATURE_ID_104": self.file_operations.toggle_no_mosaic_sin,
            # 屏蔽地狱火炬火焰风暴特效
            "FEATURE_ID_105": self.file_operations.toggle_hellfire_torch,
            # 屏蔽火焰之河岩浆特效
            "FEATURE_ID_106": self.file_operations.toggle_lava_river_flow,
            # 屏蔽开门动画,极速进站
            "FEATURE_ID_107": self.file_operations.toggle_load_screen_panel,
            # 魔法箭特效
            "FEATURE_ID_108": self.file_operations.toggle_magic_arrow,
            # 6BOSS钥匙皮肤+掉落光柱
            "FEATURE_ID_109": self.file_operations.toggle_mephisto_key,
            # 展示A2贤者之谷小站塔墓标记 屏蔽A3崔凡克议会墙屋 屏蔽A4混沌庇护所大门 屏蔽A5毁灭王座石柱
            "FEATURE_ID_110": self.file_operations.toggle_hd_env_presets,
            # 经验条变色
            "FEATURE_ID_111": self.file_operations.toggle_experience_bar,


            # MINI方块
            "FEATURE_ID_200": self.file_operations.toggle_mini_cube,
            # 屏蔽垃圾装备
            "FEATURE_ID_201": self.file_operations.toggle_low_quality,
            # 屏蔽垃圾杂物
            "FEATURE_ID_202": self.file_operations.toggle_other_misc, 
            # 按ESC直接退回大厅
            "FEATURE_ID_203": self.file_operations.toggle_escape,
            # 变色精英怪
            "FEATURE_ID_204": self.file_operations.toggle_hd_global_palette_randtransforms_json,
            # 特殊词缀装备变色
            "FEATURE_ID_205": self.file_operations.toggle_global_excel_affixes,
            # 咒符/符文/技能结束提示音
            "FEATURE_ID_206": self.file_operations.toggle_sound,
            # 尼拉塞克指示
            "FEATURE_ID_207": self.file_operations.toggle_nihlathak_pointer,
            # 兵营指示
            "FEATURE_ID_208": self.file_operations.toggle_barracks_pointer,
            # 屏蔽动画
            "FEATURE_ID_209": self.file_operations.toggle_hd_local_video,
            # 点击角色进游戏(最高难度)
            "FEATURE_ID_210": self.file_operations.toggle_quick_game,
            # 更大的好友菜单
            "FEATURE_ID_211": self.file_operations.toggle_context_menu,
            # 怪物光源+危险标识
            "FEATURE_ID_212": self.file_operations.toggle_character_enemy,
            # 技能图标(附魔/速度爆发/影散/BO/刺客聚气)
            "FEATURE_ID_213": self.file_operations.toggle_skill_logo,
            
            
            # 传送门皮肤
            "FEATURE_ID_300": self.file_operations.select_town_portal,
            
            
            # 照亮范围
            "FEATURE_ID_400": self.file_operations.modify_character_player,
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
                if feature_id in self._handlers:
                    # 执行实际的文件操作
                    result = self._handlers[feature_id](current_value) 
                    self.dialogs += f"{description} = {"开启" if current_value else "关闭"} 操作文件数量 {result[0]}/{result[1]} \n"

        for feature_id, description in self.feature_config.all_features_config["function_features"].items():
            current_value = self.current_states.get(feature_id)
            loaded_value = self.feature_state_manager.loaded_states.get(feature_id)
            # 只有当 current_value 存在且与 loaded_value 不同时才处理
            if current_value is not None and current_value != loaded_value:
                changes_detected = True
                if feature_id in self._handlers:
                    # 执行实际的文件操作
                    result = self._handlers[feature_id](current_value) 
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
                if group_id in self._handlers:
                    # 执行实际的文件操作
                    result = self._handlers[group_id](current_value) 
                    self.dialogs += f"{group_info['text']} = {selected_description} 操作文件数量 {result[0]}/{result[1]} \n"

        #  -------------------- 区间功能 (Spinbox) --------------------
        for feature_id, description in self.feature_config.all_features_config["range_features"].items():
            current_value = self.current_states.get(feature_id)
            loaded_value = self.feature_state_manager.loaded_states.get(feature_id)
            # 只有当 current_value 存在且与 loaded_value 不同时才处理
            if current_value is not None and current_value != loaded_value:
                changes_detected = True
                if feature_id in self._handlers:
                    # 执行实际的文件操作
                    result = self._handlers[feature_id](current_value) 
                    self.dialogs += f"{description} = {current_value} 操作文件数量 {result[0]}/{result[1]} \n"

        # 保存当前状态到 settings.json
        self.feature_state_manager.save_settings(self.current_states)
        # 核心：保存后，立即更新 loaded_states，使其反映当前已保存的状态
        self.feature_state_manager.loaded_states.update(self.current_states) # 使用 update 方法

        # 显示结果
        if changes_detected:
            messagebox.showinfo("设置已应用", self.dialogs)
        else:
            messagebox.showinfo("完成", "无变化!")

    def execute_feature_action(self, feature_id: str, value):
        self.current_states[feature_id] = value

if __name__ == "__main__":
    root = tk.Tk()
    app = FeatureController(root)
    root.mainloop()