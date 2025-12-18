import pyautogui
import time

def google_chrome(song_name):
    pyautogui.hotkey("win")
    pyautogui.write("google chrome")
    pyautogui.press("Enter")
    time.sleep(5)
    pyautogui.hotkey("ctrl" , "t",)
    pyautogui.hotkey("ctrl",'k')
    time.sleep(3)
    pyautogui.write(song_name)
    pyautogui.press("Enter")
    time.sleep(5)
    pyautogui.moveTo(579,559,6)
    pyautogui.leftClick(579,559)
 
google_chrome("montagem noche")
