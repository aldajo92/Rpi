import threading
import serial
import time

connected = False
port = '/dev/ttyUSB2'
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
serial_port.write("request0002 14\r")
