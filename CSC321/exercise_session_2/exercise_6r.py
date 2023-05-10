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
    sleep(0.5)

# start
while True:
    turn_off()

    sleep(1)

    turn_on([255, 0, 0])
    turn_on([0, 255, 0])
    turn_on([0, 0, 255])
    
    turn_off()
    
    # 8 combinations
    turn_on([125, 0, 0])
    turn_on([125, 125, 0])
    turn_on([0, 125, 0])
    turn_on([0, 125, 125])
    turn_on([0, 0, 125])
    turn_on([125, 0, 125])
    turn_on([125, 125, 125])
    turn_on([0, 0, 0])