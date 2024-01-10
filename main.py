import time
import os
import datetime
running = False


try:
    from pynput.mouse import Button, Controller as MouseController
    import keyboard
except ImportError:
    os.system('cmd /k pip install pynput')
    os.system('cmd /k pip install keyboard')



def Bot():
    mouse = MouseController()
    keyboard.wait(',')
    print('Starting...')
    running = True
    time.sleep(5)

    while running:
        endTime = datetime.datetime.now() + datetime.timedelta(minutes=1.42)
        while True:
            time.sleep(0.2)
            keyboard.press('w')
            time.sleep(0.2)
            keyboard.press('a')
            mouse.click(Button.left, 1)
            if datetime.datetime.now() >= endTime:
                break


        endTime = datetime.datetime.now() + datetime.timedelta(minutes=1.42)
        while True:
            time.sleep(0.2)
            keyboard.press('w')
            time.sleep(0.2)
            keyboard.press('d')
            mouse.click(Button.left, 1)
            if datetime.datetime.now() >= endTime:
                break

        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN and event.name == 'l':
            keyboard.wait(',')
            running = False
            Bot()

if __name__ == "__main__":
    Bot()
