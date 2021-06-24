# this code is specific to my chrome set up
# but i recommend pyautogui if you need something
# to automate boring stuff that you cant do with code

import pyautogui as pg
import time

time.sleep(3)

for i in range(60):
    time.sleep(.05)
    pg.click(300, 50)
    time.sleep(.05)
    pg.click(300, 50)
    time.sleep(.05)
    pg.click(300, 50)
    time.sleep(.05)
    pg.typewrite("file:///C:/Users/Ambrose/Desktop/Drexel%20Work/q3/DSCI%20591/my_map_"+str(i)+".html")
    pg.typewrite(["enter"])
    time.sleep(4)
    pg.click(45, 190)
    time.sleep(7)
    pg.screenshot('my_screenshot'+str(i)+'.png')
    pg.typewrite(["escape"])
