# from machine import Pin, SPI
# import ili934x
# 
# # Configure SPI pins and instance
# spi = SPI(1, baudrate=40000000, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
# 
# # Configure ILI9341 pins and instance
# cs = Pin(15, Pin.OUT)
# dc = Pin(2, Pin.OUT)
# rst = Pin(4, Pin.OUT)
# 
# # Initialize ILI9341 class
# display = ili934x.ILI9341(spi, cs, dc, rst, w=240, h=320, r=3)
# 
# # Set the position where you want to start writing text
# display.set_pos(10, 10)
# 
# # Write text to the screen
# display.write("Hello, world!")

import ili934x
from machine import Pin, SPI
spi = SPI(1, miso=Pin(12), mosi=Pin(13, Pin.OUT), sck=Pin(14, Pin.OUT))
display = ili934x.ILI9341(spi, cs=Pin(0), dc=Pin(5), rst=Pin(4), w=240, h=320, r=3)
display.fill_rectangle(10, 10, 50, 50, ili934x.color565(0xff, 0x11, 0x22))
display.pixel(120, 160, 0)
