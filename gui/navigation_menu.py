import tkinter as tk

class NavigationMenu:
    """
    主界面导航菜单控制器
    
    功能：
    - 管理侧边栏布局和样式
    - 创建功能模块入口按钮
    - 协调模块加载与显示
    """
    
    def __init__(self, master):
        """
        初始化导航菜单
        
        参数：
        master (tk.Tk): 主窗口根对象
        
        布局参数说明：
        - width=200: 侧边栏固定宽度
        - bg="#2c3e50": 背景色(深蓝灰)
        - height=600: 高度与主窗口保持一致
        """
        self.master = master
        
        # 创建左侧导航栏

        # `tk.Frame`：Tkinter库中的一个组件，用于创建一个矩形的容器，可用于组织其他组件。
        # `master`：指定该组件的父容器。在这个例子中，`master`是一个Tkinter的根窗口对象。
        self.sidebar = tk.Frame(master, width=200, bg="#2c3e50", height=600)
        # `pack`：是Tkinter中用于布局组件的方法之一，用于将组件放置在父容器中。
        # `side=tk.LEFT`：指定框架在其父窗口中停靠的位置，这里是停靠在左边。
        # `fill=tk.Y`：指定框架在垂直方向上填充可用空间，即框架的高度会自动调整以填充父窗口的垂直空间。
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
        
        # 添加导航按钮
        self.create_button("功能导航", 20)
        self.create_button("连点器", self.add_clicker_module)
        self.create_button("截图工具", self.add_screenshot_module)
        self.create_button("小游戏集合", self.add_games_module)
        self.create_button("更多功能", self.add_more_module)

    
    def create_button(self, text, command):
        """
        创建统一风格的导航按钮
        
        参数：
        text (str): 按钮显示文本
        command (function): 点击时触发的回调函数
        
        UI设计说明：
        - font: 使用微软雅黑12号字体
        - bg: 默认状态背景色
        - activebackground: 点击状态背景色
        - width: 固定按钮宽度保持布局统一
        """
        if text == "功能导航":
            # 使用Label组件实现标题效果
            label = tk.Label(self.sidebar,
                           text=text,
                           font=("Microsoft YaHei", 12, "bold"),
                           fg="white",
                           bg="#2c3e50",
                           pady=8)
            label.pack()
        else:
            btn = tk.Button(self.sidebar, 
                          text=text,
                          font=("Microsoft YaHei", 12),
                          bg="#34495e",
                          fg="white",
                          activebackground="#3498db",
                          command=command,
                          width=18,
                          relief="flat")
            btn.pack(pady=5, padx=10)

    def add_clicker_module(self):
        """
        加载连点器模块 
        
        
        实现逻辑：
        1. 实例化Clicker功能模块
        2. 将模块界面加载到内容区域
        3. 销毁旧模块保持界面整洁
        """
        pass

    def add_screenshot_module(self):
        pass

    def add_games_module(self):
        pass
    def add_more_module(self):
        pass