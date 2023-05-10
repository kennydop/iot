from machine import Pin, ADC
from time import sleep

sensor = ADC(Pin(36))
sensor.atten(ADC.ATTN_11DB)  
    
while True:
  value = sensor.read()
  voltage = value / 4095 * 3.3
  cel = (voltage - 0.5) * 100
  frh = cel * 9/5 + 32
  print(cel, '°C or', frh, '°F')
  sleep(1)
  