import pyautogui
import keyboard


scroll_distance = -500
pause_time = 5


if keyboard.read_key() == 'h':
    while True:
        pyautogui.sleep(pause_time)
        #if keyboard.read_key() == 'p':
            #pyautogui.sleep(20)
        pyautogui.scroll(scroll_distance)






