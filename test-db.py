import binascii
import _thread
import time
import socket
import psycopg2


HOST1 = '100.6.0.11'
HOST2 = '100.6.0.12'
HOST3 = '100.6.0.13'
HOST4 = '100.6.0.14'
HOST5 = '100.6.0.15'
HOST6 = '100.6.0.16'
PORT1 = 993
PORT2 = 994
PORTS1 = 881
PORTS2 = 883


#Database Connection
conn = psycopg2.connect(host="131.180.165.5",database="crpg", user="postgres", password="crpg")
conn.autocommit = True
cursor = conn.cursor()
db_version = cursor.execute('SELECT version()')
print(db_version)
