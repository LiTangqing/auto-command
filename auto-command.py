import time, threading
import serial, io
import csv
from serial.tools.list_ports import comports as listports

# get keyboard input
print("Input information to configure serial port.")

recur_period = int(raw_input(">> recuring period: (/s) "))
ser_port = raw_input(">> serial port: ")
ser_port = 'COM' + ser_port
baud_rate = 57600
data_len = 8
stop_bit_len = 1
test_span = int(raw_input(">> test span: (/s) "))

ser = serial.Serial(port=ser_port,
				baudrate=baud_rate,
				bytesize=data_len,
				stopbits=stop_bit_len,
				timeout=5)
if ser.isOpen():
	ser.reset_input_buffer()
	ser.reset_output_buffer()
	print (ser_port + " is open.")
	if input == 'exit':
		print("bye-bye")
		ser.close()
		exit()
	else:
		print("system writing..")
		ser.write("+++")
		print("system reading..")
		out = ser.read(size = 2)
		ser.reset_input_buffer()
		ser.reset_output_buffer()
		print ("ok postition returns: " + out)
		if out != 'OK':
			print("no OK received, closing")
			time.sleep(0.1)
			ser.close()
			exit()
		else:
			cmd = raw_input(">> command: ")+"\r\n"
			with open('result'+str(time.time())+'.csv','wb') as file:
								a = csv.writer(file,delimiter = ',')
								data = []
								if test_span != 0:  #repeat within test_span
										curr_time = int(time.time())
										termn = int(time.time()) + test_span
										while curr_time< termn:
												ser.write(cmd)
												ser.readline()[:-2]
												line = ser.readline()[:-2]
												
												print(line)
												ser.reset_output_buffer()
												time.sleep(recur_period)
												data.append(line.split())
												curr_time = time.time()
										a.writerows(data)
										
										ser.reset_input_buffer()
										ser.reset_output_buffer()
										ser.close()
										print(data)
										print("result collection finished")
								 
					
					
			
		 


