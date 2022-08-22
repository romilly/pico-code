# This example shows how to read the voltage from a LiPo battery connected to a Raspberry Pi Pico via our Pico Lipo SHIM...
# ...and uses this reading to calculate how much charge is left in the battery.
# modified by Romilly Cocking from the Pimoroni original version.
#
# The original version  displays the info on the screen of Pico Display or Pico Explorer.
# It's at https://raw.githubusercontent.com/pimoroni/pimoroni-pico/main/micropython/examples/pico_lipo_shim/battery.py
#
# This version publishes the battery state and charging status via MQTT, so you can monitor it remotely.
# Remember to save this code as main.py on your Pico if you want it to run automatically,
# and add the application code you want to run!

# You'll need to connect to an existing MQTT broker.
# You'll also need to install  via upip once you are connected to WI-Fi
# After connecting, run the code below from a REPL

"""
import upip
upip.install('umqtt.simple')
"""

# It requires network_connection.py (in the same directory as this file) and secrets.py to be installed on the Pico W


# secrets.py should contain your network id and password in this format:

"""
SSID = 'your Wi-Fi network id'
PASSWORD = 'your Wi-Fi password'
MQTT_HOST='broker url'
"""


from machine import ADC, Pin
import time
import random
from src.pico_code.picow import network_connection
from umqtt.simple import MQTTClient
from src.pico_code.picow.secrets import SSID, PASSWORD, MQTT_HOST

# connect to wifi
# this may take several seconds

network_connection.connect(SSID, PASSWORD)

# connect to the broker
# each client should have a unique id, so generate it randomly

CLIENT_ID = 'pico-lipo-monitor-%d' % (1000 + random.randrange(999))

mc = MQTTClient(CLIENT_ID, MQTT_HOST)
mc.connect()

# read and publish battery state every minute

vsys = ADC(29)              # reads the system input voltage
charging = Pin(24, Pin.IN)  # reading GP24 tells us whether USB power is connected
conversion_factor = 3 * 3.3 / 65535

full_battery = 4.2                  # these are our reference voltages for a full/empty battery, in volts
empty_battery = 2.8                 # the values could vary by battery size/manufacturer so you might need to adjust them

while True:
    # convert the raw ADC read into a voltage and a percentage
    voltage = vsys.read_u16() * conversion_factor
    percentage = 100 * ((voltage - empty_battery) / (full_battery - empty_battery))
    if percentage > 100:
        percentage = 100.00
    status = '' if charging else 'not '
    message = 'Lipo voltage: %f V = %6.2f %% %s charging' % (voltage, percentage, status)
    mc.publish('lipo-voltage', message)
    time.sleep(60) # change this value (in seconds) if you want more or less frequent readings