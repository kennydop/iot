from machine import Pin, PWM, SPI
from time import sleep_ms
import max7219

trail = Pin(26, Pin.IN, Pin.PULL_DOWN)
buz_pin = Pin(18, Pin.OUT)
leds = Pin(23, Pin.OUT)
buzzer = PWM(buz_pin, freq=1000)
buzzer.duty(0)

leds.off()

    
def trail_interrupt(trail):
        buzzer.duty(512)
        leds.on()
        sleep_ms(10)
        buzzer.duty(0)
        leds.off()
            
trail.irq(trigger=Pin.IRQ_FALLING, handler=trail_interrupt)