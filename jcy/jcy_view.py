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

        master.title("jcy MOD 控制器 v1.0.4a")
        master.geometry("600x700")

        self.feature_vars = {} 
        self.group_radio_buttons = {} 
        self._create_ui()

    def _create_ui(self):
        # 创建 Notebook 
        notebook = ttk.Notebook(self.master)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        
        # --- checkbutton ---
        tab = None
        for i, (fid, description) in enumerate(self.all_features_config.get("checkbutton", {}).items()):
            if i % 20 == 0 :
                tab = ttk.Frame(notebook)
                notebook.add(tab, text=" 功能特效 ")
            var = tk.BooleanVar()
            self.feature_vars[fid] = var
            chk = ttk.Checkbutton(tab, text=description, variable=var, command=lambda f=fid, v=var: self.controller.execute_feature_action(f, v.get()))
            chk.pack(anchor=tk.W, padx=10, pady=3)
        

        # --- radiogroup ---
        radiogroup_tab = ttk.Frame(notebook)
        notebook.add(radiogroup_tab, text=" 单选特效 ")
        radiogroup_features = self.all_features_config.get("radiogroup", {})
        for fid, info in radiogroup_features.items():
            group = LabeledRadioGroup(radiogroup_tab, feature_id=fid, data=info, default_selected="default", command=self.controller.execute_feature_action)
            group.pack(anchor="n", fill="x", padx=20, pady=10)
            self.feature_vars[fid] = group

        
        # --- checkgroup ---
        checkgroup_tab = ttk.Frame(notebook)
        notebook.add(checkgroup_tab, text=" 多选特效 ")
        checkgroup_features = self.all_features_config.get("checkgroup", {})
        for fid, info in checkgroup_features.items():
            group = LabeledCheckGroup(checkgroup_tab, feature_id=fid, data=info, default_selected=[], command=self.controller.execute_feature_action)
            group.pack(anchor="n", fill="x", padx=20, pady=10)
            self.feature_vars[fid] = group


        # --- spinbox ---
        range_tab = ttk.Frame(notebook)
        notebook.add(range_tab, text=" 区间特效 ")
        range_features = self.all_features_config.get("spinbox", {})
        for fid, description in range_features.items():
            label_frame = ttk.LabelFrame(range_tab, text=description)
            label_frame.pack(padx=20, pady=5, fill=tk.X)

            spin_container = ttk.Frame(label_frame)
            spin_container.pack(fill=tk.X, padx=15, pady=5) # 容器的填充和内边距

            var = tk.IntVar()
            self.feature_vars[fid] = var
            spin = ttk.Spinbox(spin_container, from_=0, to=9, increment=1, textvariable=var, command=lambda f=fid, v=var: self.controller.execute_feature_action(f, v.get()), state='readonly')
            spin.pack(anchor=tk.W, padx=10, pady=2)
        

        # 应用设置按钮
        apply_button = ttk.Button(self.master, text="应用设置", command=self.controller.apply_settings)
        apply_button.pack(pady=10)

    def update_ui_state(self, current_states: dict):
        """
        根据加载的设置更新 UI 元素的状态。
        """
        for fid, var in self.feature_vars.items():
            if fid in self.all_features_config["checkbutton"]:
                value = current_states.get(fid, False)
                var.set(value)
            elif fid in self.all_features_config["radiogroup"]:
                value = current_states.get(fid, None)
                var.set(value)
            elif fid in self.all_features_config["checkgroup"]:
                value = current_states.get(fid, [])
                var.set(value)
            elif fid in self.all_features_config["spinbox"]:
                value = current_states.get(fid, 0)
                var.set(value) 

class LabeledRadioGroup(ttk.LabelFrame):
    def __init__(self, master, feature_id, data, default_selected=None, command=None, **kwargs):
        super().__init__(master, text=data["text"], **kwargs)
        self.feature_id = feature_id
        self.command = command
        self.var = tk.StringVar(value=default_selected)

        for j, item in enumerate(data["params"]):
            key, label = next(iter(item.items()))
            rb = ttk.Radiobutton(self, text=label, value=key, variable=self.var, command=self._on_select)
            rb.grid(row=0, column=j, sticky="ew", padx=5, pady=5)
            self.columnconfigure(j, weight=1)

    def _on_select(self):
        if self.command:
            self.command(self.feature_id, self.var.get())

    def get(self):
        return self.var.get()

    def set(self, key):
        self.var.set(key)

    @property
    def text(self):
        return self.cget("text")

class LabeledCheckGroup(ttk.LabelFrame):
    def __init__(self, master, feature_id, data, default_selected=None, command=None, **kwargs):
        super().__init__(master, text=data["text"], **kwargs)
        self.feature_id = feature_id
        self.command = command
        self.vars = {}

        if default_selected is None:
            default_selected = []

        for j, item in enumerate(data["params"]):
            key, label = next(iter(item.items()))
            var = tk.BooleanVar(value=(key in default_selected))
            chk = ttk.Checkbutton(self, text=label, variable=var, command=self._on_check)
            chk.grid(row=0, column=j, sticky="ew", padx=5, pady=5)
            self.columnconfigure(j, weight=1)
            self.vars[key] = var

    def _on_check(self):
        if self.command:
            selected = self.get()
            self.command(self.feature_id, selected)

    def get(self):
        return sorted([key for key, var in self.vars.items() if var.get()])

    def set(self, selected_keys):
        for key, var in self.vars.items():
            var.set(key in selected_keys)

    @property
    def text(self):
        return self.cget("text")