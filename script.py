import os             
import pyautogui
import time
from time import sleep
from datetime import datetime


try:
    # open MS Teams application
    #os.startfile("/usr/bin/teams") 
    sleep(2)
    # settings
    settings = pyautogui.locateCenterOnScreen("Images/settings.PNG") 
    pyautogui.moveTo(settings)
    pyautogui.click()
    time.sleep(2)
    # manageteams.PNG
    manageteams = pyautogui.locateCenterOnScreen("Images/manageteams.PNG") 
    pyautogui.moveTo(manageteams)
    pyautogui.click()
    time.sleep(2)
except Exception as e:
    print(e)

while True:
    #DemoMeetOne
    now = datetime.now().strftime("%H:%M")
    if now < '11:00':
        DemoMeetOne = pyautogui.locateCenterOnScreen("Images/joinnow.PNG") 
        pyautogui.moveTo(DemoMeetOne)
        pyautogui.click()
        time.sleep(2)
        join = pyautogui.locateCenterOnScreen("Images/join.PNG") 
        pyautogui.moveTo(join)
        pyautogui.click()
        time.sleep(2)
        audiooff = pyautogui.locateCenterOnScreen("Images/audiooff.PNG") 
        pyautogui.moveTo(audiooff)
        pyautogui.click()
        time.sleep(2)
        
    elif now <'10:00':
      	#DemoMeetTwo
        DemoMeetTwo = pyautogui.locateCenterOnScreen("ImagesDemoMeetTwo.PNG") 
        pyautogui.moveTo(DemoMeetTwo)
        pyautogui.click()
        time.sleep(2)
        join = pyautogui.locateCenterOnScreen("Images/join.PNG") 
        pyautogui.moveTo(join)
        pyautogui.click()
        time.sleep(2)
        audiooff = pyautogui.locateCenterOnScreen("Images/audiooff.PNG") 
        pyautogui.moveTo(audiooff)
        pyautogui.click()
        time.sleep(2)