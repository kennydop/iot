from  ST7735 import Display, color565
from sht30 import SHT30
from machine import Pin, SPI, I2C
import fonts.sysfont as sysfont
import sys

sck = Pin(18)
miso= Pin(19)
mosi= Pin(23)
SPI_CS = 26
SPI_DC = 5
spi = SPI(2, baudrate=32000000, sck=sck, mosi=mosi, miso=miso)
display=Display(spi,SPI_CS,SPI_DC)

sensor = SHT30()
display.clear()

import machine

# (a)
def i2cAddress():
    i2c = I2C(scl=Pin(22), sda=Pin(21))
    print('Scanning the I2C bus')
    addresses = i2c.scan()
    print(addresses[0])

# (b)
def forecast_weather():
    temperature, humidity = sensor.measure()
    display.draw_text(x, y, _str, sysfont, color565(255, 255, 255))

print(i2cAddress())
# forecast_weather()