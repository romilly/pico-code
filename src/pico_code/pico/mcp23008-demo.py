from mcp23008 import MCP23008
from time import sleep


def loop():
    ic = MCP23008()
    ic.direction(0x00)
    while True:
        for i in range(256):
            ic.output(i)
            sleep(0.1)


loop()