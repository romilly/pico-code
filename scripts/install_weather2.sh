#!/usr/bin/env bash
cd ../src/pico_code/picow
mpremote cp bme280.py :
mpremote cp blinker.py :
mpremote cp network_connection.py :
mpremote cp secrets.py :
cd mqtt
mpremote cp mqtt_installer.py :
mpremote cp adafruit-io-weather2.py main.py:
mpremote exec 'from mqtt_installer import install;install()'
