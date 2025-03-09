# 程序主入口模块
# 负责初始化GUI应用程序和启动事件循环

import tkinter as tk
from gui.main_window import MainWindow  # 导入主窗口控制器

if __name__ == "__main__":
    
    # 创建Tkinter根窗口实例
    root = tk.Tk()
    
    # 初始化主界面控制器，传入根窗口
    app = MainWindow(root)
    
    # 启动Tkinter主事件循环，保持窗口运行
    root.mainloop()