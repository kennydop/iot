# PS/CSC/20/0055


from machine import Pin, ADC
from time import sleep
from neopixel import NeoPixel

adc = ADC(Pin(33, mode=Pin.IN))
adc.atten(ADC.ATTN_11DB)
np = NeoPixel(Pin(26), 7)

half = 4095/2
np_max = 255

def handle_rgb(r, g, b):
    for i in range(7):
        np[i] = (r, g, b)
        np.write()

handle_rgb(0, 0, 0)
while True:
    val = adc.read()
    duty = int(((val - half) / half)*255)
    r = (duty * -1) + 255
    g = duty + 255
    b = duty + 255
    handle_rgb(r, g, b)
#     print("val: {}, duty: {}, rdb: [{}, {}, {}]".format(val, duty, r,g,b))
    sleep(0.1)
