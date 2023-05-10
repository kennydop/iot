# PS/CSC/20/0055


from d1motor import Motor
from machine import I2C, Pin
from time import sleep_ms
from math import sin, pi
from rotary_irq_esp import RotaryIRQ

i2c = I2C(0, scl = Pin(22), sda = Pin(21))
m0 = Motor(0, i2c)
m0.frequency(500)
factor = 1
r = RotaryIRQ(pin_num_clk=26,
              pin_num_dt=18,
              min_val=0,
              max_val=100,
              reverse=False,
              range_mode=RotaryIRQ.RANGE_WRAP)
sw_btn = Pin(27, Pin.IN, Pin.PULL_DOWN)
val_old = r.value()

# (a)
def motorSpeed(rotary_speed):
    if rotary_speed < 0 or rotary_speed > 100:
        print("Value out of range!")
        return
    speed = (rotary_speed/100) * 1000
    m0.speed(round(speed))
    sleep_ms(200)

def handle_direction_change():
    factor * -1
    
# (b)
def changeDirection():
    sw_btn.irq(trigger=Pin.IRQ_RISING, handler=handle_direction_change)

while True:
    val_new = r.value()

    if val_old != val_new:
        val_old = val_new
        print('speed =', val_new * factor)
        motorSpeed(val_new * factor)
    sleep_ms(50)