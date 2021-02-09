from machine import Pin, SPI
from time import sleep, sleep_ms
from mcp3008 import MCP3008

spi = SPI(0)
cs = Pin(22, Pin.OUT)
cs.value(1) # disable chip at start

square = Pin(21, Pin.OUT)

chip = MCP3008(spi, cs)

while True:
    square.value(1)
    actual = chip.read(0)
    print(actual)
    sleep(0.5)
    square.value(0)
    actual = chip.read(0)
    print(actual)
    sleep(0.5)
