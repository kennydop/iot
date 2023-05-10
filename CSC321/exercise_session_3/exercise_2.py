from machine import Pin
from time import sleep_ms

push_btn = Pin(22, Pin.IN, Pin.PULL_UP)
state = push_btn.value()

def handle_interrupt(new_state):
    print(new_state.value())
        

push_btn.irq(trigger=Pin.IRQ_RISING|Pin.IRQ_FALLING, handler=handle_interrupt)