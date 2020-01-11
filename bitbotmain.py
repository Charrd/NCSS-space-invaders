from microbit import *
import radio
import neopixel


radio.on()
radio.config(channel=31)
shoot = False
direction =True
n = 8
numberalive = 3
timer = 50000
neopixel_pin = pin13
neopixel_num = 12

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

    def __init__(self):
        global direction
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



move('FOR', 700)

while True:
    bitbot_counter.update()
    if (timer - running_time()) <= 1:
        win = False
        break
    msg = radio.receive()
    if msg:
        if msg == 'SHOOT':
            shoot = True
            np = neopixel.NeoPixel(neopixel_pin, neopixel_num)
        if msg == 'BACK':
            direction = False
        elif msg == 'FOR':
            direction = True
        if msg == 'DEAD':
            numberalive -= 1
            if numberalive == 0:
                stop()
                winning_time = int((timer - running_time())/1000)
                win = True
                break
        
    if line_sensor():
        if shoot:
            msg = str(bitbot_counter.count) + 'hit'
            for i in range(6):
                np[i] = (50, 210, 50)
                np[i+6] = (50, 210, 50)
                np.show()
                sleep(30)
            np.clear()
            radio.send(msg)
            shoot = False
        else:
            shoot = False
    else:
        shoot = False

    if (bitbot_counter.count >= n and direction) or (bitbot_counter.count <= 0 and not direction):
        stop()
    else:
        if direction:
            move('FOR', 700)
        else:
            move('BACK', 323)
display.clear()
if win:
    msg = 'WON ' + str(winning_time)
else:
    msg = 'LOST'
radio.send(msg)