#!/usr/bin/python

import smbus
import time
bus = smbus.SMBus(1)
address = 0x04

def write(value):
	bus.write_byte(address,value)
	return -1

def read():
	temp = bus.read_byte(address)
	return temp

write(1)
i = 0
while i < 8:
	try:
		returnValue = read()
		i += 1
		print(returnValue)
	except IOError as e:
		print (e)
	except KeyboardInterrupt:
		print ("Bye!")
		exit()
