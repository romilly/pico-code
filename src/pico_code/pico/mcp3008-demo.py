from time import sleep
from mcp3008 import MCP3008

spi = machine.SPI(0, baudrate=100000)
cs = machine.Pin(22, machine.Pin.OUT)

chip = MCP3008(spi, cs)

while True:
    print(chip.read(0))
    sleep(1)
