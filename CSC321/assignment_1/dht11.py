import dht
from machine import Pin
class DHT11():
    def __init__(self, pin):
        self.humidity = 0
        self.temperature = 0
        self.d = dht.DHT11(Pin(pin)) 

    def measure(self):
        self.d.measure()       #Measurement of temperature and humidity
        self.temperature = d.temperature() #Read Celsius temperature
        self.humidity = d.humidity()    #Read relative humidity
