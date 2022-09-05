import unittest
from io import BytesIO

from hamcrest import assert_that, raises, equal_to, calling

from src.pico_code.picow.pmsa003i_packet_parser import aqi_reading


def u16(value: int):
    return (value).to_bytes(2, byteorder="big")


class PacketBuilder:
    def __init__(self, *values):
        self._values = values
        self._header = b"BM"
        self._length = 28
        self._checksum = None # calculated later if none is given

    def build(self):
        packet_stream = BytesIO()
        packet_stream.write(self._header)
        packet_stream.write(u16(self._length))
        data = 13*[0] # a packet contains 13 data items, though the last one just contains error info.
        for i, value in enumerate(self._values):
           data[i] = value
        for value in data:
            packet_stream.write(u16(value))
        checksum = sum(packet_stream.getvalue()) if self._checksum is None else self._checksum
        packet_stream.write(u16(checksum))
        packet = packet_stream.getvalue()
        packet_stream.close()
        return packet

    def with_header(self, header: bytes):
        self._header = header
        return self

    def with_length(self, length: int):
        self._length = length
        return self

    def with_checksum(self, checksum: int):
        self._checksum = checksum
        return self


class PacketParserTestCase(unittest.TestCase):
    def test_detects_invalid_packet_length(self):
        packet = PacketBuilder().with_header(b"NG").build()[:30]
        self.expects_error(packet, 'Invalid PM2.5 packet length')

    def test_detects_invalid_header(self):
        packet = PacketBuilder().with_header(b"NG").build()
        self.expects_error(packet, 'Invalid PM2.5 header')

    def test_detects_invalid_frame_length(self):
        packet = PacketBuilder().with_length(13).build()
        self.expects_error(packet, 'Invalid PM2.5 frame length')

    def test_detects_invalid_checksum(self):
        packet = PacketBuilder().with_checksum(0).build()
        self.expects_error(packet, 'Invalid PM2.5 checksum')

    def test_parses_valid_packet(self):
        packet = PacketBuilder(1, 2, 4, 0, 7).build()
        parsed = aqi_reading(packet)
        keys = ["pm10 standard",
                    "pm25 standard",
                    "pm100 standard",
                    "pm10 env",
                    "pm25 env"]
        for key, value in zip(keys, (1, 2, 4, 0, 7)):
            assert_that(parsed[key], equal_to(value))

    def expects_error(self, packet, error):
        assert_that(calling(aqi_reading).with_args(packet),
                    raises(RuntimeError, error))


if __name__ == '__main__':
    unittest.main()
