#! /bin/bash
cd ../src/pico_code/picow/mqtt
mpremote cp network_connection.py :
mpremote cp secrets.py :
mpremote cp mqtt_installer.py :
mpremote cp lipo-monitor.py :
mpremote exec 'from mqtt_installer import install'

