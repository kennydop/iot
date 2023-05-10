from umqtt.robust import MQTTClient
from time import sleep
import network
from machine import I2C, Pin, PWM


WIFI_SSID = 'MyWifi'

buz_pin = Pin(27)
buzzer = PWM(buz_pin, freq=500)
buzzer.duty(0)

mqtt_server = '10.10.62.21'
mqtt_port = 1883
mqtt_topic = b'esp32_buzzer'

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


def handle_buzzer(topic, msg):
    print("handling motor.....")
    payload = msg.decode('utf-8')
    if payload == 'on':
        print("buzzing")
        buzzer.duty(50)
    elif payload == 'off':
        print("halting buzzer")
        buzzer.duty(0)
    else:
        print("new duty: " + payload)
        buzzer.duty(int(payload))
 
client.connect()
client.set_callback(handle_buzzer)
client.subscribe(b'buzzer')

while True:
    client.check_msg()

