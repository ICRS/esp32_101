import network
import drive

try:
  import usocket as socket
except:
  import socket

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid="ICRS101", authmode=3, password="robotics101")

def web_page():
    with open("web/control.html") as f:
        html = f.read()
    print(html)
    return html

addr = socket.getaddrinfo('0.0.0.0',80)[0][-1]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(addr)
s.listen(1)

webpage = web_page()

driveBase = drive.DriveBase(16,13,5,4,12,14)

while True:
    conn, addr = s.accept()
    print(addr)
    request = conn.recv(1024)
    request = str(request)
    print('Request = %s' % request)

    # handle requests
    if("forward" in request):
        driveBase.forward(0.8)
        print("forward")

    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(webpage)
    conn.close()
