# Write your code here :-)
from microbit import *
import radio

radio.on()
radio.config(channel=31)



while True:
    if accelerometer.was_gesture("shake"):
        display.show(Image.ARROW_N)
        sleep(50)
        radio.send('shoot')
        #cool down
        sleep(3000)
    else:
        display.clear()