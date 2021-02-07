import binascii
import _thread
import time
import socket
import datetime

HOST2 = '131.180.165.26'
PORT1 = 999

MU02 = '100.6.0.12'
PORT2 = 994



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST2, PORT1))

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sx1:
        sx1.connect((MU02, PORT2))

        while True:
            data = s.recv(1024)
            data = data.decode("utf-8")
            data = str(data)

            if data == '2':
                print(2)
                fill = '219+2'
                fill = fill.encode()
                sx1.sendall(fill)
            else:
                print('else')


        print('Receive',repr(data))


