from machine import Pin
from neopixel import NeoPixel
from time import sleep

n = 1
p = 21

np = NeoPixel(Pin(p), n)

# np[0] = (255, 255, 255)


np[0] = (0, 0, 0)
np.write()
