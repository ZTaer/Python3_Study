from  pynput.mouse import Button, Controller
mouse = Controller()
import time
for i in range(250):
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.01)