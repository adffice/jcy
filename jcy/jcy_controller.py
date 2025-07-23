import copy
import ctypes
import json
import os
import random
import requests
import sys
import threading
import time
import tkinter as tk
from datetime import datetime, timedelta, timezone
from tkinter import messagebox

import win32con
import win32gui

from file_operations import FileOperations
from jcy_constants import APP_FULL_NAME, ERROR_ALREADY_EXISTS, MUTEX_NAME, TERROR_ZONE, LANG
from jcy_model import FeatureConfig, FeatureStateManager
from jcy_paths import APP_DATA_PATH, ensure_appdata_files
from jcy_view import FeatureView, SysTrayIcon


def is_admin():
    """
    UAC检查
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
def bring_to_front():
    """
    唤出已有实例
    """
    hwnd = win32gui.FindWindow(None, APP_FULL_NAME)  # 标题必须匹配
    if hwnd:
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)  # 恢复窗口
        win32gui.SetForegroundWindow(hwnd)              # 前置窗口
        return True
    return False


# ---- UAC ----
if not is_admin():
    # 重新以管理员权限启动自己
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit(0)

# ---- 单例 ----
kernel32 = ctypes.windll.kernel32
mutex = kernel32.CreateMutexW(None, False, MUTEX_NAME)

last_error = kernel32.GetLastError()
if ERROR_ALREADY_EXISTS == last_error:
    print("已有实例运行中, 显示实例窗口...")
    bring_to_front()
    sys.exit(0)

# ---- 初始化配置文件 ----
ensure_appdata_files()

class FeatureController:
    def __init__(self, master):
        self.master = master
        self.base_path = self.get_data_file_path("")
        self.resource_path = self.get_resource_path("")

        self.feature_config = FeatureConfig(self.base_path)
        self.file_operations = FileOperations(self.feature_config)
        self.feature_state_manager = FeatureStateManager(self.feature_config)

        # ---- 同步APP信息到JSON ----
        self.file_operations.sync_app_data()

        self.current_states = {}

        # 新增：
        self.terror_zone_fetcher = TerrorZoneFetcher()

        # 初始化 UI（内部需要用到 current_states）
        self.feature_view = FeatureView(master, self.feature_config.all_features_config, self)
                
        self._setup_feature_handlers()
        self.dialogs = "" 

        self.feature_state_manager.load_settings()
        self.current_states = copy.deepcopy(self.feature_state_manager.loaded_states)
        self.feature_view.update_ui_state(self.current_states)

        

    def get_resource_path(self, relative_path):
        """获取资源文件的绝对路径，适配打包和开发环境"""
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    def get_data_file_path(self, relative_path):
        """获取运行时外部数据文件路径，通常在exe同目录或指定文件夹"""
        if getattr(sys, 'frozen', False):
            base_path = os.path.dirname(sys.executable)
        else:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
    
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
            # "入口 箭头指引",
            "142": self.file_operations.toggle_roomtiles_arrow,
            # "小站 箭头指引",
            "143": self.file_operations.toggle_waypoint_arrow,
            
            
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
            # 符文皮肤
            "206": self.file_operations.select_rune_skin,
            

            #角色特效
            "301": self.file_operations.select_character_effects,


            # 照亮范围
            "401": self.file_operations.modify_character_player,
            # 22#+符文名称大小
            "402": self.file_operations.modify_rune_rectangle,

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
                    self.dialogs += f"{description} = {'开启' if current_value else '关闭'} 操作文件数量 {result[0]}/{result[1]} \n"



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

def start_win32_tray(root, ico_path):
    tray = SysTrayIcon(
        root=root,
        icon=ico_path,
        hover_text=APP_FULL_NAME,
        menu_options=[
            ("退出程序", SysTrayIcon.QUIT),
        ]
    )
    # 在新线程运行托盘事件循环
    threading.Thread(target=tray.run, daemon=True).start()
    return tray


class TerrorZoneFetcher:
    def __init__(self, n_times_per_hour=5):
        self.base_url = "https://asia.d2tz.info/terror_zone?mode=online"
        self.running = False
        self.first = True
        self.thread = None
        self.n_times_per_hour = n_times_per_hour
        self.output_file = os.path.join(APP_DATA_PATH, "terror_zone.json")
        os.makedirs(os.path.dirname(self.output_file), exist_ok=True)

    def fetch_once_with_retry(self, max_retries=9):
        """
        爬取TZ最新数据
        """
        for attempt in range(1, max_retries + 1):
            try:
                print(f"[尝试] 第 {attempt} 次抓取")
                response = requests.get(self.base_url, timeout=10)
                response.raise_for_status()
                json_data = response.json()

                # 1. 检查 status 和 data
                if json_data.get("status") != "ok" or not json_data.get("data"):
                    print(f"[失败] 数据格式异常: {json_data}")
                else:
                    # 2. 解析时间戳（UTC时间）
                    tz_time = json_data["data"][0]["time"]
                    target_hour = datetime.fromtimestamp(tz_time, tz=timezone.utc).hour

                    # 3. 当前 UTC 时间 + 1
                    current_hour = datetime.now(timezone.utc).hour
                    expected_hour = (current_hour + 1) % 24

                    # 4. 判断是否为“下一个小时”
                    if target_hour == expected_hour:
                        print("[成功] 恐怖区域数据抓取成功（为下一个小时）")
                        return json_data
                    else:
                        print(f"[失败] 数据未更新：目标小时={target_hour}，当前+1={expected_hour}")
            except Exception as e:
                print(f"[异常] 第 {attempt} 次抓取失败: {e}")

            time.sleep(random.randint(3, 10))

        print("[错误] 所有尝试均失败或数据未更新")
        return None

    def _run_fetch_loop(self, callback):
        print("[启动] 恐怖区域自动抓取线程已启动")
        self.running = True

        while self.running:
            if self.first:
                self.first = False
                print("[首次] 程序启动，立即执行一次抓取")
            else:
                now = datetime.now()
                target = now.replace(minute=0, second=30, microsecond=0)
                if now > target:
                    # 超过当前小时，推到下一个小时
                    next_hour = (now + timedelta(hours=1)).replace(minute=0, second=30, microsecond=0)
                    target = next_hour

                wait_seconds = (target - now).total_seconds()
                print(f"[等待] 距离下次整点触发还有 {int(wait_seconds)} 秒")
                time.sleep(wait_seconds)

                delay = random.randint(30, 90)
                print(f"[延迟] 随机延迟 {delay} 秒后开始抓取")
                time.sleep(delay)

            data = self.fetch_once_with_retry(max_retries=5)

            if data:
                try:
                    with open(self.output_file, "w", encoding="utf-8") as f:
                        json.dump(data, f, ensure_ascii=False, indent=2)
                    print(f"[保存] 数据已保存到 {self.output_file}")
                except Exception as e:
                    print(f"[错误] 保存数据失败: {e}")

                if callback:
                    callback(data)
            else:
                print("[提示] 当前时间点抓取失败，等待下个整点再尝试")

    def start_auto_fetch_thread(self, callback):
        if self.thread and self.thread.is_alive():
            print("[提示] 自动抓取线程已在运行")
            return

        self.thread = threading.Thread(target=self._run_fetch_loop, args=(callback,), daemon=True)
        self.thread.start()

    def stop(self):
        self.running = False

if not getattr(sys, 'frozen', False):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    root = tk.Tk()
    app = FeatureController(root)

    ico_path = app.get_resource_path("assets/bear.ico")
    root.iconbitmap(ico_path)
    
    def on_closing():
        if messagebox.askokcancel("退出", "确定要退出程序吗？"):
            root.destroy()
        else:
            # 取消关闭，不做操作
            pass

    root.protocol("WM_DELETE_WINDOW", on_closing)

    # 先创建托盘对象
    tray = start_win32_tray(root, ico_path)

    # 跨线程通知函数
    def show_notification_from_thread(title, message):
        root.after(0, lambda: tray.show_balloon(title, message))

    # 恐怖区域数据更新回调
    def notify_fetch_success(data):
        print("[通知] 恐怖区域数据更新成功！")
        try:
            rec = data["data"][0]
            raw_time = rec.get("time")
            zone_key = rec.get("zone")
            formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(raw_time)) if raw_time else "未知时间"
            
            zone_info = TERROR_ZONE.get(zone_key, {})
            zone_name = zone_info.get(LANG, "未知区域") if zone_info else f"未知区域（{zone_key}）"
            message = f"{formatted_time} {zone_name}"
        except Exception as e:
            print("[通知构造异常]", e)
            message = "恐怖区域数据更新成功，但部分信息解析失败。"

        show_notification_from_thread("恐怖区域已更新", message)

    # 启动自动获取恐怖区域数据的后台线程
    app.terror_zone_fetcher.start_auto_fetch_thread(notify_fetch_success)

    root.mainloop()