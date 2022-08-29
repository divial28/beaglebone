#!/usr/bin/python3

import socket
import threading
import time

HOST = "192.168.7.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    def send():
        s.sendall(b"data")
        threading.Timer(0.1, send).start()

    threading.Timer(0.1, send).start()

    while True:
        ...

    # data = s.recv(1024)

# print(f"Received {data!r}")

