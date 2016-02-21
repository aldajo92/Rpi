import time
import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)

ser.write('a1\n')
time.sleep(0.1)
print ser.readline()

time.sleep(2)

ser.write('a2\n')
time.sleep(0.1)
print ser.readline()

time.sleep(2)

ser.write('b1\n')
time.sleep(0.1)
print ser.readline()

ser.write('b2\n')
time.sleep(0.1)
print ser.readline()
