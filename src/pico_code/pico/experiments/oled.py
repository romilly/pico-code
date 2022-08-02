import SSD1306
import machine


i2c = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0))
oled = SSD1306.SSD1306_I2C(128, 32, i2c)

oled.text('MicroPython', 10, 0)
oled.text('I2C + RP2 rock', 10, 16)
oled.show()








