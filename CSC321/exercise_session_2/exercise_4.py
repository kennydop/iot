from machine import Pin, PWM
from time import sleep_ms
from math import sin, pi

led = Pin(19, Pin.OUT)
pwm_led = PWM(led)

while True:
    for i in range(0, 100):
        brightness = 511 * sin(2*pi/100*i) + 511
        pwm_led.duty(round(brightness))
        sleep_ms(50)
        
    