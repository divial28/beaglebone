#!/usr/bin/python3

# from http import client
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("localhost", 10100))
server_socket.listen()

while True:
    print('listening')
    client_socket, addr = server_socket.accept()
    print('incoming connection from ', addr)

    while True:
        print('receiving')
        request = client_socket.recv(1024)

        if not request:
            break
        else:
            response = b'hello world!\n'
            client_socket.send(response)

