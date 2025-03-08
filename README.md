# python 合作项目 :dart:

# 可视化工具箱项目开发计划

## 项目概述

- **目标**：开发集成多功能的桌面应用（连点器/截图/小游戏/表格生成等），最终打包为.exe 文件
- **技术栈**：Python + Tkinter/PyQt5（GUI 框架）、PyInstaller（打包工具）、Git（版本控制）等

## 功能模块划分

### 1. 主界面设计

- [ ] 导航菜单（侧边栏或顶部标签页）
- [ ] 模块加载框架（动态调用子功能）

### 2. 子功能开发

- **连点器**

- **截图工具**

- **小游戏集合**

- **表格生成器**

- **可视化条形图**

- **语音备忘录**

- **翻译插件**

- **AI 图像处理**

## 开发计划

### 第一阶段（需求分析 & 技术验证）

- [ ] 确定核心功能清单
- [ ] 完成 GUI 框架技术选型

### 第二阶段（模块并行开发）

- [ ] 主界面与子模块开发
- [ ] 各子功能独立开发与单元测试

### 第三阶段（集成测试与优化）

- [ ] 模块联调测试
- [ ] 性能优化（启动速度/内存占用）
- [ ] 手册编写（Markdown 格式）

# python 所需的库

### Python 可视化工具箱项目所需库汇总表

| 分类         | 库名称            | 主要功能描述                                             |
| ------------ | ----------------- | -------------------------------------------------------- |
| **GUI 开发** | Tkinter           | Python 内置 GUI 库，适合快速搭建简单界面（菜单、按钮等） |
|              | PyQt5             | 支持复杂界面设计，提供现代化 UI 组件和动态加载能力       |
| **基础工具** | pyautogui         | 实现连点器的鼠标控制和坐标记录                           |
|              | Pillow (PIL)      | 处理截图功能（区域选择、图像保存），支持多种图片格式     |
|              | pygame            | 开发贪吃蛇、俄罗斯方块等小游戏，支持音效和图形渲染       |
| **数据处理** | openpyxl          | Excel 文件读写，生成带样式和公式的表格                   |
|              | pandas            | 数据清洗与分析，支持 CSV/Excel 格式转换                  |
|              | Matplotlib        | 创建统计图表（折线图/柱状图），嵌入到表格生成器          |
| **扩展功能** | opencv-python     | 实现高级图像处理（人脸马赛克、边缘检测）                 |
|              | SpeechRecognition | 语音转文字功能，用于开发语音备忘录模块                   |
|              | python-docx       | 生成 Word 文档报告，与表格生成器联动                     |
| **打包工具** | PyInstaller       | 将项目打包为.exe 文件，支持添加资源文件                  |
|              | cx_Freeze         | 跨平台打包工具（备选方案）                               |
| **协作开发** | pytest            | 编写单元测试，确保模块稳定性                             |
|              | black             | 自动化代码格式化，统一团队编码风格                       |
|              | pre-commit        | Git 提交前自动检查代码规范                               |
| **扩展增强** | PyQtGraph         | 开发实时数据看板（股票走势/传感器仪表盘）                |
|              | requests          | 调用在线 API（如翻译插件接入谷歌/百度接口）              |

## 项目进度计划

| 阶段         | 任务             | 预计完成时间 | 实际完成时间 |
| ------------ | ---------------- | ------------ | ------------ |
| 需求分析     | 确定核心功能清单 |              |              |
| 技术验证     |                  |              |              |
| 模块并行开发 |                  |              |              |
