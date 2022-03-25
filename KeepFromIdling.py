#! python3

import time
import pyautogui

WaitTime = 3*59

def Execute():
    while True:
        time.sleep(WaitTime)
        print('press F15 in 1 sec')
        pyautogui.hotkey('f15')


if __name__ == '__main__':
    Execute()
