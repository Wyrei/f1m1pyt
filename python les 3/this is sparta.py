# Add your Python code here. E.g.
from microbit import *


while True:
    display.scroll('this is sparta')
   
    display.show(Image.HEART)
    sleep(1000)
    display.show(Image.HEART_SMALL)
    sleep(1000)
   
    display.scroll(str(button_a.get_presses()))
    display.show(Image.DUCK)
    sleep(1000)