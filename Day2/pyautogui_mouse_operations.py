import pyautogui
import time


#Mouse operations
pyautogui.moveTo(100,100,duration=1)

pyautogui.click(100,100)
pyautogui.rightClick(100,100)

pyautogui.scroll(500)
time.sleep(1)
pyautogui.scroll(-500)


