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

class SensorCount:
    global direction
    def __init__(self):
        self.pin = pin11
        self.state = False
        self.count = 1
    def update(self):
        if not self.pin.read_digital() and not self.state:
            self.state = True
            if direction:
                self.count += 1
            else:
                self.count -= 1
        elif self.pin.read_digital() and self.state:
            self.state = False
            if direction:
                self.count += 1
            else:
                self.count -= 1

bitbot_counter = SensorCount()


shoot = False
direction =True

n = 8
move('FOR', 1023)



while True:
    update(bitbot_counter)
    msg = radio.receive()
    if msg:
        if msg == 'shoot':
            shoot = True
        if msg == 'BACK':
            direction = False
        elif msg == 'FOR':
            direction = True
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
    
    if (bitbot_counter.count == n and direction) or (bitbot_counter.count == 0 and not direction):
        stop()
    else:
        if direction:
            move('FOR', 1023)
        else:
            move('BACK', 1023)
