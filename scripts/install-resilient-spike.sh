#! /bin/bash
cd ../src/pico_code/picow/
mpremote cp blinker.py :
# mpremote cp pmsa003i.py :
# mpremote cp pms003i-spike.py :
mpremote cp network_connection.py :
mpremote cp secrets.py :
cd mqtt
mpremote cp mqtt_robust_installer.py :
mpremote exec 'import mqtt_robust_installer'

