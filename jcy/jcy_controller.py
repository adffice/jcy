import copy
import json
import os
import shutil
import sys
import tkinter as tk
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

        self.current_states = {}
        # 初始化 UI（内部需要用到 current_states）
        self.feature_view = FeatureView(master, self.feature_config.all_features_config, self)

        self._setup_feature_handlers()
        self.dialogs = "" 

        self.feature_state_manager.load_settings()
        self.current_states = copy.deepcopy(self.feature_state_manager.loaded_states)
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
            # "点击角色快速建立最高难度游戏",
            "101": self.file_operations.toggle_quick_game,
            # "Esc=存儲並離開",
            "102": self.file_operations.toggle_escape,
            # "更大的好友菜单",
            "103": self.file_operations.toggle_context_menu,
            # "特殊词缀蓝装变色(红/绿)",
            "104": self.file_operations.toggle_global_excel_affixes,
            # "入口/小站 箭头指引",
            "105": self.file_operations.toggle_entrance_arrow,
            # "经验祭坛/宝石祭坛 特效标识",
            "106": self.file_operations.toggle_shrine,
            # "暗黑2百科",
            "107": self.file_operations.toogle_d2r_wiki,
            # "物品栏+精品词缀",
            "108": self.file_operations.toggle_inventory_expansion,
            # "储物箱+精品词缀",
            "109": self.file_operations.toggle_bank_expansion,
            # "赫拉迪姆方塊+符文升级公式",
            "110": self.file_operations.toogle_cube_formula,
            # "MINI方块常开before蓝球",
            "111": self.file_operations.toggle_mini_cube,
            # "画面变亮",
            "112": self.file_operations.toggle_env_vis,
            # "蓝怪/金怪/暗金怪随机染色",
            "113": self.file_operations.toggle_hd_global_palette_randtransforms_json,
            # "怪物光源+危险标识",
            "114": self.file_operations.toggle_character_enemy,
            # "屏蔽 劣等的/損壞的/破舊的武器装备",
            "115": self.file_operations.toggle_low_quality,
            # "屏蔽 杂物道具",
            "116": self.file_operations.toggle_other_misc, 
            # "咒符/22#+符文增加掉落光柱",
            "117": self.file_operations.toggle_droped_highlight, 
            # "咒符/22#+符文增加掉落提示音 & 技能结束提示音",
            "118": self.file_operations.toggle_sound,
            # "技能图标(头顶:熊之印记/狼之印记 脚下:附魔/速度爆发+影散/BO 右侧:刺客聚气)",
            "119": self.file_operations.toggle_skill_logo,
            # "A1兵营/A4火焰之河/A5尼拉塞克/BOSS 指引",
            "120": self.file_operations.toggle_pointer,
            # "交互对象增加蓝色火苗",
            "121": self.file_operations.toggle_chest_highlight, 
            # "马赛克护眼",
            "122": self.file_operations.toggle_no_mosaic_sin,
            # "符文编号贴图",
            "123": self.file_operations.toggle_rune_sprite, 
            # "6BOSS钥匙皮肤+掉落光柱",
            "124": self.file_operations.toggle_mephisto_key,
            # "屏蔽 开场/过场/结束动画",
            "125": self.file_operations.toggle_hd_local_video,
            # "屏蔽 地狱火炬火焰风暴特效",
            "126": self.file_operations.toggle_hellfire_torch,
            # "屏蔽 A4火焰之河岩浆特效",
            "127": self.file_operations.toggle_lava_river_flow,
            # "屏蔽 A5督军山克死亡特效",
            "128": self.file_operations.toggle_shenk,
            # "屏蔽 开门动画,极速进站",
            "129": self.file_operations.toggle_load_screen_panel,
            # "展示 A2贤者之谷小站塔墓标记 & 屏蔽 A3崔凡克议会墙屋/A4混沌庇护所大门/A5毁灭王座石柱",
            "130": self.file_operations.toggle_hd_env_presets,
            # "经验条变色",
            "131": self.file_operations.toggle_experience_bar,
            # "屏蔽 影散隐身特效",
            "132": self.file_operations.toggle_fade_dummy,
            # "屏蔽 头环类装备外观",
            "133": self.file_operations.toggle_circlet,
            # "屏蔽 雷云风暴吓人特效",
            "134": self.file_operations.toggle_lightningbolt_big,
            # "降低 闪电新星亮度",
            "135": self.file_operations.toggle_electric_nova,
            # "怪物血条加宽加高",
            "136": self.file_operations.toggle_monster_health,
            # "死灵召唤骷髅 火焰刀+圣盾特效",
            "137": self.file_operations.toggle_necroskeleton,
            # "投掷标枪->闪电枪特效",
            "138": self.file_operations.toggle_missiles_javelin,
            # "投掷飞刀->闪电尾特效",
            "139": self.file_operations.toggle_missiles_throw,
            # "德鲁伊飓风术 特效",
            "140": self.file_operations.toggle_hurricane,
            # "左键快速购买",
            "141": self.file_operations.toggle_quick_buy,
            
            
            # 佣兵图标位置
            "201": self.file_operations.select_hireables_panel,
            # 传送门皮肤
            "202": self.file_operations.select_town_portal,
            # 传送术皮肤
            "203": self.file_operations.select_teleport_skin,
            # 弩/箭皮肤
            "204": self.file_operations.select_arrow_skin,
            # 老鼠刺针/剥皮吹箭样式
            "205": self.file_operations.select_enemy_arrow_skin,
            

            #角色特效
            "301": self.file_operations.select_character_effects,


            # 照亮范围
            "401": self.file_operations.modify_character_player,

            # 道具屏蔽
            "501": self.file_operations.modify_item_names,
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
        for feature_id, description in self.feature_config.all_features_config["checkbutton"].items():
            current_value = self.current_states.get(feature_id)
            loaded_value = self.feature_state_manager.loaded_states.get(feature_id)
            if current_value is not None and current_value != loaded_value:
                changes_detected = True
                if feature_id in self._handlers:
                    result = self._handlers[feature_id](current_value) 
                    self.dialogs += f"{description} = {"开启" if current_value else "关闭"} 操作文件数量 {result[0]}/{result[1]} \n"


        # -------------------- 单选功能 (RadioGroup) --------------------
        for fid, info in self.feature_config.all_features_config["radiogroup"].items():
            current_value = self.current_states.get(fid)
            loaded_value = self.feature_state_manager.loaded_states.get(fid)
            if current_value is not None and current_value != loaded_value:
                changes_detected = True
                selected_description = next((param_dict[current_value] for param_dict in info["params"] if current_value in param_dict), current_value)
                if fid in self._handlers:
                    result = self._handlers[fid](current_value)
                    self.dialogs += f"{info['text']} = {selected_description} 操作文件数量 {result[0]}/{result[1]} \n"


        # -------------------- 多选功能 (CheckGroup) --------------------
        for fid, info in self.feature_config.all_features_config["checkgroup"].items():
            current_value = self.current_states.get(fid)
            loaded_value = self.feature_state_manager.loaded_states.get(fid)
            if current_value is not None and current_value != loaded_value:
                changes_detected = True
                if fid in self._handlers:
                    result = self._handlers[fid](current_value)
                    self.dialogs += f"{info['text']} 操作文件数量 {result[0]}/{result[1]} \n"


        #  -------------------- 区间功能 (Spinbox) --------------------
        for feature_id, description in self.feature_config.all_features_config["spinbox"].items():
            current_value = self.current_states.get(feature_id)
            loaded_value = self.feature_state_manager.loaded_states.get(feature_id)
            if current_value is not None and current_value != loaded_value:
                changes_detected = True
                if feature_id in self._handlers:
                    result = self._handlers[feature_id](current_value) 
                    self.dialogs += f"{description} = {current_value} 操作文件数量 {result[0]}/{result[1]} \n"

        # -- 屏蔽道具 --
        for fid, info in self.feature_config.all_features_config["checktable"].items():
            current_value = self.current_states.get(fid)
            loaded_value = self.feature_state_manager.loaded_states.get(fid)
            if current_value is not None and current_value != loaded_value:
                changes_detected = True
                if fid in self._handlers:
                    result = self._handlers[fid](current_value)
                    self.dialogs += f"{info} 操作文件数量 {result[0]}/{result[1]} \n"
        

        # 保存当前状态到 settings.json
        self.feature_state_manager.save_settings(self.current_states)
        # 核心：保存后，立即更新 loaded_states，使其反映当前已保存的状态
        # self.feature_state_manager.loaded_states.update(self.current_states) # 使用 update 方法
        self.feature_state_manager.loaded_states = copy.deepcopy(self.current_states)

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