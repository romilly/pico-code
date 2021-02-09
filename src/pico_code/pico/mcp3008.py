"""
Drive am MCP3008 8-channel ADC from a Raspberry Pi Pico using MicroPython

Code makes much use of Tony di Cola's CircuitPython code at
https://github.com/adafruit/Adafruit_CircuitPython_MCP3xxx
adapted to use 'vanilla' MicroPython on the Pico.

Thanks, @Adafruit, for all you've given us!
"""

import machine


class MCP3008:

    def __init__(self, ref_voltage=3.3):
        spi_sck = machine.Pin(2)
        spi_tx = machine.Pin(3)
        spi_rx = machine.Pin(4)
        self.spi_cs = machine.Pin(22, machine.Pin.OUT)
        self.spi_cs.value(1) # ncs on
        self._spi_device = machine.SPI(0, baudrate=100000, sck=spi_sck, mosi=spi_tx, miso=spi_rx)
        self._out_buf = bytearray(3)
        self._out_buf[0] = 0x01
        self._in_buf = bytearray(3)
        self._ref_voltage = ref_voltage

    def reference_voltage(self):
        """Returns the MCP3xxx's reference voltage. (read-only)"""
        return self._ref_voltage

    def read(self, pin, is_differential=False):
        """SPI Interface for MCP3xxx-based ADCs reads. Due to 10-bit accuracy, the returned
        value ranges [0, 1023].
        :param int pin: individual or differential pin.
        :param bool is_differential: single-ended or differential read.
        .. note:: This library offers a helper class called `AnalogIn`_ for both single-ended
            and differential reads. If you opt to not implement `AnalogIn`_ during differential
            reads, then the ``pin`` parameter should be the first of the two pins associated with
            the desired differential channel mapping.
        """
        self.spi_cs.value(0) # select
        self._out_buf[1] = ((not is_differential) << 7) | (pin << 4)
        self._spi_device.write_readinto(self._out_buf, self._in_buf)
        self.spi_cs.value(1) # turn off
        return ((self._in_buf[1] & 0x03) << 8) | self._in_buf[2]
