import bluetooth
import os
import time
import random

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
	time.sleep(0.1)

client_sock.close()
server_sock.close()

