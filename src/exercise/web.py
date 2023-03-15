# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 18:02:01 2023

@author: He
"""

import socket

socket_1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_1.connect(("localhost", 5555)) # Address tuple

socket_1.send(bytes("hello world", encoding="UTF-8"))


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 5555))
serversocket.listen()
(socket_2, address) = serversocket.accept()
b = socket_2.recv(30)
print(str(b))