from microbit import *
import radio

radio.on()
radio.config(channel=31)


#for sender

while True:
    if button_a.was_pressed():
        radio.send("LEFT")
    if button_b.was_pressed():
        radio.send("RIGHT")