from machine import Pin
from neopixel import NeoPixel
from time import sleep

n = 7
p = 26

np = NeoPixel(Pin(p), n)

for i in range(0, n):
    np[i] = (0, 0, 0)
    np.write()

sleep(1)

for i in range(0, n):
    np[i] = (255, 0, 0)
    np.write()
    sleep(5)
    np[i] = (0, 0, 0)
    np.write()
