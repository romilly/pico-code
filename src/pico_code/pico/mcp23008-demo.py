from mcp23008 import MCP23008
from time import sleep
from machine import Pin, I2C

i2c = I2C(0, scl=Pin(21), sda=Pin(20), freq=100000) # pins for Pico Explorer

def loop():
    ic = MCP23008(i2c)
    ic.direction(0x00)
    while True:
        for i in range(256):
            ic.output(i)
            sleep(0.2)


loop()