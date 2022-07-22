from machine import ADC
import time

adc = ADC(26)

while True:
    a0 = adc.read_u16()
    volts_mv = 3300*a0/65535.0 # 3V3 = 65535
    temp = (volts_mv -500)/10  # from
    print('%5.2f C' % temp)
    time.sleep(1)