from mcp23008 import MCP23008
from time import sleep
from machine import Pin, I2C

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=40000)


def loop():
    mcp23008 = MCP23008(i2c)
    mcp23008.direction(0x00)
    try:
        while True:
            for i in range(256):
                mcp23008.output(i)
                sleep(0.1)
    finally:
        mcp23008.output(0)


loop()
