from machine import Pin
from time import sleep

led = Pin(19, Pin.OUT)

def morse_S():
    for i in range(3):
        led.on()
        sleep(0.5)
        led.off()
        sleep(0.5)
        
def morse_O():
    for i in range(3):
        led.on()
        sleep(0.2)
        led.off()
        sleep(0.2)
        

while True:
    morse_S()
    morse_O()
    morse_S()

    # Pause
    sleep(1.0)