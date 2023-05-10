from machine import Pin, ADC
from time import sleep

# analog inputs for X and Y
analogPinX = ADC(Pin(34))
analogPinY = ADC(Pin(32))

#switching the analog input to 12Bit (0...4095)
analogPinX.atten(ADC.ATTN_11DB)
analogPinY.atten(ADC.ATTN_11DB)

# digital input on pin 26
sw = Pin(26, Pin.IN, Pin.PULL_UP)


while True:
  analogValX = analogPinX.read()
  analogValY = analogPinY.read()
  switch = sw.value()
  print("x:%s   y:%s   sw:%s" % (analogValX, analogValY, switch))
  sleep(1)