import pyautogui
import keyboard


scroll_distance = -500
pause_time = 5


if keyboard.read_key() == 'h':
    while True:
        '''if keyboard.read_key() == 'j':
            pyautogui.PAUSE = 120
            print('paused')
            if keyboard.read_key() == 'h':
                print('continued')
                continue'''
        print('go!')
        pyautogui.press('right')
        pyautogui.PAUSE = pause_time
        pyautogui.scroll(scroll_distance)
        pyautogui.PAUSE = pause_time
        pyautogui.scroll(scroll_distance)
        pyautogui.PAUSE = pause_time




