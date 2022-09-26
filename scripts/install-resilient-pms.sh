#! /bin/bash
cd ../src/pico_code/picow/
mpremote cp blinker.py :
mpremote cp pmsa003i_packet_parser.py :
mpremote cp pmsa003i.py :
mpremote cp network_connection.py :
mpremote cp secrets.py :
cd mqtt
mpremote cp pms003i_adafruit.py :
mpremote cp mqtt_installer.py :
mpremote exec 'import mqtt_installer'
mpremote cp mqtt_robust_installer.py :
mpremote exec 'import mqtt_robust_installer'

