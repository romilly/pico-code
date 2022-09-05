from machine import Pin, I2C
from pmsa003i import PMSA003i
import time

i2c=I2C(0, sda=Pin(0), scl=Pin(1), freq=100000) # seems to be the maximum I2C bit rate that the PMS03i can cope with
pmsa003i = PMSA003i(i2c)

def try_to_read(count=5):
    for _ in range(count):
        try:
            pmsa003i.read()
            return
        except:
            pass
        time.sleep(1)
    raise ValueError('could not read from PM2.5 after %d atttmepts' % count)
    
try_to_read()   
while True:
    print(pmsa003i.read())
    time.sleep(1)