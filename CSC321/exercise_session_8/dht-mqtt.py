import machine
import ujson
from umqtt.robust import MQTTClient
from dht import DHT11
from time import sleep
import network

WIFI_SSID = 'MyWifi'

d = DHT11(machine.Pin(22))

ProjectName = 'esp32_rgb_led_mqtt'
MQTTName = '06ed040f-dfa6-4cf1-8990-ecb7b2dd1626'
MQTTPassword = 'cfd6cf41-5e30-47ee-87e1-9ac328a6c388'
ClientID = '8d3646ab-cb3e-48aa-a25a-ac527749db28'

mqtt_server = '10.10.62.21'
mqtt_port = 1883
mqtt_topic = 'csc321'

client = MQTTClient(mqtt_topic, mqtt_server, port=mqtt_port, user='csc321', password='csc321')
client = MQTTClient(ClientID, MQTTName, port=mqtt_port, user=ClientID, password=MQTTPassword)


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

client.connect()

while True:
    try:
        d.measure()
        temp = d.temperature()
        hum = d.humidity()
        data = '\nThank you for subscribing to God Updates, The temperature is %s°C and humidity is %s rh. Stay tuned for further updates! \n' % (temp, hum)
        client.publish(mqtt_topic, data)
    except Exception as e:
        print('Error publishing data: %s' % str(e))
    sleep(30)