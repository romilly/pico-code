"""
publish temperature from TMP36 via Adafruit.IO
"""
from machine import ADC
import time
from adafruit_io import topic, connect_to_adafruit_io

mc = connect_to_adafruit_io('tmp36')
tmp36_topic = topic('temp-tmp36')
adc = ADC(26)

while True:
    a0 = adc.read_u16()
    volts_mv = 3300 * a0 / 65535.0  # 3V3 = 65535
    temp = (volts_mv - 500) / 10  # from
    mc.publish(tmp36_topic, str(temp))
    time.sleep(60)
