import binascii
import _thread
import time
import socket
import datetime

HOST2 = '131.180.165.26'
PORT1 = 999

# Define a function for the thread
def serverOne():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
        s1.connect((HOST2, PORT1))
        x = 1
        while x < 6:
            data1 = s1.recv(1024)
            data1new = data1.decode("utf-8")
            print(data1new)

# Create two threads as follows
try:
   _thread.start_new_thread( serverOne, ( ) )
   #_thread.start_new_thread( serverTwo, ( ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass

