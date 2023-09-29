import adafruit_ntp as ntp
import socketpool
import time
import wifi
import ssl
import os
import rtc
import microcontroller
import json
import adafruit_requests as requests
import board
import neopixel

def HexEncode(bs):
    if not bs:
        return ''
    
    s = ''

    for b in bs:
        s += hex(b)[2:]
    return s

def DisplayTime(t, tcolor, daychar, daycolor, periodchar, periodcolor):
    ts = time.localtime(t)
    print(f"{ts.tm_hour:02d}"+':'+f"{ts.tm_min:02d}"+':'+f"{ts.tm_sec:02d}","Day:",daychar,"Period:",periodchar)

def GetCurrentBellTime():
    return time.time()+config["belloffset"]

# Get wifi details and more from settings.toml file
wifi.radio.connect(os.getenv("CIRCUITPY_WIFI_SSID"), os.getenv("CIRCUITPY_WIFI_PASSWORD"))

pool = socketpool.SocketPool(wifi.radio)

rq = requests.Session(pool, ssl.create_default_context())
devid = HexEncode(microcontroller.cpu.uid)
print("Device ID: " + devid)

resp = rq.get("https://cclock.tastewar.com/" + devid)
config=resp.json()

tzresp=rq.get("https://worldtimeapi.org/api/timezone/" + config["timezone"] )
tz=json.loads(tzresp.text)
my_offset = tz["raw_offset"]
if tz["dst"]:
    my_offset+=tz["dst_offset"]

print("time zone offset in seconds",my_offset)

attempts=0
ntpc = ntp.NTP(pool, tz_offset=my_offset/3600)

while attempts<5:
    try:
        attempts+=1
        rtc.RTC().datetime = ntpc.datetime
        break
    except:
        print("failed getting ntp time")

p = neopixel.NeoPixel(board.NEOPIXEL, 1)
resp = rq.get("https://cclock.tastewar.com/" + devid)
print(resp.json())
r=255
g=0
b=0
while True:
    #print(time.localtime())
    DisplayTime(GetCurrentBellTime(),0,'A',0,3,0)
    time.sleep(1)
    p.fill((r,g,b))
    if r==255:
        r=0
        g=255
        b=0
    elif g==255:
        r=0
        g=0
        b=255
    else:
        r=255
        g=0
        b=0

