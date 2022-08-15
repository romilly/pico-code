from umqtt.simple import MQTTClient
from network_connection import connect
from machine import Pin, I2C, ADC
import time
from secrets import SSID, PASSWORD, IO_USERNAME, IO_KEY
import bme280

MQTT_HOST = 'io.adafruit.com'


def topic(name):
    return bytes('{:s}/feeds/{:s}'.format(IO_USERNAME, name), 'utf-8')


topics = list(topic(name) for name in
              ['bme280-temp','bme280-pressure', 'bme280-humidity','light-level'])

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
bme = bme280.BME280(address=0x77, i2c=i2c)
adc = ADC(26)
connect(SSID, PASSWORD)
mc = MQTTClient('thermo', MQTT_HOST, user=IO_USERNAME, password=IO_KEY)
mc.connect()
print('connected to %s' % MQTT_HOST)

def bme_data():
    t, p, h = bme.read_compensated_data()
    return [t/100, p/25600, h/1000]
    

while True:
    a2 = adc.read_u16()
    light_level = a2/10
    values = bme_data() + [light_level]
    print(values[0], values[2], values[3]) # for plotting in Thonny
    for (topic, value) in zip(topics, values):
        mc.publish(topic, str(value)) # published to Adafruit.IO
    time.sleep(60)
