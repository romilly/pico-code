from src.pico_code.picow.secrets import SSID, PASSWORD
from src.pico_code.picow.network_connection import connect
import upip


def install():
    connect(SSID, PASSWORD)
    upip.install('umqtt.simple')

install()