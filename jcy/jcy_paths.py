import os
from pathlib import Path
import json
import sys
import shutil
from jcy_constants import APP_DATA_DIR, SETTINGS_FILE, ACCOUNTS_FILE, VERSION_FILE, APP_VERSION

# 路径定义
APP_DATA_PATH = Path(os.getenv("LOCALAPPDATA")) / APP_DATA_DIR
SETTINGS_PATH = APP_DATA_PATH / SETTINGS_FILE
ACCOUNTS_PATH = APP_DATA_PATH / ACCOUNTS_FILE
VERSION_PATH = APP_DATA_PATH / VERSION_FILE

def resource_path(relative_path: str) -> Path:
    """获取资源的绝对路径（适配打包和开发模式）"""
    if getattr(sys, '_MEIPASS', None):
        base_path = Path(sys._MEIPASS)
    else:
        base_path = Path(__file__).parent
    return base_path / relative_path

def ensure_appdata_files() -> bool:
    """返回是否执行了初始化"""
    initialized = False
    
    if not VERSION_PATH.exists():
        update_config_version()
        print("[DEBUG] 创建新版本文件")
        initialized = True
    
    if not SETTINGS_PATH.exists():
        shutil.copy(resource_path("assets/settings.json"), SETTINGS_PATH)
        print("[DEBUG] 初始化默认配置")
        initialized = True
        
    return initialized

def check_config_version() -> bool:
    """增强版版本检查"""
    if not VERSION_PATH.exists():
        print("[DEBUG] 版本文件不存在")
        return False
        
    saved_version = VERSION_PATH.read_text().strip()
    print(f"[DEBUG] 版本检查: 保存版本={saved_version} 当前版本={APP_VERSION}")
    return saved_version == APP_VERSION

def update_config_version():
    """更新配置文件版本记录"""
    VERSION_PATH.write_text(APP_VERSION, encoding='utf-8')

def load_default_config() -> dict:
    """从assets加载默认配置"""
    default_path = resource_path("assets/settings.json")
    with open(default_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def merge_configs(default: dict, user: dict) -> tuple[dict, dict]:
    """
    安全合并配置
    Returns:
        tuple: (merged_config, diff_dict)
    """
    diff = {'added': [], 'modified': []}
    merged = default.copy()
    
    # 识别新增/修改项
    for key in set(default) | set(user):
        if key not in user:
            diff['added'].append(key)
        elif user[key] != default.get(key):
            diff['modified'].append(key)
            merged[key] = user[key]  # 保留用户设置
    
    return merged, diff

# 导出所有需要的符号
__all__ = [
    'APP_DATA_PATH',
    'ensure_appdata_files',
    'check_config_version',
    'update_config_version',
    'load_default_config',
    'merge_configs'
]