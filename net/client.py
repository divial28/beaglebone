#!/usr/bin/python3

import threading
import socket
import sys

HOST, PORT = "192.168.6.1", 65432
data = " ".join(sys.argv[1:])


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

    def send():
        s.sendto(bytes(data + "\n", "utf-8"), (HOST, PORT))
        threading.Timer(0.1, send).start()

    threading.Timer(0.1, send).start()

    while True:
        ...