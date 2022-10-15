import pyautogui as pg
import time
time.sleep(10)

for i in range(400):
    pg.write("Hello!")
    pg.press('enter')