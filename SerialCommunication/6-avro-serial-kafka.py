import threading
import serial
import time

from kafka import *
import io
import avro.schema
import avro.datafile
import avro.io
import sys

myid = "Rpi1"

connected = False
port = '/dev/ttyUSB2'
baud = 9600

serial_port = serial.Serial(port, baud)

kafka_client = KafkaClient('52.2.239.144:9092')
producer = KeyedProducer(kafka_client)
schema_path = "RuleMessage.avsc"
schema = avro.schema.parse(open(schema_path).read())

def message_serializer(station, model, iodata, value, connection):
    raw_bytes = None
    try:
        writer = avro.io.DatumWriter(schema)
        bytes_writer = io.BytesIO()
        encoder = avro.io.BinaryEncoder(bytes_writer)
        writer.write({
            "station": station,
            "model": model,
            "io": iodata,
            "timestamp": int(round(time.time() * 1000)),
            "value": value,
            "connection": connection
        },
            encoder)
        raw_bytes = bytes_writer.getvalue()
    except:
        print("Error serializer data", sys.exc_info()[0])
    return raw_bytes


def send_message_producer(topic, raw_bytes, station):
    try:
        producer.send_messages(topic, station, raw_bytes)
    except:
        print("Error send message kafka", sys.exc_info()[0])

def handle_data(data):
        string = data.split('-')

        topic = "events"
	#messageToSend = message_serializer("12", "32", "e", 1.3, True)
	messageToSend = message_serializer(myid, string[0], string[1], float(string[2]), True)
	raw_bytes = messageToSend
	print data
	print(raw_bytes)
	if raw_bytes is not None:
    		send_message_producer(topic, raw_bytes, "idestacion")

def read_from_port(ser):
        while True:
                reading = ser.readline()
                if(reading != ""):
                        handle_data(reading)
                        time.sleep(0.1)

thread = threading.Thread(target=read_from_port, args=(serial_port,))
thread.start()



time.sleep(4)
serial_port.write("request0002 14\r")
