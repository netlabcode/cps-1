import binascii
import _thread
import time
import socket
import time
import sqlite3
from sqlite3 import Error
import datetime

#Predefined parameters
MU01 = '100.7.0.11'
MU02 = '100.7.0.12'
MU03 = '100.7.0.13'
MU04 = '100.7.0.14'
MU05 = '100.7.0.15'
MU06 = '100.7.0.16'
MU07 = '100.7.0.17'
MU08 = '100.7.0.18'
MU09 = '100.7.0.19'
MU10 = '100.7.0.20'
PORT1 = 991
PORT2 = 992

def create_connection(db_file):
	conn = None
	try:
		conn = sqlite3.connect(db_file, timeout=10)
	except Error as e:
		print(e)
	return conn

def db_connect():
	datafile="s07.db"
	con = create_connection(datafile)
	return con


# Define a function for the thread
def serverMU01():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
		s1.connect((MU01, PORT1))
		x = 1
		while x < 6:
			#recive data from server
			data1 = s1.recv(1024)
			
			try: 
				#parsing data
				data1new = data1.decode("utf-8")
				datet,a,b,ce,d,e,f = data1new.split("+")

				#save db
				con = db_connect()
				c = con.cursor()
				#datet = datetime.datetime.now()
				c.execute("INSERT INTO mu01(xtime, B19_Li_16_19_CB_ctrl, B19_Li_16_19_CB_res, B19_Li_16_19_I_res, B19_Li_16_19_P_res, B19_Li_16_19_Q_res, B19_Li_16_19_V_res) VALUES (?,?,?,?,?,?,?)",(datet,int(a),int(b),float(ce),float(d),float(e),float(f)))
				#c.execute("INSERT INTO mu01(xtime, B23_Li_23_24_CB_ctrl) VALUES (?,?)",(datet,int(a)))
				con.commit()
				con.close()
			except Exception:
				print("mu01")
				pass



def serverMU02():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
		s2.connect((MU02, PORT1))
		x = 1
		while x < 6:
			#recive data from server
			data2 = s2.recv(1024)
			#print('MU02:',data2)

			#parsing data
			data1new = data2.decode("utf-8")

			try:
				datet,a,b,ce,d,e,f,g,h,i,j,k,l,m = data1new.split("+")
				#save db
				con = db_connect()
				c = con.cursor()
				#datet = datetime.datetime.now()
				c.execute("INSERT INTO mu02(xtime, B19_Tr_19_33_CB_ctrl, B19_Tr_19_33_CB_res, B19_Tr_19_33_Ld_res , B19_Tr_19_33_V_res, B19_Tr_19_33_f_res, B19_Tr_19_33_hv_P_res, B19_Tr_19_33_hv_Q_res, B19_Tr_19_33_lv_P_res, B19_Tr_19_33_lv_Q_res, B19_Tr_19_33_tap, B19_Tr_19_33_tap_ctrl, B19_Tr_19_33_tap_mode, B19_Tr_19_33_tap_res) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(datet,int(a),int(b),float(ce),float(d),float(e),float(f),float(g),float(h),float(i),int(j),int(k),int(l),int(m)))
				con.commit()
				con.close()
			except Exception:
				print("mu02")
				pass


def serverMU03():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
		s2.connect((MU03, PORT1))
		x = 1
		while x < 6:
			#recive data from server
			data2 = s2.recv(1024)

			#parsing data
			data1new = data2.decode("utf-8")

			try:
				datet,a,b,ce,d,e,f,g,h,i,j,k,l,m = data1new.split("+")
				#save db
				con = db_connect()
				c = con.cursor()
				#datet = datetime.datetime.now()
				c.execute("INSERT INTO mu03(xtime, B19_Tr_19_20_CB_ctrl, B19_Tr_19_20_CB_res, B19_Tr_19_20_Ld_res , B19_Tr_19_20_V_res, B19_Tr_19_20_f_res, B19_Tr_19_20_hv_P_res, B19_Tr_19_20_hv_Q_res, B19_Tr_19_20_lv_P_res, B19_Tr_19_20_lv_Q_res, B19_Tr_19_20_tap, B19_Tr_19_20_tap_ctrl, B19_Tr_19_20_tap_mode, B19_Tr_19_20_tap_res) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(datet,int(a),int(b),float(ce),float(d),float(e),float(f),float(g),float(h),float(i),int(j),int(k),int(l),int(m)))
				#c.execute("INSERT INTO mu01(xtime, B23_Li_23_24_CB_ctrl) VALUES (?,?)",(datet,int(a)))
				con.commit()
				con.close()
			except Exception:
				print("mu03")
				pass


def serverMU04():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
		s2.connect((MU04, PORT1))
		x = 1
		while x < 6:
			#recive data from server
			data2 = s2.recv(1024)
			#print('MU02:',data2)

			#parsing data
			data1new = data2.decode("utf-8")

			try:
				datet,a,b,ce,d,e,f,g,h,i,j = data1new.split("+")
				#save db
				con = db_connect()
				c = con.cursor()
				#datet = datetime.datetime.now()
				c.execute("INSERT INTO mu04(xtime, B20_Tr_CB_ctrl, B20_Tr_CB_res, B20_Tr_Ld_res, B20_Tr_hv_P_res, B20_Tr_hv_Q_res, B20_Tr_lv_P_res, B20_Tr_lv_Q_res, B20_Tr_tap_ctrl, B20_Tr_tap_mode, B20_Tr_tap_res) VALUES (?,?,?,?,?,?,?,?,?,?,?)",(datet,int(a),int(b),float(ce),float(d),float(e),float(f), float(g), int(h), int(i), int(j)))
				#c.execute("INSERT INTO mu01(xtime, B23_Li_23_24_CB_ctrl) VALUES (?,?)",(datet,int(a)))
				con.commit()
				con.close()
			except Exception:
				print("mu04")
				pass

def serverMU05():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
		s2.connect((MU05, PORT1))
		x = 1
		while x < 6:
			#recive data from server
			data2 = s2.recv(1024)
			#print('MU02:',data2)

			#parsing data
			data1new = data2.decode("utf-8")

			try:
				datet,a,b = data1new.split("+")
				#save db
				con = db_connect()
				c = con.cursor()
				#datet = datetime.datetime.now()
				c.execute("INSERT INTO mu05(xtime, B20_Tr_19_20_CB_ctrl, B20_Tr_19_20_CB_res) VALUES (?,?,?)",(datet,int(a),int(b)))
				#c.execute("INSERT INTO mu01(xtime, B23_Li_23_24_CB_ctrl) VALUES (?,?)",(datet,int(a)))
				con.commit()
				con.close()
			except Exception:
				print("mu05")
				pass


def serverMU06():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
		s2.connect((MU06, PORT1))
		x = 1
		while x < 6:
			#recive data from server
			data2 = s2.recv(1024)

			#parsing data
			data1new = data2.decode("utf-8")

			try:
				datet,a,b,ce,d,e,f,g = data1new.split("+")
				#save db
				con = db_connect()
				c = con.cursor()
				#datet = datetime.datetime.now()
				c.execute("INSERT INTO mu06(xtime, B20_Ld20_CB_ctrl, B20_Ld20_CB_res, B20_Ld20_I_res, B20_Ld20_P_res, B20_Ld20_Q_res, B20_Ld20_V_res, B20_Ld20_f_res) VALUES (?,?,?,?,?,?,?,?)",(datet,int(a),int(b),float(ce),float(d),float(e),float(f),float(g)))
				#c.execute("INSERT INTO mu01(xtime, B23_Li_23_24_CB_ctrl) VALUES (?,?)",(datet,int(a)))
				con.commit()
				con.close()
			except Exception:
				print("mu06")
				pass

def serverMU07():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
		s2.connect((MU07, PORT1))
		x = 1
		while x < 6:
			#recive data from server
			data2 = s2.recv(1024)

			#parsing data
			data1new = data2.decode("utf-8")

			try:
				datet,a,b,ce,d,e = data1new.split("+")
				#save db
				con = db_connect()
				c = con.cursor()
				#datet = datetime.datetime.now()
				c.execute("INSERT INTO mu07(xtime, B20_Tr_CB_ctrl, B20_Tr_CB_res, B20_Tr_V_res, B20_Tr_f_res, B20_Tr_tap) VALUES (?,?,?,?,?,?)",(datet,int(a),int(b),float(ce),float(d),int(e)))
				#c.execute("INSERT INTO mu01(xtime, B23_Li_23_24_CB_ctrl) VALUES (?,?)",(datet,int(a)))
				con.commit()
				con.close()
			except Exception:
				print("mu07")
				pass

def serverMU08():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
		s2.connect((MU08, PORT1))
		x = 1
		while x < 6:
			#recive data from server
			data2 = s2.recv(1024)

			#parsing data
			data1new = data2.decode("utf-8")

			try:
				datet,a,b,ce,d,e,f,g,h,i = data1new.split("+")
				#save db
				con = db_connect()
				c = con.cursor()
				#datet = datetime.datetime.now()
				c.execute("INSERT INTO mu08(xtime, B33_G4_CB_ctrl, B33_G4_CB_res, B33_G4_Ld_res, B33_G4_P_ctrl, B33_G4_P_res, B33_G4_Q_res, B33_G4_V_ctrl, B33_G4_V_res, B33_G4_f_res) VALUES (?,?,?,?,?,?,?,?,?,?)",(datet,int(a),int(b),float(ce),float(d),float(e),float(f),float(g),float(h),float(i)))
				#c.execute("INSERT INTO mu01(xtime, B23_Li_23_24_CB_ctrl) VALUES (?,?)",(datet,int(a)))
				con.commit()
				con.close()
			except Exception:
				print("mu08")
				pass

def serverMU09():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
		s2.connect((MU09, PORT1))
		x = 1
		while x < 6:
			#recive data from server
			data2 = s2.recv(1024)

			#parsing data
			data1new = data2.decode("utf-8")

			try:
				datet,a,b = data1new.split("+")
				#save db
				con = db_connect()
				c = con.cursor()
				#datet = datetime.datetime.now()
				c.execute("INSERT INTO mu09(xtime, B34_Tr_CB_ctrl, B34_Tr_CB_res) VALUES (?,?,?)",(datet,int(a),int(b)))
				#c.execute("INSERT INTO mu01(xtime, B23_Li_23_24_CB_ctrl) VALUES (?,?)",(datet,int(a)))
				con.commit()
				con.close()
			except Exception:
				print("mu09")
				pass

def serverMU10():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
		s2.connect((MU10, PORT1))
		x = 1
		while x < 6:
			#recive data from server
			data2 = s2.recv(1024)

			#parsing data
			data1new = data2.decode("utf-8")

			try:
				datet,a,b,ce,d,e,f,g,h,i = data1new.split("+")
				#save db
				con = db_connect()
				c = con.cursor()
				#datet = datetime.datetime.now()
				c.execute("INSERT INTO mu10(xtime, B34_G5_CB_ctrl, B34_G5_CB_res, B34_G5_Ld_res, B34_G5_P_ctrl, B34_G5_P_res, B34_G5_Q_res, B34_G5_V_ctrl, B34_G5_V_res, B34_G5_f_res) VALUES (?,?,?,?,?,?,?,?,?,?)",(datet,int(a),int(b),float(ce),float(d),float(e),float(f),float(g),float(h),float(i)))
				#c.execute("INSERT INTO mu01(xtime, B23_Li_23_24_CB_ctrl) VALUES (?,?)",(datet,int(a)))
				con.commit()
				con.close()
			except Exception:
				print("mu10")
				pass

# Create two threads as follows
try:
   _thread.start_new_thread( serverMU01, ( ) )
   #_thread.start_new_thread( serverMU02, ( ) )
   _thread.start_new_thread( serverMU03, ( ) )
   _thread.start_new_thread( serverMU04, ( ) )
   _thread.start_new_thread( serverMU05, ( ) )
   #_thread.start_new_thread( serverMU06, ( ) )
   _thread.start_new_thread( serverMU07, ( ) )
   #_thread.start_new_thread( serverMU08, ( ) )
   _thread.start_new_thread( serverMU09, ( ) )
   #_thread.start_new_thread( serverMU10, ( ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass
