import pyautogui
import time




time.sleep(5)

for i in range(1,20):
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.write(f' hahahaha {i+1} ', interval=0.1)  # Type with quarter-second pause in between each key.
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter') 
