# adapted from Adafruit code  https://github.com/adafruit/Adafruit_CircuitPython_PM25.git

import time
from machine import Pin

from pmsa003i_packet_parser import aqi_reading


class PMSA003i:

    def __init__(self, i2c, reset_pin: Pin = None) -> None:
        self._buffer = bytearray(32)
        self._i2c = i2c
        self._address = 0x12
        if reset_pin:
            # Reset device
            reset_pin.direction = Pin.OUTPUT
            reset_pin.value = False
            time.sleep(0.01)
            reset_pin.value = True
            # it takes at least a second to start up
            time.sleep(1)

    def _read_into_buffer(self) -> None:
        try:
            self._i2c.readfrom_into(self._address, self._buffer)
        except OSError as err:
            raise RuntimeError("Unable to read from PM2.5 over I2C") from err

    def read(self) -> dict:
        """Read any available data from the air quality sensor and
        return a dictionary with available particulate/quality data"""
        self._read_into_buffer()
        return aqi_reading(self._buffer)

