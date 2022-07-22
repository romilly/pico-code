from machine import Pin
from time import sleep


buzzer = Pin(17,Pin.OUT)

try:
    while True:
        buzzer.value(1)
        sleep(1)
        buzzer.value(0)
        sleep(1)
finally:
        buzzer.value(0)
