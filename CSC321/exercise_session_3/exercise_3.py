from machine import Pin
from time import sleep_ms

led = Pin(19, Pin.OUT)
push_btn = Pin(22, Pin.IN, Pin.PULL_UP)
state = push_btn.value()

# def handle_interrupt(new_state):
#     if new_state.value() == 1:
#         led.on()
#         print(new_state.value())
#         
# 
# push_btn.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)

active = True

while active:
    try:
        new_state = push_btn.value()
        print(new_state)
        if new_state == 1:
            led.on()
        if new_state == 0:
            led.off()
    except KeyboardInterrupt:
        led.off()
        active = False
    sleep_ms(100)