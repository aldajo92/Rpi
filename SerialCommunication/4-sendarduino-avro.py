import threading
import serial
import time
import io
import avro.schema
import avro.io

myid = "Rpi1"

connected = False
port = '/dev/ttyUSB2'
baud = 9600

schema_path = "RuleMessage.avsc"
schema = avro.schema.parse(open(schema_path).read())
serial_port = serial.Serial(port, baud)

def generatemessage(station, model, iodata, value, connection):
    writer = avro.io.DatumWriter(schema)
    bytes_writer = io.BytesIO()
    encoder = avro.io.BinaryEncoder(bytes_writer)
    writer.write(
        {
            "station": station,
            "model": model,
            "io": iodata,
            "timestamp": int(round(time.time() * 1000)),
            "value": value,
            "connection": connection
        },
        encoder
    )
    raw_bytes = bytes_writer.getvalue()
    return raw_bytes

def handle_data(data):
	var = data.split('-')
	##bytesArray = generatemessage("ex1", "md1", 12, 2.3, True)
	##	(String)arduinoID	(int)pinNumber	(double)pinData
	bytesArray = generatemessage(myid, var[0], var[1], var[2], True)
	print(bytesArray)
    print(data)

def read_from_port(ser):
        while True:
                reading = ser.readline()
                if(reading != ""):
                    handle_data(reading)
                    time.sleep(0.1)

thread = threading.Thread(target=read_from_port, args=(serial_port,))
thread.start()

serial_port.write("actionroof on*13\r")
time.sleep(2)
serial_port.write("actionroof on*13\r")
time.sleep(2)
serial_port.write("requestroof 14\r")
time.sleep(2)
serial_port.write("requestroof 14\r")
