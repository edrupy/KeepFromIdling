#! python3

import time
import pyautogui

WaitTime = 3*59

def Execute():
    while True:
        print('press F19 in 1 sec')
        pyautogui.hotkey('f19')
        time.sleep(WaitTime)


if __name__ == '__main__':
    Execute()
