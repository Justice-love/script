from SocketServer import TCPServer, StreamRequestHandler

host = '127.0.0.1'
port = 4321
addr = (host,port)

class MyRequestHandler(StreamRequestHandler):
    def handle(self):
        print self.rfile.readline()

tcpServ = TCPServer(addr,MyRequestHandler)
print 'waiting for connection'
tcpServ.serve_forever()