"""
MicroPython Library for MCP3008 8-channel ADC with SPI

Datasheet for the MCP3008: https://www.microchip.com/datasheet/MCP3008

This code makes much use of Adafruit's CircuitPython code at
https://github.com/adafruit/Adafruit_CircuitPython_MCP3xxx
adapted for MicroPython.

Tested on the Raspberry Pi Pico.

Thanks, @Raspberry_Pi and @Adafruit, for all you've given us!
"""

import machine


class MCP3008:

    def __init__(self, spi, cs, ref_voltage=3.3):
        """
        Create MCP3008 instance

        Args:
            spi: configured SPI bus
            cs:  pin to use for chip select
            ref_voltage: r
        """
        self.cs = cs
        self.cs.value(1) # ncs on
        self._spi = spi
        self._out_buf = bytearray(3)
        self._out_buf[0] = 0x01
        self._in_buf = bytearray(3)
        self._ref_voltage = ref_voltage

    def reference_voltage(self) -> float:
        """Returns the MCP3xxx's reference voltage as a float."""
        return self._ref_voltage

    def read(self, pin, is_differential=False):
        """
        read a voltage or voltage difference using the MCP3008.

        Args:
            pin: the pin to use
            is_differential: if true, return the potential difference between two pins,


        Returns:
            voltage in range [0, 1023] where 1023 =

        """

        self.cs.value(0) # select
        self._out_buf[1] = ((not is_differential) << 7) | (pin << 4)
        self._spi.write_readinto(self._out_buf, self._in_buf)
        self.cs.value(1) # turn off
        return ((self._in_buf[1] & 0x03) << 8) | self._in_buf[2]
