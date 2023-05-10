from machine import Pin, ADC, DAC
from time import sleep

adc = ADC(Pin(36))
adc.atten(ADC.ATTN_11DB)
dac = DAC(Pin(26))

with open('adc.txt', 'w') as f:
    for i in range(256):
        dac.write(i)
        _adc_val = adc.read()
        f.write(str(_adc_val) + '\n')
        print(i, ',', _adc_val) 
