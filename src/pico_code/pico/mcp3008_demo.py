from time import sleep
from mcp3008 import MCP3008

def run():
    chip = MCP3008()
    while True:
        print(chip.read(0))
        sleep(1)
