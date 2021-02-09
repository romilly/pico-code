from pio_dac import PIOPWM

import machine
from time import sleep_ms
from mcp3008 import MCP3008

spi = machine.SPI(0)
cs = machine.Pin(22, machine.Pin.OUT)
cs.value(1) # disable chip at start

pwm = PIOPWM(0, 21, max_count=1023, count_freq=10_000_000)

chip = MCP3008(spi, cs)

error_count = 0
for _ in range(5):
    for i in range(0, 5):
        pwm.set((i*256)-1)
        sleep_ms(10)
        expected = 256*i
        difference = abs(chip.read(1)-expected)
        pc_difference = (100*difference)//max(expected, 10)
        if pc_difference > 8:
            error_count += 1
        sleep_ms(10)
if error_count == 0:
    print('all tests passed')
else:
    print('%d tests failed' % error_count)
