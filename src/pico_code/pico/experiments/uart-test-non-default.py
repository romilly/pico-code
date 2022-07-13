"""
MicroPython code to read and write from UART1 on the Pico


UART0 is not available as it is used for the REPL.

To test, you can use a 3V3 FTDI cable or similar device that connects a host computer with the Pico.
NB: Make sure it's a 3V3 cable, not a 5V cable, or you could kill your PIco!!

Connect FTDI black to Pico GND.
Connect FTDI yellow to Pico GP4.
Connect FTDI orange to Pico GP5.
"""
from machine import UART, Pin

ser = UART(1, 115200,tx=Pin(8), rx=Pin(9))

ser.write('Hello UART!\r\n')

while True:
    ch = ser.read(1)
    reply = 'I saw %s \r\n' % ch
    ser.write(reply)
    print(reply)