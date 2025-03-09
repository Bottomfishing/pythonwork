import time
import pyautogui
import keyboard

def clicker(interval):
    """
    此函数用于实现鼠标连点功能，直到按下指定按键停止。

    参数:
    interval (float): 每次点击之间的间隔时间（秒）。
    """
    print("连点器将在3秒后开始，请将鼠标移动到需要点击的位置。")
    time.sleep(3)  # 等待3秒，让用户有时间将鼠标移动到目标位置
    while not keyboard.is_pressed('q'):  # 当未按下 'q' 键时持续点击
        pyautogui.click()  # 执行一次鼠标点击
        time.sleep(interval)  # 等待指定的间隔时间
    print("连点器已停止。")

if __name__ == "__main__":
    click_interval = 0.01  # 每次点击之间的间隔时间，单位为秒
    clicker(click_interval)