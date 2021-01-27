#!/user/bin/env python3
from opcua import Client
from opcua import ua
import socket
import binascii
import _thread
import time
from datetime import datetime


HOST = ''
PORT1 = 991
PORT2 = 992
PORT3 = 993
PORT4 = 994


#OPC ACCESS
url = "opc.tcp://131.180.165.25:8899/freeopcua/server/"
client = Client(url)
client.connect()
print("connected to OPC UA Server")
val1 = client.get_node("ns=2;i=283")
val2 = client.get_node("ns=2;i=284")
val3 = client.get_node("ns=2;i=288")
val4 = client.get_node("ns=2;i=295")
val5 = client.get_node("ns=2;i=285")
val6 = client.get_node("ns=2;i=286")
val7 = client.get_node("ns=2;i=287")
val8 = client.get_node("ns=2;i=289")
val9 = client.get_node("ns=2;i=290")
val10 = client.get_node("ns=2;i=291")
val11 = client.get_node("ns=2;i=292")
val12 = client.get_node("ns=2;i=293")
val13 = client.get_node("ns=2;i=294")


# Define a function for the thread
def serverOne():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
		s1.bind(('',PORT1))
		s1.listen()
		conn1, addr = s1.accept()
		value=0
		with conn1:
			print('Server 1 from:',addr)
			while True:
				a = 1
				value = 2

				try: 
				#Update OPC value
					value1 = val1.get_value()
					value2 = val2.get_value()
					value3 = val3.get_value()
					value4 = val4.get_value()
					value5 = val5.get_value()
					value6 = val6.get_value()
					value7 = val7.get_value()
					value8 = val8.get_value()
					value9 = val9.get_value()
					value10 = val10.get_value()
					value11 = val11.get_value()
					value12 = val12.get_value()
					value13 = val13.get_value()
					dt = datetime.now()

					#covert inetger to string
					#stringd = str(value)

					stringd = str(dt)+"+"+str(value1)+"+"+str(value2)+"+"+str(value3)+"+"+str(value4)+"+"+str(value5)+"+"+str(value6)+"+"+str(value7)+"+"+str(value8)+"+"+str(value9)+"+"+str(value10)+"+"+str(value11)+"+"+str(value12)+"+"+str(value13)

					#convert string to bytes data
					data1 = stringd.encode()

					#send data back to client
					conn1.sendall(data1)

					#print('S1:',data1)
					time.sleep(1)

				except Exception:
						print("One")
						pass

				

# Define a function for the thread
def serverOneCC():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
		s1.bind(('',PORT3))
		s1.listen()
		conn1, addr = s1.accept()
		value=0
		with conn1:
			print('Server 1 from:',addr)
			while True:
				a = 1
				value = 2

				try:
					#Update OPC value
					value1 = val1.get_value()
					value2 = val2.get_value()
					value3 = val3.get_value()
					value4 = val4.get_value()
					value5 = val5.get_value()
					value6 = val6.get_value()
					value7 = val7.get_value()
					value8 = val8.get_value()
					value9 = val9.get_value()
					value10 = val10.get_value()
					value11 = val11.get_value()
					value12 = val12.get_value()
					value13 = val13.get_value()
					dt = datetime.now()

					#covert inetger to string
					#stringd = str(value)

					stringd = str(dt)+"+"+str(value1)+"+"+str(value2)+"+"+str(value3)+"+"+str(value4)+"+"+str(value5)+"+"+str(value6)+"+"+str(value7)+"+"+str(value8)+"+"+str(value9)+"+"+str(value10)+"+"+str(value11)+"+"+str(value12)+"+"+str(value13)


					#convert string to bytes data
					data1 = stringd.encode()

					#send data back to client
					conn1.sendall(data1)

					#print('S1:',data1)
					time.sleep(1)

				except Exception:
						print("OneCC")
						pass


# Define a function for the thread
def serverTwo():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
		s2.bind(('',PORT2))
		s2.listen()
		conn2, addr = s2.accept()
		valueb=0
		with conn2:
			print('Server 2 from:',addr)
			while True:
				b = 1
				value = 2
				data2 = conn2.recv(1024)
				data3 = data2.decode("utf-8")

				try: 
					a,b = data3.split("+")


					value = int(b)
					check = int(a)
					if check == 283:
						val1.set_value(value, ua.VariantType.Int16)
						print('Value 283 set to:',value)
					elif check == 284:
						val2.set_value(value, ua.VariantType.Int16)
						print('Value 284 set to:',value)
					elif check == 288:
						val3.set_value(value, ua.VariantType.Float)
						print('Value 288 set to:',value)
					elif check == 295:
						val4.set_value(value, ua.VariantType.Float)
						print('Value 295 set to:',value)
					elif check == 285:
						val5.set_value(value, ua.VariantType.Float)
						print('Value 285 set to:',value)
					elif check == 286:
						val6.set_value(value, ua.VariantType.Float)
						print('Value 286 set to:',value)
					elif check == 287:
						val7.set_value(value, ua.VariantType.Float)
						print('Value 287 set to:',value)
					elif check == 289:
						val8.set_value(value, ua.VariantType.Float)
						print('Value 289 set to:',value)
					elif check == 290:
						val9.set_value(value, ua.VariantType.Float)
						print('Value 290 set to:',value)
					elif check == 291:
						val10.set_value(value, ua.VariantType.Int16)
						print('Value 291 set to:',value)
					elif check == 292:
						val11.set_value(value, ua.VariantType.Int16)
						print('Value 292 set to:',value)
					elif check == 293:
						val12.set_value(value, ua.VariantType.Int16)
						print('Value 293 set to:',value)
					elif check == 294:
						val13.set_value(value, ua.VariantType.Int16)
						print('Value 294 set to:',value)
					else:
							print(".")

				except Exception:
						print("Two")
						pass

def serverTwoCC():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
		s2.bind(('',PORT4))
		s2.listen()
		conn2, addr = s2.accept()
		valueb=0
		with conn2:
			print('Server 2 from:',addr)
			while True:
				b = 1
				value = 2
				data2 = conn2.recv(1024)
				data3 = data2.decode("utf-8")

				try:
					a,b = data3.split("+")


					value = int(b)
					check = int(a)
					if check == 283:
						val1.set_value(value, ua.VariantType.Int16)
						print('Value 283 set to:',value)
					elif check == 284:
						val2.set_value(value, ua.VariantType.Int16)
						print('Value 284 set to:',value)
					elif check == 288:
						val3.set_value(value, ua.VariantType.Float)
						print('Value 288 set to:',value)
					elif check == 295:
						val4.set_value(value, ua.VariantType.Float)
						print('Value 295 set to:',value)
					elif check == 285:
						val5.set_value(value, ua.VariantType.Float)
						print('Value 285 set to:',value)
					elif check == 286:
						val6.set_value(value, ua.VariantType.Float)
						print('Value 286 set to:',value)
					elif check == 287:
						val7.set_value(value, ua.VariantType.Float)
						print('Value 287 set to:',value)
					elif check == 289:
						val8.set_value(value, ua.VariantType.Float)
						print('Value 289 set to:',value)
					elif check == 290:
						val9.set_value(value, ua.VariantType.Float)
						print('Value 290 set to:',value)
					elif check == 291:
						val10.set_value(value, ua.VariantType.Int16)
						print('Value 291 set to:',value)
					elif check == 292:
						val11.set_value(value, ua.VariantType.Int16)
						print('Value 292 set to:',value)
					elif check == 293:
						val12.set_value(value, ua.VariantType.Int16)
						print('Value 293 set to:',value)
					elif check == 294:
						val13.set_value(value, ua.VariantType.Int16)
						print('Value 294 set to:',value)
					else:
							print(".")

				except Exception:
						print("TwoCC")
						pass




# Create two threads as follows
try:
   _thread.start_new_thread( serverOne, ( ) )
   _thread.start_new_thread( serverOneCC, ( ) )
   _thread.start_new_thread( serverTwo, ( ) )
   _thread.start_new_thread( serverTwoCC, ( ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass