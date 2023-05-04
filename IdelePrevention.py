# author Darshan Ramjiyani

import threading
import time
import pyautogui


def click_thread():
    while True:
        pyautogui.click()  # perform a mouse click action
        time.sleep(3)  # wait for half a second


def scroll_thread():
    while True:
        pyautogui.scroll(-1)  # scroll down by one unit
        time.sleep(1)  # wait for half a second


def switch_thread():
    direction = 'right'
    while True:
        time.sleep(60)  # wait for 60 seconds
        # switch to the next desktop
        pyautogui.hotkey('ctrl', 'alt', direction)
        if direction == 'left':
            direction = 'right'
        else:
            direction = 'left'


if __name__ == '__main__':
    threading.Thread(target=click_thread).start()
    #threading.Thread(target=scroll_thread).start() #uncomment this line if you want to scroll.
    # threading.Thread(target=switch_thread).start() #uncomment this line if you want switch the desktops.
