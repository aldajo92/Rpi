import bluetooth
import os
import time
import random
import smbus
import math


os.system("hciconfig hci0 piscan")
#create a socket on bluetooth
#RFCOMM is one of several protocols bluetooth can use
server_sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)

#choose a port number, must be same on client and server, 1 is fine
port = 1
#bind our socket to this port, the "" indicates we are happy to connect
#on any available bluetooth adapter
server_sock.bind(("",port))
#listen for any incoming connections
server_sock.listen(1)

#accept connections and create the client socket
client_sock,address = server_sock.accept()
print("Accepted connection from ", address)

a1 = 0
a2 = 0
a3 = 0
a = 300
b = 650
s = ""

while True:
        a1 = random.randint(a, b)
        a2 = random.randint(a, b)
        a3 = random.randint(a, b)
        s = "R-"+str(a1)+"-"+str(a2)+"-"+str(a3)+"-A\n"
        client_sock.send(s)
        time.sleep(1)

client_sock.close()
server_sock.close()


# Power management registers
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

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

bus = smbus.SMBus(1) # or bus = smbus.SMBus(1) for Revision 2 boards
address = 0x68       # This is the address value read via the i2cdetect command

# Now wake the 6050 up as it starts in sleep mode
bus.write_byte_data(address, power_mgmt_1, 0)


