import keyboard
import pyautogui

while True:
    #            EDIT 'a' to your macro key for activate it.
    if keyboard.is_pressed('a'):
    #            EDIT 'a' to your macro key for activate it.
        
        current_x, current_y = pyautogui.position()
        pyautogui.moveTo(current_x, current_y + 6, duration=0.25)
