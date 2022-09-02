#!/usr/bin/env bash
cd ../src/pico_code/picow
mpremote cp bme680i.py :
mpremote cp blinker.py :
mpremote cp network_connection.py :
mpremote cp secrets.py :
cd mqtt
mpremote cp mqtt_installer.py :
mpremote cp adafruit_io.py :
mpremote cp adafruit_io_bme680.py :main.py
mpremote exec 'import mqtt_installer'
