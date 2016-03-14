import threading
import serial
import time

connected = False
port = '/dev/ttyUSB3'
baud = 9600

serial_port = serial.Serial(port, baud)

def handle_data(data):
	string = data.split('-')
        print(data)
	print(string)

def read_from_port(ser):
        while True:
                reading = ser.readline()
                if(reading != ""):
                        handle_data(reading)
                        time.sleep(0.1)

thread = threading.Thread(target=read_from_port, args=(serial_port,))
thread.start()

time.sleep(2)
while(True):
	serial_port.write("request0003 14\r")
	serial_port.write("request0003 14\r")	
	time.sleep(0.1)
	serial_port.write("request0004 14\r")
	serial_port.write("request0004 14\r")
	time.sleep(0.1)
