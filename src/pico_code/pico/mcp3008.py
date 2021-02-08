"""
MicroPython library for the MCP3008 series of analog-to-digital converters

This code is adapted from Adafruit's library
https://github.com/adafruit/Adafruit_CircuitPython_MCP3xxx
"""


class MCP3008:
    """
    MCP3008 8-channel, 10-bit, analog-to-digital converter.
    """


    def __init__(self, spi, cs, ref_voltage=3.3):
        """
        Initialise MC3008 instance.

        :param spi: SPI bus the ADC is connected to.
        :param cs: Chips elect pin.
        :param ref_voltage: Voltage into (Vin) the ADC.
        """
        self.cs = cs
        self._spi_device = spi
        self._out_buf = bytearray(3)
        self._out_buf[0] = 0x01
        self._in_buf = bytearray(3)
        self._ref_voltage = ref_voltage


    def reference_voltage(self):
        """Returns the MCP3xxx's reference voltage. (read-only)"""
        return self._ref_voltage


    def read(self, pin, is_differential=False) -> int:
        """read the voltage on or petween a pin or pario of pins as a scaled integer.
        :param int pin: individual or differential pin.
        :param bool is_differential: single-ended or differential read.
        :return: The returned value ranges from 0 to 1023 inclusive. 0 = 0V0, 1023 = 100% of reference voltage.

        If you want to do a differential read, the ``pin`` parameter should be the first of the two pins
        associated with the desired differential channel mapping.
        """

        self.cs.value(0)  # select
        self._out_buf[1] = ((not is_differential) << 7) | (pin << 4)
        self._spi_device.write_readinto(self._out_buf, self._in_buf)
        self.cs.value(1)  # turn off
        return ((self._in_buf[1] & 0x03) << 8) | self._in_buf[2]
