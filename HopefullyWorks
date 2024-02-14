import time
import sys
import os
import datetime
import threading
# importing stuff (when not found install it)
try:
    from win32gui import GetWindowText, GetForegroundWindow
    import keyboard
    import pyautogui
    import dearpygui.dearpygui as dpg
except ImportError as IE:
    os.system('cmd /k pip install keyboard')
    os.system('cmd /k pip install pyautogui')
    os.system('cmd /k pip install pywin32')
    os.system('cmd /k pip install dearpygui')

def getSliderLength(sender, app_data):
    global lengthofline
    lengthofline = app_data
    return lengthofline

# Delay Value
def getSliderVal(sender, app_data):
    global delay
    delay = app_data
    return delay





# Mouse Movement and Bot Movement
def Mouse(event_stopper):
    while not event_stopper.wait(1):    
        while True:
            while "Minecraft" in GetWindowText(GetForegroundWindow()):
                pyautogui.mouseDown()
            else:
                pyautogui.mouseUp()
                time.sleep(25)

def Bot(event_stopper, delay):
    while not event_stopper.wait(1):
        State = 0
        while True:
            if State == 0:
                endTime = datetime.datetime.now() + datetime.timedelta(seconds=delay)
                print(endTime)
                while datetime.datetime.now() < endTime and  "Minecraft" in GetWindowText(GetForegroundWindow()):
                    print(endTime - datetime.datetime.now())
                    pyautogui.keyDown('w')
                    pyautogui.keyDown('a')
                    
                    if not "Minecraft" in GetWindowText(GetForegroundWindow()):
                        print("Waiting 30 secs")
                        endTime +=  datetime.timedelta(seconds=30)
                        threadingBot.sleep(30)
    
                    if datetime.datetime.now() >= endTime:
                        pyautogui.keyUp('w')
                        pyautogui.keyUp('a')
                        State = 1

            #Run right
            if State == 1:
                endTime = datetime.datetime.now() + datetime.timedelta(seconds=delay)
                print(endTime)
                while datetime.datetime.now() < endTime and  "Minecraft" in GetWindowText(GetForegroundWindow()):
                    print(endTime - datetime.datetime.now())
                    pyautogui.keyDown('w')
                    pyautogui.keyDown('d')
                    
                    if not "Minecraft" in GetWindowText(GetForegroundWindow()):
                        print("Waiting 30 secs")
                        endTime +=  datetime.timedelta(seconds=30)
                        threadingBot.sleep(30)
    
                    if datetime.datetime.now() >= endTime:
                        pyautogui.keyUp('w')
                        pyautogui.keyUp('d')
                        State = 0


#Start bot
def Start(sender, app_data):
    print("Delay: ", delay)
    print("Length of Lane: ", lengthofline)
    global threadingBot
    threadingBot = threading.Thread(target=Bot(pill2Kill, delay=delay))

    global threadingMouse
    threadingMouse = threading.Thread(target=Mouse(pill2Kill))
    threadingBot.start()
    threadingMouse.start()


#Stop Bot and let it wait 
def Stop():
    pill2Kill.set()
    sys.exit()
    


# Build GUI
def Gui():
    dpg.create_context()
    dpg.create_viewport(decorated=False, width=275, height=250, x_pos=10, y_pos=0)
    dpg.setup_dearpygui()

    with dpg.window(label="Pumpkin farmbot", width=275, height=250, no_resize=True, no_move=True, no_collapse=True, no_close=True):
        dpg.add_text("Use at your own Risk \nI take no liabillity", pos=[65, 30], color=[255,0,0])

        dpg.add_button(label="Stop", callback=Stop, width=100, height=25, pos=[65, 160])

        dpg.add_input_int(label="Time per lane ", width=75, pos=[65, 65], callback=getSliderLength)

        dpg.add_slider_int(label="Start Delay", width=75, pos=[65, 100], min_value=0, max_value=60, default_value=0, callback=getSliderVal)
        
        dpg.add_button(label="Start bot", callback=Start, width=100, height=25, pos=[65, 130])


    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == "__main__":
    global pill2Kill
    pill2Kill = threading.Event()

    # Create Thread
    threadingGUI = threading.Thread(target=Gui())
    threadingGUI.start()

