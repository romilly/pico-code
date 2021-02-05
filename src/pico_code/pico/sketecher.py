import machine
import utime


class Sketcher:
    POT_LEFT = machine.ADC(27)
    POT_RIGHT = machine.ADC(26)

    def __init__(self, read=print):
        self.read = read

    def run(self):
        while True:
            self.read(self.POT_LEFT.read_u16(), self.POT_RIGHT.read_u16())
            utime.sleep_ms(100)

