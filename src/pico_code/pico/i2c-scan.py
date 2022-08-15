from machine import Pin, I2C

bus = 0
i2c = I2C(bus, scl=Pin(1), sda=Pin(0), freq=40000)

print('scanning I2C bus %d' % bus)
devices = i2c.scan()

print(len(devices), 'device(s)')

for device in devices:
    print('address %d (0x%02x)' % (device, device))