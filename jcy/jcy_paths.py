import os
import json
import sys
import shutil
from jcy_constants import APP_DATA_DIR, SETTINGS_FILE, ACCOUNTS_FILE

# 获取用户的 Local AppData 路径
APP_DATA_PATH = os.path.join(os.getenv("LOCALAPPDATA"), APP_DATA_DIR)
# Mod配置
SETTINGS_PATH = os.path.join(APP_DATA_PATH, SETTINGS_FILE)
# 多开器&账号配置
ACCOUNTS_PATH = os.path.join(APP_DATA_PATH, ACCOUNTS_FILE)

def resource_path(relative_path):
    """
    获取打包后资源的路径：
    - 开发环境：直接使用相对路径
    - 打包环境（PyInstaller）：使用 _MEIPASS 临时目录
    """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return relative_path

def ensure_appdata_files():
    """
    确保 AppData 目录中存在 settings.json 和 accounts.json：
    - settings.json：若不存在则从 assets/ 中复制默认配置
    - accounts.json：若不存在则创建一个空字典文件
    """
    os.makedirs(APP_DATA_PATH, exist_ok=True)

    # settings.json不存在,则使用默认文件
    if not os.path.exists(SETTINGS_PATH):
        default_settings = resource_path("assets/settings.json")
        shutil.copy(default_settings, SETTINGS_PATH)

    # 若不存在 accounts.json，则初始化为空字典
    if not os.path.exists(ACCOUNTS_PATH):
        with open(ACCOUNTS_PATH, "w", encoding="utf-8") as f:
            json.dump({}, f, ensure_ascii=False, indent=2)