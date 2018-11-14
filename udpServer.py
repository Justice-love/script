import socket

BUFSIZE = 1024
ip_port = ('127.0.0.1', 9999)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(ip_port)
while True:
    data, client_addr = server.recvfrom(BUFSIZE)
    print data

