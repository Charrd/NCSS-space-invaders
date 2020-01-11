# Write your code here :-)
from microbit import *
import radio
import music


radio.on()
radio.config(channel=31)


while True:
    msg = radio.receive()
    if msg:
        if msg.startswith('WON'):
            music.stop()
            words = msg.split()
            display.scroll('YOU WON')
            display.scroll(words[1])
        elif msg == 'LOST':
            music.stop()
            display.scroll('YOU LOST')