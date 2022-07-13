"""
Cycle the Tiny2040's on-board LED through a range of colours
"""
from machine import Pin
from time import sleep_ms

r = Pin(18, Pin.OUT)
g = Pin(19, Pin.OUT)
b = Pin(20, Pin.OUT)
while True:
    for i in range(2):
        r.toggle()
        for j in range(2):
            g.toggle()
            for k in range(2):
                b.toggle()
                sleep_ms(250)


