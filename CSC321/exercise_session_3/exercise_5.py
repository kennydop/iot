from machine import Pin
from neopixel import NeoPixel
from time import sleep

np = NeoPixel(Pin(26), 7)
push_btn = Pin(22, Pin.IN, Pin.PULL_UP)

cur_col = 0
cur_index = 0

def off_all():
    for i in range(0, 7):
        np[i] = (0, 0, 0)
        np.write()
        
def handle_light():
    global cur_col
    global cur_index
    if cur_index > 6:
        cur_index = 0
        cur_col += 1
    if cur_col > 2:
        cur_col = 0
        off_all()
        return
    rgb = [0, 0, 0]
    if cur_col == 0:
        rgb[0] = 5
    if cur_col == 1:
        rgb[1] = 5
    if cur_col == 2:
        rgb[2] = 5
    np[cur_index] = (rgb[0], rgb[1], rgb[2])
    np.write()
    cur_index += 1

def handle_interrupt(new_state):
    handle_light()
        
push_btn.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)