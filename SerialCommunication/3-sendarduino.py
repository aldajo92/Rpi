import threading
import serial
import time

connected = False
port = '/dev/ttyUSB2'
baud = 9600

serial_port = serial.Serial(port, baud)

def handle_data(data):
        print(data)

def read_from_port(ser):
        while True:
                reading = ser.readline()
                if(reading != ""):
                        handle_data(reading)
                        time.sleep(0.1)

thread = threading.Thread(target=read_from_port, args=(serial_port,))
thread.start()

serial_port.write("a1\r\n")
time.sleep(2)
serial_port.write("a2\r\n")
time.sleep(2)
serial_port.write("b1\r\n")
time.sleep(2)
serial_port.write("b2\r\n")
