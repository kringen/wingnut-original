#!/usr/bin/python3

import sys
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

pin=15 #int(sys.argv[1])
deg=float(sys.argv[1])

duty=1./20.*(deg)+2

GPIO.setup(pin, GPIO.OUT)
pwm=GPIO.PWM(pin, 50)
pwm.start(duty)

time.sleep(.6) #Give it 1/2 second then shut it down. 
pwm.stop()
GPIO.cleanup()
