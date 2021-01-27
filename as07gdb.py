import binascii
import _thread
import time
import socket
import psycopg2


HOST1 = '100.7.0.11'
HOST2 = '100.7.0.12'
HOST3 = '100.7.0.13'
HOST4 = '100.7.0.14'
HOST5 = '100.7.0.15'
HOST6 = '100.7.0.16'
HOST7 = '100.7.0.17'
HOST8 = '100.7.0.18'
HOST9 = '100.7.0.19'
HOST10 = '100.7.0.20'
PORT1 = 993
PORT2 = 994
PORTS1 = 881
PORTS2 = 883


#Database Connection
conn = psycopg2.connect(host="131.180.165.5",database="crpg", user="postgres", password="crpg")
conn.autocommit = True
cursor = conn.cursor()

# Define a function for the thread
def serverOne():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc1:
		sc1.connect((HOST1, PORT1))
		
		x = 1
		while x < 6:
			#recive data from server A
			data1 = sc1.recv(1024)

			strval1 = str(data1.decode("utf-8"))

			a,b,c,d,e,f,g = strval1.split("+")

			inserted_values = (
        		a,
        		b,
        		c,
        		d,
        		e,
        		f,
        		g
    		)

			cursor.execute(" INSERT INTO s07m1(dtime, cb_ctrl, cb_res, i_res, p_res, q_res, v_res) VALUES (%s,%s,%s,%s,%s,%s,%s)", inserted_values)


			print(strval1)

def serverTwo():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc1:
		sc1.connect((HOST2, PORT1))
		
		x = 1
		while x < 6:
			#recive data from server A
			data1 = sc1.recv(1024)

			strval1 = str(data1.decode("utf-8"))
            
			a,b,c,d,e,f,g,h,i,j,k,l,m,n = strval1.split("+")

			inserted_values = (
        		a,
        		b,
        		c,
        		d,
        		e,
        		f,
        		g,
                h,
                i,
                j,
                k,
                l,
                m,
                n
    		)

			cursor.execute(" INSERT INTO s07m2(dtime, cb_ctrl, cb_res, f_res, hv_p_res, hv_q_res, ld_res, lv_p_res, lv_q_res, tap, tap_ctrl, tap_mode, tap_res, v_res) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", inserted_values)


			print(strval1)


def serverThree():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc1:
		sc1.connect((HOST3, PORT1))
		
		x = 1
		while x < 6:
			#recive data from server A
			data1 = sc1.recv(1024)

			strval1 = str(data1.decode("utf-8"))

			a,b,c,d,e,f,g,h,i,j,k,l,m,n = strval1.split("+")

			inserted_values = (
        		a,
        		b,
        		c,
        		d,
        		e,
        		f,
        		g,
                h,
                i,
                j,
                k,
                l,
                m,
                n
    		)

			cursor.execute(" INSERT INTO s07m3(dtime, cb_ctrl, cb_res, f_res, hv_p_res, hv_q_res, ld_res, lv_p_res, lv_q_res, tap, tap_ctrl, tap_mode, tap_res, v_res) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", inserted_values)


			print(strval1)

def serverFour():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc1:
		sc1.connect((HOST4, PORT1))
		
		x = 1
		while x < 6:
			#recive data from server A
			data1 = sc1.recv(1024)

			strval1 = str(data1.decode("utf-8"))
            
			a,b,c,d,e,f,g,h,i,j,k = strval1.split("+")

			inserted_values = (
        		a,
        		b,
        		c,
        		d,
        		e,
        		f,
        		g,
                h,
                i,
                j,
                k
    		)

			cursor.execute(" INSERT INTO s07m4(dtime, cb_ctrl, cb_res, hv_p_res, hv_q_res, ld_res, lv_p_res, lv_q_res, tap_ctrl, tap_mode, tap_res) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", inserted_values)


			print(strval1)

def serverFive():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc1:
		sc1.connect((HOST5, PORT1))
		
		x = 1
		while x < 6:
			#recive data from server A
			data1 = sc1.recv(1024)

			strval1 = str(data1.decode("utf-8"))
            
            
			a,b,c= strval1.split("+")

			inserted_values = (
        		a,
        		b,
        		c
    		)

			cursor.execute(" INSERT INTO s07m5(dtime, cb_ctrl, cb_res) VALUES (%s,%s,%s)", inserted_values)
        
			print(5)

def serverSix():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc1:
		sc1.connect((HOST6, PORT1))
		
		x = 1
		while x < 6:
			#recive data from server A
			data1 = sc1.recv(1024)

			strval1 = str(data1.decode("utf-8"))
        
			a,b,c,d,e,f,g,h= strval1.split("+")

			inserted_values = (
        		a,
        		b,
        		c,
        		d,
        		e,
        		f,
        		g,
        		h
    		)

			cursor.execute(" INSERT INTO s07m6(dtime, cb_ctrl, cb_res, f_res, i_res, p_res, q_res, v_res) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", inserted_values)

			print(6)

def serverSeven():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc1:
		sc1.connect((HOST7, PORT1))
		
		x = 1
		while x < 6:
			#recive data from server A
			data1 = sc1.recv(1024)

			strval1 = str(data1.decode("utf-8"))

			a,b,c,d,e,f = strval1.split("+")

			inserted_values = (
        		a,
        		b,
        		c,
        		d,
        		e,
        		f
    		)

			cursor.execute(" INSERT INTO s07m7(dtime, cb_ctrl, cb_res, f_res, tap, v_res) VALUES (%s,%s,%s,%s,%s,%s)", inserted_values)


			print(7)

def serverEight():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc1:
		sc1.connect((HOST8, PORT1))
		
		x = 1
		while x < 6:
			#recive data from server A
			data1 = sc1.recv(1024)

			strval1 = str(data1.decode("utf-8"))

			a,b,c,d,e,f,g,h,i,j = strval1.split("+")

			inserted_values = (
        		a,
        		b,
        		c,
        		d,
        		e,
        		f,
        		g,
                h,
                i,
                j
    		)

			cursor.execute(" INSERT INTO s07m8(dtime, cb_ctrl, cb_res, f_res, ld_res, p_ctrl, p_res, q_res, v_ctrl, v_res) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", inserted_values)


			print(8)

def serverNine():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc1:
		sc1.connect((HOST9, PORT1))
		
		x = 1
		while x < 6:
			#recive data from server A
			data1 = sc1.recv(1024)

			strval1 = str(data1.decode("utf-8"))
            
            
			a,b,c= strval1.split("+")

			inserted_values = (
        		a,
        		b,
        		c
    		)

			cursor.execute(" INSERT INTO s07m9(dtime, cb_ctrl, cb_res) VALUES (%s,%s,%s)", inserted_values)
        
			print(9)

def serverTen():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc1:
		sc1.connect((HOST10, PORT1))
		
		x = 1
		while x < 6:
			#recive data from server A
			data1 = sc1.recv(1024)

			strval1 = str(data1.decode("utf-8"))

			a,b,c,d,e,f,g,h,i,j = strval1.split("+")

			inserted_values = (
        		a,
        		b,
        		c,
        		d,
        		e,
        		f,
        		g,
                h,
                i,
                j
    		)

			cursor.execute(" INSERT INTO s07m10(dtime, cb_ctrl, cb_res, f_res, ld_res, p_ctrl, p_res, q_res, v_ctrl, v_res) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", inserted_values)


			print(10)

# Create two threads as follows
try:
   _thread.start_new_thread( serverOne, ( ) )
   _thread.start_new_thread( serverTwo, ( ) )
   _thread.start_new_thread( serverThree, ( ) )
   _thread.start_new_thread( serverFour, ( ) )
   _thread.start_new_thread( serverFive, ( ) )
   _thread.start_new_thread( serverSix, ( ) )
   _thread.start_new_thread( serverSeven, ( ) )
   _thread.start_new_thread( serverEight, ( ) )
   _thread.start_new_thread( serverNine, ( ) )
   _thread.start_new_thread( serverTen, ( ) )

except:
   print ("Error: unable to start thread")

while 1:
   pass