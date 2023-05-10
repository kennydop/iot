from machine import Pin, PWM
from time import sleep

led_pin = 19
pir_pin = 18
push_btn_pin = 22
buz_pin = Pin(27)

buzzer = PWM(buz_pin, freq=500)
led = Pin(led_pin, Pin.OUT)
push_btn = Pin(push_btn_pin, Pin.IN, Pin.PULL_UP)
pir = Pin(pir_pin, Pin.IN, Pin.PULL_UP)

raising_alarm = False

    
def handle_pir_interrupt(new_pir):
    print("PIR: alarm activated!")
    raise_alarm(True)
        

def handle_push_btn_interrupt(new_btn):
    print("BTN: alarm deactivated!")
    raise_alarm(False)
        
push_btn.irq(trigger=Pin.IRQ_RISING, handler=handle_push_btn_interrupt)
pir.irq(trigger=Pin.IRQ_FALLING, handler=handle_pir_interrupt)

def raise_alarm(val):
    while val:
        print("raising an alarm!")
        buzzer.duty(50)
        led.on()
        sleep(3)
        buzzer.duty(0)
        led.off()
        sleep(0.5)
    else:
        buzzer.duty(0)
        led.off()
