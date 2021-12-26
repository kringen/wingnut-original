import RPi.GPIO as GPIO
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s %(message)s',)

GPIO.setmode(GPIO.BCM)

TRIG = 7
ECHO = 12

GPIO.setup(TRIG, GPIO.OUT)
GPIO.output(TRIG, 0)

GPIO.setup(ECHO, GPIO.IN)

time.sleep(0.1)

def getDistance():
	logging.debug("Starting Measurement...")

	# send 10 microsecond high
	GPIO.output(TRIG, 1)
	time.sleep(0.00001)
	GPIO.output(TRIG, 0)

	while GPIO.input(ECHO) == 0: # this loop runs until signal received
		pass
	start = time.time()

	while GPIO.input(ECHO) == 1: # received the echo and loop until signal is low
		pass
	stop = time.time()

	distance = (stop - start) * 17000
	logging.debug(distance)
	return distance

if __name__ == '__main__':
	getDistance()
	GPIO.cleanup()
