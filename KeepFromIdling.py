#! python3

import time
import random
import pyautogui

def Execute():
    while True:
        waitTime = random.randint(50, 150)
        print(f'press Ctrl + Alt + F15 - sleep {waitTime:<3} sec afterwards')  #:<3 ensures left-aligned within an 3-character wide field
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'alt', 'f15')
        time.sleep(waitTime)



if __name__ == '__main__':
    Execute()
