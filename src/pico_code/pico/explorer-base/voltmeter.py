from machine import Pin, ADC
import picoexplorer as display
import utime

def clear():
    display.set_pen(0,0,0)
    display.clear()
    display.update()

def voltage_at(ip):
    raw = ip.read_u16()
    return 3.3 * raw / 62535


def show_voltages():
    inputs =  [ADC(26),ADC(27), ADC(28)]
    while True:
        for i in range(3):
            voltage = voltage_at(inputs[i])
            text = 'V%d %f4.2' % (i, voltage)
            display.text(text, 10, 30*i, 100, 5)
            display.update()
            utime.sleep_ms(100)

show_voltages()

