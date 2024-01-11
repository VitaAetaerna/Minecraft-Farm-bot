import time
import os
import datetime
import threading


try:
    from win32gui import GetWindowText, GetForegroundWindow
    import keyboard
    import pyautogui
except ImportError as IE:
    os.system('cmd /k pip install keyboard')
    os.system('cmd /k pip install pyautogui')
    os.system('cmd /k pip install pywin32')

def MouseThread():
    while True:
        while "Minecraft" in GetWindowText(GetForegroundWindow()):
            pyautogui.mouseDown()
        else:
            pyautogui.mouseUp()
            time.sleep(25)
    

def Bot():
    State = 0  #0 left 1 right
    time_for_lane = input("Enter the time you need from 1 Lane End to the End (as a floating point number (1.50 = 1 min 30), (1.33 = 1 min 20)) \n ")
    time_for_lane = float(time_for_lane)
    print("Press Space to start the bot")
    keyboard.wait('space')
    print("Starting in 5 seconds, please tab into your MC...")
    for i in range(5):
        print(i)
        time.sleep(1)
    

    threadingMouse.start()

    #Run Left
    while True:
        if State == 0:
            endTime = datetime.datetime.now() + datetime.timedelta(minutes=time_for_lane)
            print(endTime)
            while datetime.datetime.now() < endTime and  "Minecraft" in GetWindowText(GetForegroundWindow()):
                print(endTime - datetime.datetime.now())
                pyautogui.keyDown('w')
                pyautogui.keyDown('a')
                
                if not "Minecraft" in GetWindowText(GetForegroundWindow()):
                    print("Waiting 30 secs")
                    endTime +=  datetime.timedelta(minutes=0.50)
                    time.sleep(30)
 
                if datetime.datetime.now() >= endTime:
                    pyautogui.keyUp('w')
                    pyautogui.keyUp('a')
                    State = 1

        #Run right
        if State == 1:
            endTime = datetime.datetime.now() + datetime.timedelta(minutes=time_for_lane)
            print(endTime)
            while datetime.datetime.now() < endTime and  "Minecraft" in GetWindowText(GetForegroundWindow()):
                print(endTime - datetime.datetime.now())
                pyautogui.keyDown('w')
                pyautogui.keyDown('d')
                
                if not "Minecraft" in GetWindowText(GetForegroundWindow()):
                    print("Waiting 30 secs")
                    endTime +=  datetime.timedelta(minutes=0.50)
                    time.sleep(30)
 
                if datetime.datetime.now() >= endTime:
                    pyautogui.keyUp('w')
                    pyautogui.keyUp('d')
                    State = 0

threadingMouse = threading.Thread(target=MouseThread)
Bot()
