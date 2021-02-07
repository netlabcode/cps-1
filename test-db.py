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

one_query = "SELECT * from s07m10 ORDER BY no DESC"

"""
x = 0
while x <= 5:
    cursor.execute(one_query)
    one_record = cursor.fetchone()
    print(one_record[2])
    print(one_record[3])
    time.sleep(2)
"""
HOST = ''
PORT = 999


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            cursor.execute(one_query)
            one_record = cursor.fetchone()
            d = str(one_record[2])
            data = d.encode()
            conn.sendall(data)
            time.sleep(2)




