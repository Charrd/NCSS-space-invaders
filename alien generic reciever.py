from microbit import *
import radio

radio.on()
radio.config(channel=31)
alienID = 0
alive = True


#for reciever
while True:
    msg = radio.receive()
    if msg and alive:
        if msg.startswith(str(alienID)):
            display.show(Image.NO)
            hit = True
            alive = False
            sleep(50)
    if alive:
        display.show(Image.GHOST)