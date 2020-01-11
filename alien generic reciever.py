from microbit import *
import radio
import neopixel

n = 15
spd = 70
neo = neopixel.NeoPixel(pin0, n)

radio.on()
radio.config(channel=31)
alienID = 2
alive = True



neo.clear()
#for reciever
while True:
    msg = radio.receive()
    if msg and alive:
        if msg.startswith(str(alienID)):
            neo[n-1] = (50,205,50)
            sleep(spd)
            neo.show()
            for light in range(n-1, 0, -1):
                neo[light] = (0, 0, 0)
                neo[light-1] = (50,205,50)
                sleep(spd)
                neo.show()
            neo.clear()
            display.show(Image.NO)
            hit = True
            alive = False
            sleep(50)
            radio.send('DEAD')
            break
    if alive:
        display.show(Image.GHOST)
