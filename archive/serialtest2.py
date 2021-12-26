import serial

port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=0)

print("Connected to: " + port.portstr)

line = []

while True:
	for c in port.read():
		line.append(c)
		if c == '\n':
			print("Line: " + line)
			line = []
			break
port.close()
