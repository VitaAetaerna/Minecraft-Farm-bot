import time
import os
import datetime


try:
    from pynput.mouse import Button, Controller as MouseController
    from win32gui import GetWindowText, GetForegroundWindow
    import keyboard
except ImportError:
    os.system('cmd /k pip install pynput')
    os.system('cmd /k pip install keyboard')
    os.system('cmd /k pip install pywin32')


def Bot():
    State = 0  #0 left 1 right
    mouse = MouseController()
    print("This bot requires Minecraft 1.8")
    print("Press  ,  to start the bot")
    keyboard.wait(',')
    print("Starting in 5 seconds, please tab into your MC...")
    time.sleep(5.5)
    #Run left
    if State == 0:
        endTime = datetime.datetime.now() + datetime.timedelta(minutes=1)
        print(endTime)
        while datetime.datetime.now() < endTime and GetWindowText(GetForegroundWindow()) == "Minecraft* 1.20 - Multiplayer (3rd-party Server)":
            print(endTime - datetime.datetime.now())
            time.sleep(0.05)
            keyboard.press('w')
            keyboard.press('a')
            mouse.click(Button.left, 1) 
            
            if  GetWindowText(GetForegroundWindow()) != "Minecraft* 1.20 - Multiplayer (3rd-party Server)":
                time.sleep(30)
                if  GetWindowText(GetForegroundWindow()) == "Minecraft* 1.20 - Multiplayer (3rd-party Server)":
                    continue
            if datetime.datetime.now() >= endTime:
                State = 1
    #Run right
    if State == 1:
        endTime = datetime.datetime.now() + datetime.timedelta(minutes=1)
        print(endTime)
        while datetime.datetime.now() < endTime and GetWindowText(GetForegroundWindow()) == "Minecraft* 1.20 - Multiplayer (3rd-party Server)":
            print(endTime - datetime.datetime.now())
            time.sleep(0.05)
            keyboard.press('w')
            keyboard.press('d')
            mouse.click(Button.left, 1) 
            
            if  GetWindowText(GetForegroundWindow()) != "Minecraft* 1.20 - Multiplayer (3rd-party Server)":
                time.sleep(30)
                if  GetWindowText(GetForegroundWindow()) == "Minecraft* 1.20 - Multiplayer (3rd-party Server)":
                    continue
            if datetime.datetime.now() >= endTime:
                State = 0

Bot()
