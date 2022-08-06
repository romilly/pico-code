"""
Control an MCP23008 8-bit Port expander via I2C

See https://www.microchip.com/wwwproducts/en/MCP23008
This implements a subset of chip features.
"""

# some of this code was copied from code for the MicroBit
# at present, I think the read code is broken :(

import ustruct

class MCP23008:
    IODIR = 0x00
    IPOL =  0x01
    GPPU =  0x06
    GPIO =  0x09

    def __init__(self, i2c, addr=None):
        self._addr = addr if addr else 0x20
        self.i2c = i2c
        self.ipol(0x000) # set normal polarity

    def _write(self, reg, value):
        self.i2c.writeto(self._addr, ustruct.pack('<BB', reg, value))

    def _read(self, reg):
        self.i2c.writeto(self._addr, ustruct.pack('<B', reg), stop=False)
        return self.i2c.readfrom(self._addr, 1)

    def output(self, val):
        self._write(self.GPIO, val)

    def input(self):
        return self._read(self.GPIO)

    def direction(self, val):
        self._write(self.IODIR, val)

    def gppu(self, val):
        self._write(self.GPPU, val)

    def ipol(self, val):
        self._write(self.IPOL, val)
