"""
publish readings from BME680 via Adafruit.IO
"""

from machine import Pin, I2C, ADC
import timefrom bme680i import BME680_I2C
from adafruit_io import topic, connect_to_adafruit_io
import time

topics = list(topic(name) for name in
              ['bme680-temp','bme680-pressure', 'bme680-humidity','bme680-co2'])

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
bme = BME680_I2C(address=0x76, i2c=i2c)
adc = ADC(26)
mc = connect_to_adafruit_io('bme280')

def bme_data():
    return bme.read_compensated_data()
    

while True:
    values = bme_data()
    print(values)
    for (topic, value) in zip(topics, values):
        mc.publish(topic, str(value))
    time.sleep(60)
