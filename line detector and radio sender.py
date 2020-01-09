# Write your code here :-)
from microbit import *
import radio

radio.on()
radio.config(channel=31)

linenumber = 0
drive_state = 'left'
shoot = False

running_time()


def line_sensor():
    left_sensor = not pin11.read_digital()
    right_sensor = not pin5.read_digital()
    if not left_sensor and not right_sensor:
        return
    else:
        return True


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

