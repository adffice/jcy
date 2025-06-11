import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class FeatureView:
    def __init__(self, master, all_features_config, controller):
        self.master = master
        self.all_features_config = all_features_config
        self.controller = controller

        master.title("jcy MOD 控制器")
        master.geometry("600x700")

        self.feature_vars = {}  # 存储所有 Checkbutton 和 Radiobutton 的 Tkinter 变量
        self.group_radio_buttons = {} # 存储每个组的 Radiobutton 列表，用于批量启用/禁用
        self._create_ui()

    def _create_ui(self):
        # 创建 Notebook (Tabbed Interface)
        notebook = ttk.Notebook(self.master)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # 创建“独立功能”选项卡
        standalone_tab = ttk.Frame(notebook)
        notebook.add(standalone_tab, text=" 开关策略 ")

        # 创建“分组的互斥功能”选项卡
        grouped_tab = ttk.Frame(notebook)
        notebook.add(grouped_tab, text=" 组策略 ")

        # --- 独立功能 (Standalone Features) ---
        # 移除 # 为独立功能创建可滚动区域 的代码块，直接在 standalone_tab 中放置控件
        standalone_features = self.all_features_config.get("standalone_features", {})
        for fid, description in standalone_features.items():
            var = tk.BooleanVar(value=False)
            self.feature_vars[fid] = var
            cb = ttk.Checkbutton(standalone_tab, # 直接放置在 standalone_tab
                                 text=description,
                                 variable=var,
                                 command=lambda f=fid, v=var: self.controller.on_control_change(f, v.get()))
            cb.pack(anchor=tk.W, pady=2)

        # --- 分组的互斥功能 (Grouped Mutually Exclusive Features) ---
        # 移除 # 为分组功能创建可滚动区域 的代码块，直接在 grouped_tab 中放置控件
        feature_groups = self.all_features_config.get("feature_groups", {})
        for group_name, group_info in feature_groups.items():
            group_frame = ttk.LabelFrame(grouped_tab, text=group_name, padding=(10, 5)) # 直接放置在 grouped_tab
            group_frame.pack(fill=tk.X, padx=5, pady=5, anchor=tk.N)

            # 每个组一个 Checkbutton 用于启用/禁用整个组
            enabled_var = tk.BooleanVar(value=False)
            self.feature_vars[f"_{group_name}_enabled"] = enabled_var # 存储组的开关状态变量
            group_checkbutton = ttk.Checkbutton(group_frame,
                                                text=f"启用 {group_name} 功能",
                                                variable=enabled_var,
                                                command=lambda g=group_name, v=enabled_var: self.controller.on_control_change(f"_{g}_enabled", v.get()))
            group_checkbutton.pack(anchor=tk.W, pady=2)

            # Radiobutton 组
            radio_var = tk.StringVar(value="")
            self.feature_vars[group_name] = radio_var # 存储 Radiobutton 的选择值
            self.group_radio_buttons[group_name] = [] # 初始化列表

            for fid, description in group_info["features"].items():
                rb = ttk.Radiobutton(group_frame,
                                     text=description,
                                     variable=radio_var,
                                     value=fid,
                                     command=lambda g=group_name, f=fid: self.controller.on_control_change(g, f))
                rb.pack(anchor=tk.W, padx=20, pady=1)
                self.group_radio_buttons[group_name].append(rb) # 将 Radiobutton 实例添加到列表

            # 初始禁用状态
            self._toggle_group_state(group_name, False) # 初始时，所有组内 Radiobutton 都是禁用状态

        # 应用设置按钮
        apply_button = ttk.Button(self.master, text="应用设置", command=self.controller.apply_settings)
        apply_button.pack(pady=10)


    def _toggle_group_state(self, group_name: str, enabled: bool):
        """
        根据组的 Checkbutton 状态启用或禁用组内的 Radiobutton。
        """
        if group_name in self.group_radio_buttons:
            for radio_button in self.group_radio_buttons[group_name]:
                radio_button.configure(state=tk.NORMAL if enabled else tk.DISABLED)

    def update_ui_state(self, current_states: dict):
        """
        根据加载的设置更新 UI 元素的状态。
        """
        for fid, var in self.feature_vars.items():
            if fid.startswith('_') and fid.endswith('_enabled'): # 处理组的开关
                group_name = fid[1:-8] # 提取组名
                enabled = current_states.get(fid, False)
                var.set(enabled)
                self._toggle_group_state(group_name, enabled)
            elif fid in self.all_features_config["standalone_features"]: # 独立功能
                var.set(current_states.get(fid, False))
            elif fid in self.all_features_config["feature_groups"]: # 分组功能
                selected_fid = current_states.get(fid, "")
                var.set(selected_fid)