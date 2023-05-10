from machine import Pin
from neopixel import NeoPixel
from time import sleep

p = 21
n = 1
np = NeoPixel(Pin(p), n)


def turn_off():
    np[0] = (0, 0, 0)
    np.write()
    
def turn_on(rgb):
    np[0] = (rgb[0], rgb[1], rgb[2])
    np.write()

# Start
while True:
    turn_off()

    sleep(1)
    
    for c in range(0xFFFFFF+1):
        r  = (c >> 16) & 0xFF
        g = (c >> 8) & 0xFF
        b  = (c) & 0xFF
        turn_on([r, g, b])
        print([r, g, b])
    
