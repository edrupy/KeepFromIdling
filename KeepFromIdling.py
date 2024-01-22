#! python3

import time
import pyautogui

WaitTime = 3*59

def Execute():
    while True:
        print('press numlock x2 in 1 sec')
        time.sleep(1)
        pyautogui.hotkey('numlock')
        pyautogui.hotkey('numlock')
        time.sleep(WaitTime)


if __name__ == '__main__':
    Execute()
