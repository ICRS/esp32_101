# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)

import drive

#import webrepl
#webrepl.start(password="icrs101")

#from network import WLAN
import network
from MicroWebSrv2 import *

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid="ICRS101", authmode=3, password="robotics101")

def OnWebSocketProtocol(microWebSrv2, protocols) :
    if WS_CHAT_SUB_PROTOCOL in protocols :
        return WS_CHAT_SUB_PROTOCOL

def OnWebSocketAccepted(microWebSrv2, webSocket) :
    print('New WebSocket (myGreatChat proto) accepted from %s:%s.' % webSocket.Request.UserAddress)

websocket = MicroWebSrv2.LoadModule('WebSockets')
websocket.OnWebSocketProtocol = OnWebSocketProtocol
websocket.OnWebSocketAccepted = OnWebSocketAccepted

