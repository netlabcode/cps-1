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


def serverXMUCC():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sx1:
		sx1.connect((MU01, PORT2))

		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sx2:
			sx2.connect((MU02, PORT2))

			with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sx3:
				sx3.connect((MU03, PORT2))

				with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sx4:
					sx4.connect((MU04, PORT2))

					with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sx5:
						sx5.connect((MU05, PORT2))

						with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sx6:
							sx6.connect((MU06, PORT2))

							with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sx7:
								sx7.connect((MU07, PORT2))

								with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sx8:
									sx8.connect((MU08, PORT2))

									with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sx9:
										sx9.connect((MU09, PORT2))

										with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sx10:
											sx10.connect((MU10, PORT2))

											bx = 1
											value2x=0
											while bx < 6:
												#covert inetger to string

												print("Format: mu01_id+value")
												stringx = str(input("Command entry: "))
												print(stringx)
												part1,part2 = stringx.split("_")
	

												if 'mu01' in stringx:
													part1,part2 = stringx.split("_")
													part2x = part2.encode()
													print(part2x)
													sx1.sendall(part2x)
												elif 'mu02' in stringx:
													part1,part2 = stringx.split("_")
													print(part2)
													part2x = part2.encode()
													sx2.sendall(part2x)
												elif 'mu03' in stringx:
													part1,part2 = stringx.split("_")
													print(part2)
													part2x = part2.encode()
													sx3.sendall(part2x)
												elif 'mu04' in stringx:
													part1,part2 = stringx.split("_")
													print(part2)
													part2x = part2.encode()
													sx4.sendall(part2x)
												elif 'mu05' in stringx:
													part1,part2 = stringx.split("_")
													print(part2)
													part2x = part2.encode()
													sx5.sendall(part2x)
												elif 'mu06' in stringx:
													part1,part2 = stringx.split("_")
													print(part2)
													part2x = part2.encode()
													sx6.sendall(part2x)
												elif 'mu07' in stringx:
													part1,part2 = stringx.split("_")
													print(part2)
													part2x = part2.encode()
													sx7.sendall(part2x)
												elif 'mu08' in stringx:
													part1,part2 = stringx.split("_")
													print(part2)
													part2x = part2.encode()
													sx8.sendall(part2x)
												elif 'mu09' in stringx:
													part1,part2 = stringx.split("_")
													print(part2)
													part2x = part2.encode()
													sx9.sendall(part2x)
												elif 'mu10' in stringx:
													part1,part2 = stringx.split("_")
													print(part2)
													part2x = part2.encode()
													sx10.sendall(part2x)
												else:
													print(".")

												time.sleep(1)
												#sx2.close()
												


# Create two threads as follows
try:
   _thread.start_new_thread( serverXMUCC, ( ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass
