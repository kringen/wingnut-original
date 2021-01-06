#!/usr/bin/python3

import RPi.GPIO as GPIO
import threading
import queue
import time
import distance, motors, speak

gettingCloseSpoken = False
turningAroundSpoken = False

def calculateManeuvers(objDist):
	global gettingCloseSpoken
	global turningAroundSpoken
	
	if(objDist < 10): #Turn around
			speedLeft = 25
			speedRight = 25
			if(turningAroundSpoken == False):
				t1 = threading.Thread(target=speak.SpeechFromText, args=("Object detected.  Scanning",))
				t1.start()
				turningAroundSpoken = True
			else:
				turningAroundSpoken = False
			motors.hardLeft(speedLeft, speedRight)
	else:
		motors.moveForward(objDist, objDist)
	
	


if __name__ == '__main__':
	#try:
		#motorSpeed = queue.Queue()
		#motorDirection = queue.Queue()
		#motor_thread = threading.Thread(name="motor_thread", target=motors.threadTest, args=(motorSpeed,))
		#direction_thread = threading.Thread(name="direction_thread", target=motors.threadTest2, args=(motorDirection,))
		#motor_thread.start()
		#direction_thread.start()
		#print(threading.activeCount())
		while True: 	# infinite loop
			#objDist = distance.getDistance()
			for objDist in range(0,101, 5):
				time.sleep(500.0 / 1000.0)
				calculateManeuvers(objDist)
			#motorSpeed.put(speed)


	#except:
	#	print("Exiting")
	#	pass
	#	GPIO.cleanup()
