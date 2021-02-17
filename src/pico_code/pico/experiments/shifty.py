from machine import Pin
from time import sleep_ms, sleep_us

ser = Pin(5, Pin.OUT)
ser.value(0)
rclock = Pin(6, Pin.OUT)
rclock.value(0)
srclock = Pin(7, Pin.OUT)
srclock.value(0)


def srclock_pulse():
    srclock.value(1)
    sleep_us(10)
    srclock.value(0)
    sleep_us(10)


def rclock_pulse():
    rclock.value(1)
    sleep_us(10)
    rclock.value(0)
    sleep_us(10)


def cycle():
    srclock_pulse()
    ser.value(1)
    srclock_pulse()
    ser.value(0)
    sleep_ms(10)
    for j in range(9):
        rclock_pulse()
        sleep_us(10)
        srclock_pulse()
        sleep_ms(50)


while True:
    cycle()




