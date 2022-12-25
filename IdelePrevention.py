# author Darshan Ramjiyani

import pyautogui as pag

if __name__=="__main__":
    from time import sleep
    while True:
        x,y = pag.position()
        print(f"Clicking at the : ({x}, {y}).")
        pag.click()
        sleep(1)