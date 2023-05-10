from machine import Pin
from time import sleep_ms

push_btn = Pin(21, Pin.IN, Pin.PULL_UP)
state = push_btn.value()
print(state)

active = True

while True:
    print(push_btn.value())

# while active:
#     try:
#         new_state = push_btn.value()
#         if new_state != state:
#             print(new_state)
#             state = new_state
#     except KeyboardInterrupt:
#         active = False
#     sleep_ms(100)
