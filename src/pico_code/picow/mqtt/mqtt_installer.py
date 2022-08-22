from secrets import SSID, PASSWORD
from network_connection import connect
import upip


def install():
    connect(SSID, PASSWORD)
    upip.install('umqtt.simple')

install()