import serial
line = [];

def comConnect():
	try:
		port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=0)
		print("Connected to: " + port.portstr)
	except:
		print("Could not connect to: " + port.portstr)
def comReceive():
	while True:
		for c in port.read():
			line.append(c)
			if c == '\n':
				print("Line: " + line)
				line = []
				break
def comClose():
	port.close()

if __name__ == '__main__':
	try:
		comConnect()
		comReceive()
	except:
		pass
