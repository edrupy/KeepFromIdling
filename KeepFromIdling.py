#! python3

import time
import random
import pyautogui

def Execute():
    keys = ['numlock', 'capslock', 'shift']
    lastUsedKey = None
    while True:
        availableKeys = [key for key in keys if key != lastUsedKey]
        key = random.choice(availableKeys)
        lastUsedKey = key
        waitTime = random.randint(50, 150)
        print(f'press {key:<8} x2 in 1 sec - sleep {waitTime:<3} sec afterwards')  #:<8 ensures left-aligned within an 8-character wide field
        time.sleep(1)
        pyautogui.hotkey(key)
        time.sleep(0.01)
        pyautogui.hotkey(key)
        time.sleep(waitTime)



if __name__ == '__main__':
    Execute()
