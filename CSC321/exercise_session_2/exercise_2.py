from machine import Pin
from time import sleep_ms

led = Pin(19, Pin.OUT)

active = True

while active:
    try:
        led.on()
        sleep_ms(500)
        led.off()
        sleep_ms(500)
    except KeyboardInterrupt:
        active = False
        led.off()
        sleep_ms(500)
