#!/usr/bin/python3
#-*- coding:utf-8 -*-
from  pynput.mouse import Button, Controller
import time

mouse = Controller()

if __name__ == "__main__":
    for i in range(7):
        time.sleep(0.5)
        mouse.position = (20, 70)
        time.sleep(0.5)
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(0.5)

        mouse.position = (20, 329)
        time.sleep(0.5)
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(0.5)

        mouse.position = (20, 320)
        time.sleep(0.5)
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(0.5)