import socket
import sys

if len(sys.argv) < 2:
    print 'please set send message'
    sys.exit(1)

ip, port = '120.27.13.239', 8014
# ip, port = '127.0.0.1', 4321

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(sys.argv[1], (ip, port))
print 'send to %s, %d udp success' % (ip, port)
s.close()
