# Write your code here :-)
from microbit import *
import neopixel
import radio
radio.on()
radio.config(channel=31)

def move(fb, spd):
    if fb == 'FOR' or fb == 'FORWARD':
        pin0.write_analog(spd)
        pin1.write_analog(spd)
        pin8.write_digital(0)
        pin12.write_digital(0)
    elif fb == 'BACK' or fb == "BACKWARD":
        pin0.write_analog(spd)
        pin1.write_analog(spd)
        pin8.write_digital(1)
        pin12.write_digital(1)

def stop():
    pin8.write_digital(0)
    pin12.write_digital(0)
    pin0.write_analog(0)
    pin1.write_analog(0)

class line_sense:
    def __init__(self):
        self.was_pressed = False
        self.was_helper = True
    def check(self):
        if not pin11.read_digital() and not self.was_pressed and self.was_helper:
            self.was_pressed = True





sensor_detect = line_sense()
direc = True
count = 0
n = 5
move('FOR', 1023)
while True:
    sensor_detect.check()
    if direc:
        move('FOR', 1023)
    else:
        move('BACK', 1023)
    if radio.receive() or count == 5 or count == 0:
        direc = not direc
    if sensor_detect.was_pressed and direc and count != n:
        count += 1
        was_helper = False
    elif sensor_detect.was_pressed and not direc and count != 1:
        count -= 1
        was_helper = False
    else:
        was_helper = True

