import socket
import sys

if len(sys.argv) < 2:
    print 'please set send message'
    sys.exit(1)

ip, port = '120.27.13.239', 8013
# ip, port = '127.0.0.1', 4321

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

s.send(sys.argv[1])

buffer = []
d = s.recv(1024)
buffer.append(d)
data = ''.join(buffer)
print data
s.close()
