# connect A0 to AOUT, check that increasing output voltage increases voltage read.

# My circuit uses IC1 with pins scl=7, sda = 6

import machine
import pcf8591
import time

i2c = machine.I2C(1, scl=machine.Pin(7), sda=machine.Pin(6))
adc_dac = pcf8591.PCF8591(i2c)

for i in range(255):
    vout = i
    adc_dac.dac_out(vout)
    vin = adc_dac.adc_in(0) # channel 0
    print(vout, vin)
    time.sleep(0.1)

