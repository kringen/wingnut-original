import RPi.GPIO as GPIO
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s %(message)s',)

GPIO.setmode(GPIO.BCM)

# Left motor
leftOne = 18
leftTwo = 23
leftPWMPin = 24
GPIO.setup(leftOne, GPIO.OUT)
GPIO.setup(leftTwo, GPIO.OUT)
GPIO.setup(leftPWMPin, GPIO.OUT)

GPIO.output(leftOne, False)
GPIO.output(leftTwo, False)

pwmLeft = GPIO.PWM(leftPWMPin, 1000) # create pwm at port 12 at 50 Hz
pwmLeft.start(1) # start at 0% duty cycle

# Right motor
rightOne = 22
rightTwo = 27
rightPWMPin = 25
GPIO.setup(rightOne, GPIO.OUT)
GPIO.setup(rightTwo, GPIO.OUT)
GPIO.setup(rightPWMPin, GPIO.OUT)

GPIO.output(rightOne, False)
GPIO.output(rightTwo, False)

pwmRight = GPIO.PWM(rightPWMPin, 1000) # create pwm at port 12 at 50 Hz
pwmRight.start(1) # start at 0% duty cycle

		
def setSpeed(motor, speed):
	if(motor=="left"):
		pwmLeft.ChangeDutyCycle(speed)
	if(motor=="right"):
		pwmRight.ChangeDutyCycle(speed)
	
#def threadTest(q):
#		while True:
#			dc = q.get()
#			logging.debug(dc)

def moveForward(leftSpeed, rightSpeed):
	GPIO.output(leftOne, True)
	GPIO.output(leftTwo, False)
	setSpeed("left", leftSpeed)
	
	GPIO.output(rightOne, True)
	GPIO.output(rightTwo, False)
	setSpeed("right", rightSpeed)
	
	logging.debug("Moving Forward Left=" + str(leftSpeed) + ", Right=" + str(rightSpeed))

def moveBackward(leftSpeed, rightSpeed):
	GPIO.output(leftOne, False)
	GPIO.output(leftTwo, True)
	setSpeed("left", leftSpeed)
	
	GPIO.output(rightOne, False)
	GPIO.output(rightTwo, True)
	setSpeed("right", rightSpeed)
	
def hardRight(leftSpeed, rightSpeed):
	GPIO.output(leftOne, True)
	GPIO.output(leftTwo, False)
	setSpeed("left", leftSpeed)
	
	GPIO.output(rightOne, False)
	GPIO.output(rightTwo, True)
	setSpeed("right", rightSpeed)

def hardLeft(leftSpeed, rightSpeed):
	GPIO.output(leftOne, False)
	GPIO.output(leftTwo, True)
	setSpeed("left", leftSpeed)
	
	GPIO.output(rightOne, True)
	GPIO.output(rightTwo, False)
	setSpeed("right", rightSpeed)
	
def stop():
	GPIO.output(leftOne, False)
	GPIO.output(leftTwo, False)
	setSpeed("left", 1)
	
	GPIO.output(rightOne, False)
	GPIO.output(rightTwo, False)
	setSpeed("right", 1)

	

if __name__ == '__main__':
	try:
		while (1 == 1): 	# infinite loop
			for dc in range(0,101, 5):
				moveForward(dc, dc)
				time.sleep(500.0 / 1000.0)
	except:
		pass
		pwmLeft.stop()
		pwmRight.stop()
		GPIO.cleanup()
