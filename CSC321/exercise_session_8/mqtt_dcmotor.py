from machine import Pin
from umqtt.robust import MQTTClient
from time import sleep
import network
from d1motor import Motor
from machine import I2C, Pin

n = 1
p = 21
WIFI_SSID = 'MyWifi'

i2c = I2C(0, scl = Pin(22), sda = Pin(21))
m0 = Motor(0, i2c)
m0.frequency(500)

mqtt_server = '10.10.62.21'
mqtt_port = 1883
mqtt_topic = b'esp32_motor'

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


def handle_motor(topic, msg):
    print("handling motor.....")
    payload = msg.decode('utf-8')
    if payload == 'on':
        print("turning on")
        m0.speed(100)
    elif payload == 'off':
        print("turning off")
        m0.speed(0)
    else:
        print("new speed: " + payload)
        m0.speed(int(payload))
 
client.connect()
client.set_callback(handle_motor)
client.subscribe(b'motor')

while True:
    client.check_msg()
