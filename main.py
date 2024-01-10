import time
import os
import datetime
running = False


try:
    from pynput.mouse import Button, Controller as MouseController
    from win32gui import GetWindowText, GetForegroundWindow
    import keyboard
except ImportError:
    os.system('cmd /k pip install pynput')
    os.system('cmd /k pip install keyboard')
    os.system('cmd /k pip install pywin32')

def GetNewTime():
    endTime = datetime.datetime.now() + datetime.timedelta(minutes=1.42)
    return endTime

def Bot():
    running = False
    mouse = MouseController()
    keyboard.wait(',')
    print('Starting in 5 seconds...')
    running = True
    time.sleep(5)
    

    while running:
        while datetime.datetime.now() < GetNewTime() and GetWindowText(GetForegroundWindow()) == "Minecraft* 1.20 - Multiplayer (3rd-party Server)":
            time.sleep(0.1)
            keyboard.press('w')
            time.sleep(0.1)
            keyboard.press('a')
            mouse.click(Button.left, 1)
            if datetime.datetime.now() >= GetNewTime():
                break


        while datetime.datetime.now() < GetNewTime() and GetWindowText(GetForegroundWindow()) == "Minecraft* 1.20 - Multiplayer (3rd-party Server)":
            time.sleep(0.1)
            keyboard.press('w')
            time.sleep(0.1)
            keyboard.press('d')
            mouse.click(Button.left, 1)
            if datetime.datetime.now() >= GetNewTime():
                break

        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN and event.name == 'l':
            keyboard.wait(',')
            Bot()
            

if __name__ == "__main__":
    Bot()
