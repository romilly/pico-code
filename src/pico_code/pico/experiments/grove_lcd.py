# I think this will only work with a 3V3 to 5V I2c adaptor.

import time
import ustruct
import machine

i2c = machine.I2C(1, scl=machine.Pin(7), sda=machine.Pin(6))

# this device has two I2C addresses
DISPLAY_RGB_ADDR = 0x62
DISPLAY_TEXT_ADDR = 0x3e


class I2CDevice:
    def __init__(self, i2c, address):
        self.i2c =   i2c
        self._addr = address
        

    def write(self, reg, value):
        self.i2c.writeto(self._addr, ustruct.pack('<BB', reg, value))

    def _read(self, reg):
        self.i2c.writeto(self._addr, ustruct.pack('<B', reg), repeat=True)
        return self.i2c.readfrom(self._addr, 1)
    
rgb = I2CDevice(i2c, DISPLAY_RGB_ADDR)
lcd = I2CDevice(i2c, DISPLAY_TEXT_ADDR)


# set backlight to (R,G,B) (values from 0..255 for each)
def setRGB(r, g, b):
    rgb.write(0, 0)
    rgb.write(1, 0)
    rgb.write(0x08, 0xaa)
    rgb.write(4, r)
    rgb.write(3, g)
    rgb.write(2, b)


# send command to display (no need for external use)
def textCommand(cmd):
     lcd.write(0x80, cmd)


# set display text \n for second line(or auto wrap)
def setText(text):
    textCommand(0x01)  # clear display
    time.sleep(.05)
    textCommand(0x08 | 0x04)  # display on, no cursor
    textCommand(0x28)  # 2 lines
    time.sleep(.05)
    count = 0
    row = 0
    for c in text:
        if c == '\n' or count == 16:
            count = 0
            row += 1
            if row == 2:
                break
            textCommand(0xc0)
            if c == '\n':
                continue
        count += 1
        lcd.write(0x40, ord(c))


# Update the display without erasing the display
def setText_norefresh(text):
    textCommand(0x02)  # return home
    time.sleep(.05)
    textCommand(0x08 | 0x04)  # display on, no cursor
    textCommand(0x28)  # 2 lines
    time.sleep(.05)
    count = 0
    row = 0
    while len(text) < 32:  # clears the rest of the screen
        text += ' '
    for c in text:
        if c == '\n' or count == 16:
            count = 0
            row += 1
            if row == 2:
                break
            textCommand(0xc0)
            if c == '\n':
                continue
        count += 1
        lcd.write(0x40, ord(c))


# example code
if __name__ == "__main__":
    setText("Hello world\nThis is an LCD test")
    setRGB(0, 128, 64)
    time.sleep(2)
    for c in range(0, 255):
        setText_norefresh("Going to sleep in {}...".format(str(c)))
        setRGB(c, 255 - c, 0)
        time.sleep(0.1)
    setRGB(0, 255, 0)
    setText("Bye bye, this should wrap onto next line")
