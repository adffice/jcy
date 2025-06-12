import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class FeatureView:
    """
    UI控制
    """
    def __init__(self, master, all_features_config, controller):
        self.master = master
        self.all_features_config = all_features_config
        self.controller = controller

        master.title("jcy MOD 控制器 v1.0.2")
        master.geometry("600x700")

        self.feature_vars = {}  # 存储所有 Checkbutton 和 Radiobutton 的 Tkinter 变量
        self.group_radio_buttons = {} # 存储每个组的 Radiobutton 列表
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
        standalone_features = self.all_features_config.get("standalone_features", {})
        for fid, description in standalone_features.items():
            var = tk.BooleanVar()
            self.feature_vars[fid] = var
            chk = ttk.Checkbutton(standalone_tab, text=description, variable=var, command=lambda f=fid, v=var: self.controller.execute_feature_action(f, v.get()))
            chk.pack(anchor=tk.W, padx=10, pady=2)

        # --- 分组的互斥功能 (Grouped Features) ---
        group_features = self.all_features_config.get("group_features", {})
        for group_id, group_info in group_features.items():
            group_frame = ttk.LabelFrame(grouped_tab, text=group_info["text"])
            group_frame.pack(padx=20, pady=5, fill=tk.X)

            self.group_radio_buttons[group_id] = []
            group_radio_var = tk.StringVar()
            self.feature_vars[group_id] = group_radio_var

            # 为 Radiobutton 创建一个内部容器，以便横向排列
            radio_button_container = ttk.Frame(group_frame)
            radio_button_container.pack(fill=tk.X, padx=15, pady=5) # 容器的填充和内边距

            for param_dict in group_info["params"]:
                param_key = next(iter(param_dict.keys()))
                param_description = param_dict[param_key]
                rb = ttk.Radiobutton(radio_button_container, text=param_description, variable=group_radio_var, value=param_key,
                                     command=lambda g_id=group_id, v_var=group_radio_var: self.controller.execute_group_action(g_id, v_var.get()))
                # 这里使用 side=tk.LEFT 进行横向排列，并调整 padx/pady
                rb.pack(side=tk.LEFT, padx=5, pady=0)
                self.group_radio_buttons[group_id].append(rb)

        # 应用设置按钮
        apply_button = ttk.Button(self.master, text="应用设置", command=self.controller.apply_settings)
        apply_button.pack(pady=10)

    def update_ui_state(self, current_states: dict):
        """
        根据加载的设置更新 UI 元素的状态。
        """
        for fid, var in self.feature_vars.items():
            # 处理独立功能 (Checkbutton) 的状态
            if fid in self.all_features_config["standalone_features"]:
                value = current_states.get(fid, False)
                var.set(value)
            # 处理分组功能 (Radiobutton) 的状态
            elif fid in self.all_features_config["group_features"]:
                group_info = self.all_features_config["group_features"][fid]
                if group_info["params"]:
                    default_param_key = next(iter(group_info["params"][0].keys()))
                    selected_param_key = current_states.get(fid, default_param_key)
                    var.set(selected_param_key)
                else:
                    var.set("")