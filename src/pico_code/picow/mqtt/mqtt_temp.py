from umqtt.simple import MQTTClient
from src.pico_code.picow.network_connection import connect
from machine import ADC
import time
from src.pico_code.picow.secrets import SSID, PASSWORD, MQTT_HOST


adc = ADC(26)
connect(SSID, PASSWORD)
mc = MQTTClient('thermo', MQTT_HOST)
print('connected to %s' % MQTT_HOST)
mc.connect()

while True:
    a0 = adc.read_u16()
    volts_mv = 3300*a0/65535.0 # 3V3 = 65535
    temp = (volts_mv -500)/10  # from
    c_temp = '%5.2f C' % temp
    print(c_temp)
    mc.publish('temp', c_temp)
    time.sleep(1)
