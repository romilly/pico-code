# Minimalist PCF8591 implementation
# No auto-increment, 4 x single-ended ADCs


class PCF8591:
    def __init__(self, i2c, addr=0x48):
        self.i2c = i2c
        self._addr = addr
        self._buffer = bytearray(2)

    def _write(self, buffer):
        self.i2c.writeto(self._addr, buffer)

    def _read(self):
        return self.i2c.readfrom(self._addr, 1)

    def adc_in(self, channel: int):
        self._buffer[0] = 0x40 | (channel & 0x03)
        self._write(self._buffer)
        self._read()
        return 	int.from_bytes(self._read(),'little')

    def dac_out(self, value):
        self._buffer[0] = 0x40
        self._buffer[1] = value
        self._write(self._buffer)

