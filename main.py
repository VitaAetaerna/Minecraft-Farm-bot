import time
import os


try:
    from pynput.mouse import Button, Controller as MouseController
    import keyboard
except ImportError:
    os.system('cmd /k pip install pynput')
    os.system('cmd /k pip install keyboard')



def Bot():
    mouse = MouseController()
    keyboard.wait(',')
    time.sleep(5)

    while True:
        tl_end = time.time() + 60 * 2
        while time.time() < tl_end:
            time.sleep(0.2)
            keyboard.press('a')
            mouse.click(Button.left, 1)

        tr_end = time.time() + 60 * 2
        while time.time() < tr_end:
            time.sleep(0.2)
            keyboard.press('d')
            mouse.click(Button.left, 1)

        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN and event.name == 'l':
            keyboard.wait(',')
            Bot()

if __name__ == "__main__":
    Bot()
