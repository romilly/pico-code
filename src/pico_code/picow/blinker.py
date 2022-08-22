import machine
import time

led = machine.Pin('LED', machine.Pin.OUT)

def blink(duration=1.0):
    led.on()
    time.sleep(duration/2)
    led.off()
    time.sleep(duration/2)
    
def blinks(count, duration=1.0):
    for i in range(count):
        blink(duration)
        
def sos():
    blinks(3, 0.5)
    time.sleep(1)
    blinks(3, 1.0)
    time.sleep(1)
    blinks(3, 0.5)
    