from machine import Pin
from neopixel import NeoPixel
from time import sleep

n = 7
p = 26

np = NeoPixel(Pin(p), n)

def turn_off():
    for i in range(0, n):
        np[i] = (0, 0, 0)
        np.write()

def turn_on(rgb):
    for i in range(0, n):
        np[i] = (rgb[0], rgb[1], rgb[2])
        np.write()
        sleep(0.1)

# start
while True:
    turn_off()

    sleep(1)

    turn_on([255, 0, 0])

    turn_off()
    sleep(1)

    turn_on([0, 255, 0])

    turn_off()
    sleep(1)

    turn_on([0, 0, 255])
