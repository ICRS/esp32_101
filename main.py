import network
from MicroWebSrv2 import *
import drive

try:
  import usocket as socket
except:
  import socket

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid="ICRS101", authmode=3, password="robotics101")

# print(ap.ifconfig())
#
# def OnTextMessage(webSocket, msg):
#     print(msg)
#     webSocket.SendTextMessage("Received")
#
# def OnWebSocketAccepted(microWebSrv2, webSocket) :
#     print("Received")
#     webSocket.OnTextMessage = OnTextMessage
#     print('Accepted from %s:%s.' % webSocket.Request.UserAddress)


# websocket = MicroWebSrv2.LoadModule('WebSockets')
#websocket.OnWebSocketProtocol = OnWebSocketProtocol
# websocket.OnWebSocketAccepted = OnWebSocketAccepted

#mws = MicroWebSrv2()
#mws.RootPath = 'www'
#mws.NotFoundURL = '/'
#mws.StartManaged()

def web_page():
    with open("www/control.html") as f:
        html = f.read()
    print(html)
    return html

addr = socket.getaddrinfo('0.0.0.0',80)[0][-1]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(addr)
s.listen(5)

webpage = web_page()

# addr = socket.getaddrinfo('0.0.0.0', 81)[0][-1]
# dataSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# dataSocket.bind(addr)
# dataSocket.listen(5)

driveBase = drive.driveBase(25,13,26,27,14,12)

while True:
    conn, addr = s.accept()
    print(addr)
    request = conn.recv(1024)
    request = str(request)
    print('Request = %s' % request)
    if("forward" in request):
        drive.forward(0.8)
    elif("backward" in request):
        drive.backward(0.8)
    else:
        drive.forward(0)

    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(webpage)
    conn.close()
