from machine import Pin, I2C
from pm25_mp_i2c import PM25_I2C
import time

i2c=I2C(0, sda=Pin(0), scl=Pin(1), freq=100000)
pm25 = PM25_I2C(i2c)

def try_to_read(count=5):
    for _ in range(count):
        try:
            pm25.read()
            return
        except:
            pass
        time.sleep(1)
    raise ValueError('could not read from PM2.5 after %d atttmepts' % count)
    
try_to_read()   
while True:
    print(pm25.read())
    time.sleep(1)