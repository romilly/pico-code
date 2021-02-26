import machine
import time

potentiometer = machine.ADC(26)


def run():
    while True:
        raw_v = potentiometer.read_u16()
        voltage = 3.3 * raw_v / 65535.0
        r_fixed = 1000 # Ohms
        try:
            r = r_fixed * voltage/(3.3 - voltage)
            print(r)
        except:
            pass
        time.sleep(1.0)
run()