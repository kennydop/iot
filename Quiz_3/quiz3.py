from machine import Pin, I2C, ADC
from dht import DHT11
from time import sleep
from  ST7735 import Display, color565
from machine import Pin, SPI
import fonts.sysfont as sysfont
import sys
from d1motor import Motor

dht = DHT11(Pin(27))
sck = Pin(18)
miso= Pin(19)
mosi= Pin(23)
SPI_CS = 26
SPI_DC = 5
spi = SPI(2, baudrate=32000000, sck=sck, mosi=mosi, miso=miso)
display=Display(spi,SPI_CS,SPI_DC)
i2c = I2C(0, scl = Pin(22), sda = Pin(21))
m0 = Motor(0, i2c)
adc = ADC(Pin(33, mode=Pin.IN))

adc.atten(ADC.ATTN_11DB)
display.clear()

# measure temperature and display on screen [Q2]
def read_and_display_temp(continous=False):
    _continous = True
    while _continous:
        dht.measure()
        temp = dht.temperature()
        display_to_tft('Temp: ' + str((temp*9/5) + 32) + 'F', 0, 0)
        _continous = continous
        sleep(1)
    
# increase motor speed when temp > 86°F [Q3]
def regulate_motor_speed_with_temp():
    while True:
        dht.measure()
        temp = dht.temperature()
        fhr = (temp*9/5) + 32
        print('Increasing motor speed to %s' % int(fhr))
        if fhr > 86:
            m0.speed(int(fhr))
        else:
            m0.speed(0)
        sleep(1)
        
# control motor with slide pot [Q1]
def control_motor_with_pot():
    while True:
        val = adc.read()
        m0.speed(int(val))
        display_to_tft('Motor speed: '+str(val), 0, 30)
        sleep(0.1)
        
def display_to_tft(_str, x=0, y=0):
    display.draw_text(x, y, _str, sysfont, color565(255, 255, 255))

# [Q4]
def q4():
    read_and_display_temp(True)
    regulate_motor_speed_with_temp()
    control_motor_with_pot()

