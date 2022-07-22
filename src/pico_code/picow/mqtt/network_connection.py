import network
import time


def connect(ssid, password, max_wait=10):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        time.sleep(1)
    if wlan.status() != 3:
        raise RuntimeError('network connection failed')
    return wlan
