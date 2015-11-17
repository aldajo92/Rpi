import smbus
import math

import bluetooth
import os
import time
import random

os.system("hciconfig hci0 piscan")
server_sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
port = 1
server_sock.bind(("",port))
server_sock.listen(1)

client_sock,address = server_sock.accept()
print("Accepted connection from ", address)

# Power management registers
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

bus = smbus.SMBus(1) # or bus = smbus.SMBus(1) for Revision 2 boards
address = 0x68       # This is the address value read via the i2cdetect command

def read_byte(adr):
	return bus.read_byte_data(address, adr)

def read_word(adr):
	high = bus.read_byte_data(address, adr)
	low = bus.read_byte_data(address, adr+1)
	val = (high << 8) + low
	return val

def read_word_2c(adr):
	val = read_word(adr)
	if (val >= 0x8000):
		return -((65535 - val) + 1)
	else:
		return val

def dist(a,b):
	return math.sqrt((a*a)+(b*b))

def get_y_rotation(x,y,z):
	radians = math.atan2(x, dist(y,z))
	return -math.degrees(radians)

def get_x_rotation(x,y,z):
	radians = math.atan2(y, dist(x,z))
	return math.degrees(radians)

def get_data():

	accel_xout = read_word_2c(0x3b)
	accel_yout = read_word_2c(0x3d)
	accel_zout = read_word_2c(0x3f)

	accel_xout_scaled = accel_xout / 16384.0
	accel_yout_scaled = accel_yout / 16384.0
	accel_zout_scaled = accel_zout / 16384.0

	return str(get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled))+"-"+str(get_y_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled))

s = ""

# Now wake the 6050 up as it starts in sleep mode
while True:
	bus.write_byte_data(address, power_mgmt_1, 0)
	s = "R-"+get_data()+"-0-A"
	client_sock.send(s)
	#print get_data()
	time.sleep(0.5)

client_sock.close()
server_sock.close()

