import pyautogui
import time


pyautogui.PAUSE = 1

pyautogui.press('win')
pyautogui.write('ubuntu')
pyautogui.press('enter')

time.sleep(8)
pyautogui.write("sudo service mysql start")
pyautogui.press('enter')
pyautogui.write('16112002b')
pyautogui.press('enter')

time.sleep(8)

pyautogui.write('sudo service apache2 start')
pyautogui.press('enter')
