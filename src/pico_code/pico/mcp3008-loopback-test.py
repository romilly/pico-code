from pio_dac import PIOPWM

import machine
from time import sleep
from mcp3008 import MCP3008

spi = machine.SPI(0)
cs = machine.Pin(22, machine.Pin.OUT)
cs.value(1) # disable chip at start

pwm = PIOPWM(0, 21, max_count=250, count_freq=10_000_000)

chip = MCP3008(spi, cs)
while True:
    for i in range(0, 250, 50):
        pwm.set(i)
        sleep(0.1)
        print(chip.read(0))
        sleep(0.01)