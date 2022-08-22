"""
publish readings from BME280 via Adafruit.IO
"""
from machine import Pin, I2C, ADC
import time
import bme280
from adafruit_io import topic, connect_to_adafruit_io

topics = list(topic(name) for name in
              ['bme280-temp','bme280-pressure', 'bme280-humidity','light-level'])

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
bme = bme280.BME280(address=0x77, i2c=i2c)
adc = ADC(26)
mc = connect_to_adafruit_io('bme280')

def bme_data():
    t, p, h = bme.read_compensated_data()
    return [t/100, p/25600, h/1000]
    

while True:
    a2 = adc.read_u16()
    light_level = a2/10
    values = bme_data() + [light_level]
    print(values[0], values[2], values[3]) # for plotting in Thonny
    for (topic, value) in zip(topics, values):
        mc.publish(topic, str(value))
    time.sleep(60)
