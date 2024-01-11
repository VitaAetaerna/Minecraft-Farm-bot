import time
import os
import datetime

from win32gui import GetWindowText, GetForegroundWindow
import keyboard
import pyautogui
def Bot():
    State = 0  #0 left 1 right
    print("This bot requires Minecraft 1.8")
    print("Press  ,  to start the bot")
    keyboard.wait(',')
    print("Starting in 5 seconds, please tab into your MC...")
    time.sleep(5.5)
    #Run left

    while True:
        pyautogui.mouseDown()
        if State == 0:
            endTime = datetime.datetime.now() + datetime.timedelta(minutes=1.26)
            print(endTime)
            while datetime.datetime.now() < endTime and GetWindowText(GetForegroundWindow()) == "Badlion Minecraft Client v4.0.0-a84656f-PRODUCTION4 (1.8.9)":
                print(endTime - datetime.datetime.now())
                pyautogui.keyDown('w')
                pyautogui.keyDown('a')
                
                if  GetWindowText(GetForegroundWindow()) != "Badlion Minecraft Client v4.0.0-a84656f-PRODUCTION4 (1.8.9)":
                    print("Waiting 30 secs")
                    endTime +=  datetime.timedelta(minutes=0.50)
                    time.sleep(30)
                    if  GetWindowText(GetForegroundWindow()) == "Badlion Minecraft Client v4.0.0-a84656f-PRODUCTION4 (1.8.9)":
                        continue
                if datetime.datetime.now() >= endTime:
                    pyautogui.keyUp('w')
                    pyautogui.keyUp('a')
                    State = 1
        #Run right
        if State == 1:
            endTime = datetime.datetime.now() + datetime.timedelta(minutes=1.26)
            print(endTime)
            while datetime.datetime.now() < endTime and GetWindowText(GetForegroundWindow()) == "Badlion Minecraft Client v4.0.0-a84656f-PRODUCTION4 (1.8.9)":
                print(endTime - datetime.datetime.now())
                pyautogui.keyDown('w')
                pyautogui.keyDown('d')
                
                if  GetWindowText(GetForegroundWindow()) != "Badlion Minecraft Client v4.0.0-a84656f-PRODUCTION4 (1.8.9)":
                    print("Waiting 30 secs")
                    endTime +=  datetime.timedelta(minutes=0.50)
                    time.sleep(30)
                    if  GetWindowText(GetForegroundWindow()) == "Badlion Minecraft Client v4.0.0-a84656f-PRODUCTION4 (1.8.9)":
                        continue
                if datetime.datetime.now() >= endTime:
                    pyautogui.keyUp('w')
                    pyautogui.keyUp('d')
                    State = 0

Bot()
