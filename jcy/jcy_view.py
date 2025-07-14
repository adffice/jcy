import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
import os

class FeatureView:
    """
    UI控制
    """
    def __init__(self, master, all_features_config, controller):
        self.master = master
        self.all_features_config = all_features_config
        self.controller = controller

        master.title("jcy MOD 控制器 v1.0.4c")
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

        # --- checktable ---
        filter_tab = ttk.Frame(notebook)
        notebook.add(filter_tab, text=" 道具屏蔽 ")

        columns = ["ID", "enUS", "简体中文", "繁體中文"]
        data = self.controller.file_operations.load_filter_config()
                
        checktable = TableWithCheckbox(
            filter_tab, columns, data,
            config_dict=self.controller.current_states,
            config_key="501",
            on_change=lambda new_val: self.controller.execute_feature_action("501", new_val)
        )
        checktable.pack(fill="both", expand=True, padx=10, pady=10)
        self.feature_vars["501"] = checktable

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
            elif fid in self.all_features_config["checktable"]:
                value = current_states.get(fid, {})
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

class TableWithCheckbox(tk.Frame):
    """
    Scroll‑able checkbox table:
        - columns:  ['英文', '简体', '繁體', ...]
        - data:     [[id, col1, col2, ...], ...]
        - config_dict / config_key: 用来读写 {id: bool} 状态到外部字典
    """
    def __init__(self, master, columns, data,
                 config_dict=None, config_key=None,
                 col_width=14, wrap_px=140,
                 on_change=None,
                 **kwargs):
        super().__init__(master, **kwargs)

        # ---------- 外部状态 ----------
        self.columns      = columns
        self.data         = data
        self.config_dict  = config_dict or {}
        self.config_key   = config_key
        self.on_change = on_change

        if self.config_key and self.config_key not in self.config_dict:
            self.config_dict[self.config_key] = {}
        self.state_dict = self.config_dict[self.config_key] if self.config_key else {}

        # ---------- 滚动容器 ----------
        canvas = tk.Canvas(self, highlightthickness=0)
        vbar   = tk.Scrollbar(self, orient="vertical",   command=canvas.yview)
        hbar   = tk.Scrollbar(self, orient="horizontal", command=canvas.xview)
        canvas.configure(yscrollcommand=vbar.set, xscrollcommand=hbar.set)

        vbar.pack(side="right", fill="y")
        hbar.pack(side="bottom", fill="x")
        canvas.pack(side="left", fill="both", expand=True)

        # 内层表格 Frame
        self._tbl = tk.Frame(canvas)
        tbl_window = canvas.create_window((0, 0), window=self._tbl, anchor="nw")

        # 自动调整 scrollregion & 宽度
        def _on_config(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
            canvas.itemconfigure(tbl_window, width=canvas.winfo_width())  # 拉伸填充
        self._tbl.bind("<Configure>", _on_config)

        # ---------- 构建表格 ----------
        self.vars    = []
        self.row_ids = []

        # 表头
        tk.Label(self._tbl, text="屏蔽", width=6, borderwidth=1,
                 relief="solid").grid(row=0, column=0, sticky="nsew")
        for j, col in enumerate(columns, start=1):
            tk.Label(self._tbl, text=col, width=col_width, wraplength=wrap_px,
                     borderwidth=1, relief="solid", anchor="w"
                     ).grid(row=0, column=j, sticky="nsew")

        # 表体
        for i, row in enumerate(data, start=1):
            rid = str(row[0])
            self.row_ids.append(rid)

            var = tk.BooleanVar(value=self.state_dict.get(rid, False))
            self.vars.append(var)

            tk.Checkbutton(
                self._tbl,
                variable=var,
                command=self._make_callback()
            ).grid(row=i, column=0, sticky="nsew")

            for j, text in enumerate(row[1:], start=1):
                tk.Label(self._tbl, text=text, width=col_width,
                         wraplength=wrap_px, borderwidth=1, relief="solid",
                         anchor="w").grid(row=i, column=j, sticky="nsew")

        # 列均分伸缩
        for c in range(len(columns) + 1):
            self._tbl.grid_columnconfigure(c, weight=1)

    # ---------- 公共接口 ----------
    def get(self):
        """返回 {id: bool}"""
        return {rid: var.get() for rid, var in zip(self.row_ids, self.vars)}

    def set(self, state_dict: dict):
        """根据字典批量设定勾选状态"""
        for rid, var in zip(self.row_ids, self.vars):
            var.set(state_dict.get(rid, False))

    def update_config(self):
        """把当前勾选同步进外部 config_dict"""
        if self.config_key:
            self.config_dict[self.config_key] = self.get()

    def _make_callback(self):
        def callback():
            if self.on_change:
                self.on_change(self.get())  # 获取当前表格勾选状态并传回 controller
        return callback
