#!/usr/bin/python3

import socketserver
import threading

class UDPHandler(socketserver.DatagramRequestHandler):
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        print('{} wrote:'.format(self.client_address[0]))
        print(data)
        socket.sendto(data.upper(), self.client_address)

if __name__ == '__main__':
    HOST, PORT = "192.168.6.1", 65432
    
    with socketserver.ThreadingUDPServer((HOST, PORT), UDPHandler) as server:
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.daemon = True
        server_thread.start()

        def bgproc():
            print('background process')
            threading.Timer(0.1, bgproc).start()
        
        threading.Timer(0.1, bgproc).start()

        while True:
            ...
