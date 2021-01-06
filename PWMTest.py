import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 1000) # create pwm at port 12 at 50 Hz
p.start(1) # start at 0% duty cycle


def pwmTest():
	global direction
	for dc in range(0,101, 5):
		p.ChangeDutyCycle(dc)
		print dc
		time.sleep(500.0 / 1000.0)
	for dc in range(100, -1, -5):
		p.ChangeDutyCycle(dc)
		print dc
		time.sleep(500.0 / 1000.0)

try:
	while (1 == 1): 	# infinite loop
		pwmTest()
except:
	pass
p.stop()
GPIO.cleanup()