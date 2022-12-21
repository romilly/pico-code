# adapted from Adafruit code  https://github.com/adafruit/Adafruit_CircuitPython_PM25.git

import struct


def aqi_reading(buffer):
    reading = {}

    if not len(buffer) == 32:
        raise RuntimeError("Invalid PM2.5 packet length")

    # check packet header
    if not buffer[0:2] == b"BM":
        raise RuntimeError("Invalid PM2.5 header")

    # check frame length
    frame_len = struct.unpack(">H", buffer[2:4])[0]
    if frame_len != 28:
        raise RuntimeError("Invalid PM2.5 frame length")
    
    # verify checksum
    expected = struct.unpack(">H", buffer[30:32])[0]
    actual = sum(buffer[0:30])
    if actual != expected:
        raise RuntimeError("Invalid PM2.5 checksum - expected %d, got %d" % (expected, actual))


    # unpack data
    (
        reading["pm10 standard"],
        reading["pm25 standard"],
        reading["pm100 standard"],
        reading["pm10 env"],
        reading["pm25 env"],
        reading["pm100 env"],
        reading["particles 03um"],
        reading["particles 05um"],
        reading["particles 10um"],
        reading["particles 25um"],
        reading["particles 50um"],
        reading["particles 100um"],
    ) = struct.unpack(">HHHHHHHHHHHH", buffer[4:28])
    return reading
