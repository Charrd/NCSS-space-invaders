# Write your code here :-)
from microbit import *
import radio

radio.on()
radio.config(channel=31)



while True:
    if accelerometer.was_gesture("shake"):
        display.show(Image.TARGET)
        sleep(50)
        radio.send('SHOOT')
        #cool down
        sleep(3000)
    else:
        display.clear()