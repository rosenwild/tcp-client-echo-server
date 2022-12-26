#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
connection = True
while connection:
    message = input('input yor message: ')
    sock.send(message.encode())
    if message == 'exit':
        print('goodbye')
        connection = False
        sock.close()
        break
    data = sock.recv(1024)
    print(data.decode())

