import serial

port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=0)
receivedString = []

while True:
	rcv = port.read(1)
	if len(rcv) > 0:
		port.write("\r\nYou sent: " + repr(rcv))
		print rcv

