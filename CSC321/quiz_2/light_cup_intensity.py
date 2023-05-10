from machine import Pin, PWM
from time import sleep_ms
from math import sin, pi

nb_pin = 27
ob_pin = 22
spin = 19
lpin = 23

sled = Pin(spin, Pin.OUT)
lled = Pin(lpin, Pin.IN)
spwm = PWM(sled)
new_btn = Pin(nb_pin, Pin.IN, Pin.PULL_UP)
old_btn = Pin(ob_pin, Pin.IN, Pin.PULL_UP)

sbrightness = 0
spwm.duty(sbrightness)

def handle_new_btn_interrupt(new_btn):
    print("new button pressed")
    global sbrightness
    sbrightness += 10
    print(sbrightness)
    spwm.duty(sbrightness)
    sleep_ms(500)

def handle_old_btn_interrupt(old_btn):
    print("old button pressed")
#     global sbrightness
#     sbrightness -= 1
#     print(sbrightness)
#     spwm.duty(round(sbrightness))

new_btn.irq(trigger=Pin.IRQ_RISING, handler=handle_new_btn_interrupt)
old_btn.irq(trigger=Pin.IRQ_RISING, handler=handle_old_btn_interrupt)