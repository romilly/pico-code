from machine import Pin, ADC
import picoexplorer as display
import time
              
def show_voltages():
    width = display.get_width()
    height = display.get_height()
    display_buffer = bytearray(width * height * 2)
    display.init(display_buffer)
    
    while True:
        display.set_pen(0, 0, 0)
        display.clear()
        display.set_pen(255, 255, 255)
        display.text('Voltmeter', 10, 10, 200, 4)
        for i in range(3):
            voltage = 3.3 * display.get_adc(i)
            display.text('V%d %4.2f' % (i, voltage), 10, 50 + 30 * i, 200)
        display.update()
        time.sleep(0.5)
        
show_voltages()
