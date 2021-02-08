from pio_dac import PIOPWM

import machine
from time import sleep
from mcp3008 import MCP3008

spi = machine.SPI(0)
cs = machine.Pin(22, machine.Pin.OUT)
cs.value(1) # disable chip at start

chip = MCP3008(spi, cs)
while True:
    print(chip.read(0))
    sleep(1)