import time
from machine import Pin, SPI, I2C, Timer
import fonts.sysfont as sysfont
import sys
from  ST7735 import Display, color565
from tcs3200 import TCS3200


sck = Pin(18)
miso= Pin(19)
mosi= Pin(23)
SPI_CS = 26
SPI_DC = 5
spi = SPI(2, baudrate=32000000, sck=sck, mosi=mosi, miso=miso)
display=Display(spi,SPI_CS,SPI_DC)

# s0 = Pin(26, Pin.OUT)
# s1 = Pin(22, Pin.OUT)
# s2 = Pin(25, Pin.OUT)
# s3 = Pin(27, Pin.OUT)
# out = Pin(26, Pin.IN)
  
sensor = TCS3200(21, 25, 27)
sensor.calibrate()
 
while True:
    readings = sensor.rgb()
    display.draw_filledCircle(6, 6, 4, color565(r, g, b))
    print("Red: {}, Green: {}, Blue: {}".format((r/10000)*255, g, b))
    time.sleep(1)