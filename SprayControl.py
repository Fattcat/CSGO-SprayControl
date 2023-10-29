import keyboard
import pyautogui

while True:
    if keyboard.is_pressed('a'):
        current_x, current_y = pyautogui.position()
        pyautogui.moveTo(current_x, current_y + 6, duration=0.25)
