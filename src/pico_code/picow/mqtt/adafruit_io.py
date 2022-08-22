from network_connection import connect
from secrets import IO_USERNAME, IO_KEY, SSID, PASSWORD
from umqtt.simple import MQTTClient
import random

MQTT_HOST = 'io.adafruit.com'


def connect_to_adafruit_io(client_id='', add_random=True):
    connect(SSID, PASSWORD)
    client_id = 'rareblog-%s' % client_id
    if add_random:
        client_id += str(1000+random.randrange(1000))
    mc = MQTTClient(client_id, MQTT_HOST, user=IO_USERNAME, password=IO_KEY)
    mc.connect()
    print('connected to %s' % MQTT_HOST)
    return mc

def topic(name):
    return bytes('{:s}/feeds/{:s}'.format(IO_USERNAME, name), 'utf-8')