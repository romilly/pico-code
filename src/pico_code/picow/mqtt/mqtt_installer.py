from secrets import SSID, PASSWORD
from network_connection import connect

connect(SSID, PASSWORD)
import upip
upip.install('umqtt.simple')