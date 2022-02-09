# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)

import drive

#import webrepl
#webrepl.start(password="icrs101")

#from network import WLAN
import network

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid="ICRS101", authmode=3, password="robotics101")


