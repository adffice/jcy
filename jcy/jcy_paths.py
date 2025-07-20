import os

# 获取用户的 Local AppData 路径
APPDATA_DIR = os.path.join(os.getenv("LOCALAPPDATA"), "D2R_Mod_jcy")
# Mod配置
SETTINGS_PATH = os.path.join(APPDATA_DIR, "settings.json")
# 多开器&账号配置
ACCOUNTS_PATH = os.path.join(APPDATA_DIR, "accounts.json")