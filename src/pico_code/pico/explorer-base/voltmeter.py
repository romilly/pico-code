from machine import Pin, ADC
import picoexplorer as display
import utime


def clear():
    display.set_pen(0, 0, 0)
    display.clear()
    display.update()


def voltage_at(ip):
    raw = ip.read_u16()
    return 3.3 * raw / 62535


def blk():
    display.set_pen(0, 0, 0)
    display.clear()
    display.update()


def title(msg, r, g, b):
    blk()
    display.set_pen(r, g, b)
    display.text(msg, 20, 70, 200, 4)
    display.update()
    utime.sleep(2)
    # blk()


def show_voltages():
    width = display.get_width()
    height = display.get_height()
    display_buffer = bytearray(width * height * 2)
    display.init(display_buffer)
    inputs = [ADC(26), ADC(27), ADC(28)]
    while True:
        title('Voltmeter', 255, 255, 0)
        for i in range(3):
            voltage = voltage_at(inputs[i])
            text = 'V%d %4.2f' % (i, voltage)
            display.set_pen(255, 255, 255)
            display.text(text, 10, 120 + 30 * i, 200, 2)
            display.update()
        utime.sleep_ms(1000)
        blk()


show_voltages()
