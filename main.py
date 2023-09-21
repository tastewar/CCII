import adafruit_ntp
import socketpool
import time
import wifi
import os

# Get wifi details and more from a secrets.py file
wifi.radio.connect(os.getenv("CIRCUITPY_WIFI_SSID"), os.getenv("CIRCUITPY_WIFI_PASSWORD"))

pool = socketpool.SocketPool(wifi.radio)
ntp = adafruit_ntp.NTP(pool, tz_offset=0)

while True:
    print(ntp.datetime)
    time.sleep(1)