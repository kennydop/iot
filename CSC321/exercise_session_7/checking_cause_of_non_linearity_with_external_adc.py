from ads1x15 import ADS1115
from machine import I2C, Pin, DAC

i2c = I2C(0, scl=Pin(22), sda=Pin(21))
adc = ADS1115(i2c, 0x48, 0)
dac = DAC(Pin(26))

with open('adc.txt', 'w') as f:
    for i in range(256):
        dac.write(i)
        _adc_val = adc.read()
        f.write(str(_adc_val) + '\n')
        print(i, ',', _adc_val)