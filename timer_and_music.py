# Write your code here :-)
from microbit import *
import radio
import music


radio.on()
radio.config(channel=31)

PACMAN_THEME = ['F3:2', 'F3:2', 'F3:2', 'D2:1', 'C2:1', 'F3:1','F3:2','A3:5','F3:2','F3:2','F3:2','D2:1','C2:1','F3:1','F:2','D3:5','F3:2','F:2','F:2','D2:1','C2:1','F3:1','F:2','A3b:2','B3b:2','C4b:2','B3b:2','A3b:2','F3:2','A2:4','F3:4']

music.play(PACMAN_THEME, wait=False, loop=True)

while True:
    msg = radio.receive()
    if msg:
        if msg.startswith('WON'):
            words = msg.split()
            display.scroll('YOU WON')
            display.scroll(words[1])
        elif msg == 'LOST':
            display.scroll('YOU LOST')