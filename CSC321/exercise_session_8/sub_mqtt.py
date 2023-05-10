from machine import Pin
from umqtt.robust import MQTTClient
from time import sleep
from neopixel import NeoPixel
import network

n = 1
p = 21
WIFI_SSID = 'MyWifi'

np = NeoPixel(Pin(p), n)
mqtt_server = '10.10.62.21'
mqtt_port = 1883
mqtt_topic = b'esp32_led'

def connect_to_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Connecting to Wi-Fi...')
        sta_if.active(True)
        sta_if.connect(WIFI_SSID)
        while not sta_if.isconnected():
            pass
    print('Wi-Fi connected:', sta_if.ifconfig())
    
connect_to_wifi()

client = MQTTClient(mqtt_topic, mqtt_server, port=mqtt_port, user='csc321', password='csc321')


def handle_led(topic, msg):
    print("handling LED.....")
    payload = msg.decode('utf-8')
    if payload == 'on':
        np[0] = (5, 5, 5)
        np.write()
    elif payload == 'off':
        np[0] = (0, 0, 0)
        np.write()
    elif payload == 'red':
        np[0] = (10, 0, 0)
        np.write()
    elif payload == 'green':
        np[0] = (0, 10, 0)
        np.write()
    elif payload == 'blue':
        np[0] = (0, 0, 10)
        np.write()
    else:
        print("Invalid Payload!")
        
client.connect()
client.set_callback(handle_led)
client.subscribe(b'led')

while True:
    client.check_msg()