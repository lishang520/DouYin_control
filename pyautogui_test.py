import pyautogui
import time

press_time = 3

if __name__ == '__main__':
    time.sleep(5)
    while True:
        pyautogui.keyDown("w")
        print("keyDown w")
        time.sleep(press_time)
        print("keyUp w")
        pyautogui.keyUp("w")

        pyautogui.keyDown("a")
        print("keyDown a")
        time.sleep(press_time)
        print("keyUp a")
        pyautogui.keyUp("a")

        pyautogui.keyDown("d")
        print("keyDown d")
        time.sleep(press_time)
        print("keyUp d")
        pyautogui.keyUp("d")

        pyautogui.keyDown("w")
        print("keyDown w")
        time.sleep(press_time)
        print("keyUp w")
        pyautogui.keyUp("w")