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
        self.feature_handlers = {}
        self._setup_feature_handlers()
        self.dialogs = "";

        self.feature_state_manager.load_settings()
        self.current_states.update(self.feature_state_manager.loaded_states)
        self.feature_view.update_ui_state(self.current_states)

    def _get_base_path(self):
        """获取应用程序的根目录。"""
        if getattr(sys, 'frozen', False):
            # 当应用程序被打包成 exe 时
            return os.path.dirname(sys.executable)
        else:
            # 当作为脚本运行时
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
        }

        # 分组功能：这里只处理组的开关状态，组内互斥选择的处理在 _handle_group_action 中
        self.group_handlers = {
            "显示模式": {
                "enable_group": lambda: self.feature_view._toggle_group_state("显示模式", True),
                "disable_group": lambda: self.feature_view._toggle_group_state("显示模式", False),
                "handle_selection": self._handle_display_mode,
            },
        }

    def on_control_change(self, feature_id, value):
        """
        当UI控件状态改变时调用，更新内部状态。
        """
        self.current_states[feature_id] = value

        # 对于组的开关，需要立即更新组内 Radiobutton 的启用/禁用状态
        if feature_id.startswith('_') and feature_id.endswith('_enabled'):
            group_name = feature_id[1:-8]
            self.group_handlers[group_name]["enable_group"]() if value else self.group_handlers[group_name]["disable_group"]()

    def apply_settings(self):
        """
        应用所有功能设置，执行文件操作。
        """
        self.dialogs = "";

        # 获取上次保存的状态，用于比较
        previous_states = self.feature_state_manager.loaded_states.copy()

        # 首先处理独立功能
        for fid, description in self.feature_config.all_features_config["standalone_features"].items():
            is_enabled = self.current_states.get(fid, False)
            previous_enabled = previous_states.get(fid, False)

            if is_enabled != previous_enabled: # 只有状态发生变化才执行
                _count = self.execute_feature_action(fid, is_enabled)
                self.dialogs += f"{"开启" if is_enabled else "关闭" } {description} 操作文件数量: {_count[0]}/{_count[1]}\n"

        # 然后处理分组功能
        for group_name, group_info in self.feature_config.all_features_config["feature_groups"].items():
            group_enabled_key = f"_{group_name}_enabled"
            is_group_enabled = self.current_states.get(group_enabled_key, False)
            previous_group_enabled = previous_states.get(group_enabled_key, False)

            selected_fid_in_group = self.current_states.get(group_name)
            previous_selected_fid_in_group = previous_states.get(group_name)

            # 比较组的开关状态
            if is_group_enabled != previous_group_enabled:
                if is_group_enabled:
                    # 组从禁用变为启用，如果选中了Radiobutton，则执行其操作
                    if selected_fid_in_group:
                        self.execute_group_action(group_name, selected_fid_in_group)
                    else:
                        messagebox.showwarning("警告", f"'{group_name}' 组已启用但未选择任何选项。该组将被视为禁用。")
                        self.feature_view.feature_vars[group_enabled_key].set(False) # 更新UI
                        self.current_states[group_enabled_key] = False # 更新内部状态
                        self._handle_group_disabled_action(group_name) # 执行禁用操作
                else:
                    # 组从启用变为禁用
                    self._handle_group_disabled_action(group_name)
                # 确保 Radiobutton 状态与 Group Checkbutton 同步
                self.group_handlers[group_name]["enable_group"]() if is_group_enabled else self.group_handlers[group_name]["disable_group"]()
            elif is_group_enabled and selected_fid_in_group != previous_selected_fid_in_group:
                # 组已启用，且组内的Radiobutton选择发生了变化
                self.execute_group_action(group_name, selected_fid_in_group)

        self.feature_state_manager.save_settings(self.current_states)
        # 核心修复：保存后，立即更新 loaded_states，使其反映当前已保存的状态
        self.feature_state_manager.loaded_states.update(self.current_states)

        if(self.dialogs != ''):
            messagebox.showinfo("完成", self.dialogs)
        else:
            messagebox.showinfo("完成", "无变化!")

    def execute_feature_action(self, feature_id: str, enable: bool):
        # 打印被调用的方法名
        return self.toggle_handlers[feature_id](enable)

    def execute_group_action(self, group_name: str, selected_feature_id: str):
        """
        执行分组功能的选中操作。
        """
        if group_name in self.group_handlers:
            # 打印被调用的方法名和参数
            self.group_handlers[group_name]["handle_selection"](selected_feature_id)

    def _handle_group_disabled_action(self, group_name: str):
        """
        处理当一个功能组被禁用时的操作。
        对于分组功能，当主开关被禁用时，需要执行清除操作。
        """
        # 这里放置当整个组被禁用时的具体清理逻辑
        # 例如，调用 FileOperations 中对应的禁用所有组内功能的方法
        # if group_name == "显示模式":
        #     self.file_operations.disable_all_display_modes() # 示例：需要你在 FileOperations 中实现
        # elif group_name == "电源策略":
        #     self.file_operations.reset_power_policy_to_default()
        pass # Placeholder for actual disabling logic

    # 以下是处理各个分组功能的具体策略方法
    def _handle_display_mode(self, selected_fid: str):
        group_info = self.feature_config.all_features_config['feature_groups']['显示模式']
        description = group_info['features'].get(selected_fid, selected_fid)
        # 根据 selected_fid 执行实际的文件操作
        if selected_fid == "GROUP_ID_DISPLAY_A":
            # 性能优先：可能删除或替换一些视觉效果文件
            pass
        elif selected_fid == "GROUP_ID_DISPLAY_B":
            # 平衡模式：恢复默认视觉效果
            pass
        elif selected_fid == "GROUP_ID_DISPLAY_C":
            # 外观优先：启用所有视觉效果文件
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = FeatureController(root)
    root.mainloop()