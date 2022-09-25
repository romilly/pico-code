from secrets import SSID, PASSWORD
from network_connection import connect
import upip


def install():
    try:
        import umqtt.robust
    except:
        connect(SSID, PASSWORD)
        upip.install('umqtt.robust')

install()