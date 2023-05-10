from d1motor import Motor
from machine import I2C, Pin
from time import sleep_ms
from math import sin, pi

i2c = I2C(0, scl = Pin(22), sda = Pin(21))
m0 = Motor(0, i2c)
m0.frequency(500)

while True:
    for i in range(0, 100):
        speed = 1000 * sin(2*pi/100*i)
#         print(speed)
        m0.speed(round(speed))
        sleep_ms(200)
