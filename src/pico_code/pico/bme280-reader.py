from machine import Pin, I2C        #importing relevant modules & classes
from time import sleep
import bme280       #importing BME280 library

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)    
bme = bme280.BME280(address=0x77, i2c=i2c)  

while True:
  print(bme.values)
  sleep(10)           #delay of 10s