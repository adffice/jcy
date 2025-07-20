import os
import json

# 获取用户的 Local AppData 路径
APPDATA_DIR = os.path.join(os.getenv("LOCALAPPDATA"), "D2R_Mod_jcy")
# Mod配置
SETTINGS_PATH = os.path.join(APPDATA_DIR, "settings.json")
# 多开器&账号配置
ACCOUNTS_PATH = os.path.join(APPDATA_DIR, "accounts.json")

def ensure_appdata_files():
    os.makedirs(APPDATA_DIR, exist_ok=True)

    for path in [SETTINGS_PATH, ACCOUNTS_PATH]:
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                json.dump({}, f, ensure_ascii=False, indent=2)