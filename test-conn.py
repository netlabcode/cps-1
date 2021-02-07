import binascii
import _thread
import time
import socket
import datetime

HOST2 = '131.180.165.26'
PORT1 = 999


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST2, PORT1))
    while True:
        data = s.recv(1024)
        print('Receive',repr(data))


