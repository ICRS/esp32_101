import network
from MicroWebSrv2 import *

try:
  import usocket as socket
except:
  import socket

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


def web_page():
    with open("control.html") as f:
        html = f.read()
    return html


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.4.1', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.sendall(response)