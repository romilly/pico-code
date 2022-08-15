"""
Proof-of-concept driver for the AD7307 DAC.
"""
from utime import sleep_ms, sleep_us


class AD7303():
    def __init__(self):
        spi_sck = machine.Pin(2)
        spi_tx = machine.Pin(3)
        spi_rx = machine.Pin(4)
        self.spi_cs = machine.Pin(22, machine.Pin.OUT)
        self.spi_cs.value(1)  # ncs on
        self._spi_device = machine.SPI(0, baudrate=30000000, sck=spi_sck, mosi=spi_tx, miso=spi_rx)
        self._out_buf = bytearray(2)

    def set_output_A(self, v256):
        self._out_buf[0] = 32
        self._out_buf[1] = v256
        self.spi_cs.value(0)  # select
        self._spi_device.write(self._out_buf)
        self.spi_cs.value(1)  # deselect


dac = AD7303()
while True:
    dac.set_output_A(255)
    sleep_us(25)
    dac.set_output_A(0)
    sleep_us(25)



