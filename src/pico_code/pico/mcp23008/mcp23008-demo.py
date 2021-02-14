from mcp23008 import MCP23008
from time import sleep
from machine import Pin, I2C

i2c = I2C(0, scl=Pin(21), sda=Pin(20), freq=100000) # pins for Pico Explorer

# Code added to help with debugging



def loop():
    ic = MCP23008(i2c)
    ic.direction(0x00)
    count = 0
    while True:
        for i in range(256):
            count += 1
            try:
                ic.output(i)
            except:
                print ('failed after %d iterations' % count)
                return
            sleep(0.1)


loop()