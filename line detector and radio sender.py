# Write your code here :-)
from microbit import *
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


def line_sensor():
    left_sensor = not pin11.read_digital()
    right_sensor = not pin5.read_digital()
    if not left_sensor and not right_sensor:
        return
    else:
        return True

linenumber = 0
drive_state = 'left'
shoot = False

direc = True
count = 0
n = 6
move('FOR', 1023)

while True:
    msg = radio.receive()
    if msg:
        if msg == 'shoot':
            shoot = True
    if line_sensor():
        if shoot == True:
            msg = str(linenumber) + 'hit'
            display.show(Image.GIRAFFE)
            sleep(3000)
            radio.send(msg)
            shoot = False
        else:
            display.clear()
            shoot = False
    else:
        shoot = False
        display.clear()
    if (count == n and direc) or (count == 0 and not direc):
        stop()
    else:
        if direc:
            move('FOR', 1023)
        else:
            move('BACK', 1023)