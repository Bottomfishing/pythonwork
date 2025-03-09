import tkinter as tk
from gui.navigation_menu import NavigationMenu

class MainWindow:
    """
    主窗口控制器
    
    功能：
    - 管理主窗口布局和尺寸
    - 协调导航菜单与内容区域
    - 处理模块切换时的界面更新
    
    界面管理机制：
    1. 采用pack布局管理器
    2. 内容区域使用Frame作为容器
    3. 通过destroy()方法清理旧内容

    """
    def __init__(self, master): #构造函数/初始化方法  #在Tkinter中，master指的是父窗口或主窗口，用于创建新的窗口或组件。
        self.master = master
        self.master.title("Python可视化工具箱")
        self.master.geometry("800x600")
        
        # 初始化导航菜单
        self.navigation = NavigationMenu(self.master)
        
        # 主内容区域
        self.content_frame = tk.Frame(self.master, bg="#f0f0f0")
        self.content_frame.pack(fill=tk.BOTH, expand=True)

        # 初始化默认显示内容
        self.show_default_view()

    def show_default_view(self):
        """
        初始化默认欢迎界面
        
        设计参数说明：
        - font: 微软雅黑24号标题字体
        - pady=100: 垂直间距保持视觉平衡
        - bg="#f0f0f0": 与内容区域背景色一致
        """
        label = tk.Label(self.content_frame, 
                        text="欢迎使用Python可视化工具箱",
                        font=("Microsoft YaHei", 24),
                        bg="#f0f0f0")
        label.pack(pady=100)