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
        self.sidebar = tk.Frame(master, width=200, bg="#2c3e50", height=600)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
        
        # 添加导航按钮
        self.create_button("功能导航", 20)
        self.create_button("连点器", self.add_clicker_module)
        self.create_button("截图工具", self.add_screenshot_module)
        self.create_button("小游戏集合", self.add_games_module)
    
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
        btn = tk.Button(self.sidebar, 
                      text=text,
                      font=("Microsoft YaHei", 12),
                      bg="#34495e",
                      fg="white",
                      activebackground="#3498db",
                      command=command,
                      width=18)
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