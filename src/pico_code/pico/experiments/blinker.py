"""
Example for remote control from host via Serial link.

This is the code to run on the Pico.
It sets up the onboard LED and allows you to turn it on or off.
"""
from machine import Pin

#use onboard LED which is controlled by Pin 25
led = Pin(25, Pin.OUT)


# Turn the LED on
def on():
    led.value(1)

# Turn the LED off
def off():
    led.value(0)
