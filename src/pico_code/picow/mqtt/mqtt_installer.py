from secrets import SSID, PASSWORD
from network_connection import connect
import upip


def install():
    try:
        import umqtt.simple
    except:
        connect(SSID, PASSWORD)
        upip.install('umqtt.simple')

install()