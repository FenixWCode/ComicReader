import pyautogui
import keyboard


scroll_distance = -500
pause_time = 4


if keyboard.read_key() == 'h':
    while True:
        print('go!')
        pyautogui.press('right')
        pyautogui.sleep(pause_time)
        pyautogui.scroll(scroll_distance)
        pyautogui.sleep(pause_time)
        pyautogui.scroll(scroll_distance)
        pyautogui.sleep(pause_time)




