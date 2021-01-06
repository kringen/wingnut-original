import sys
import time
import RPi.GPIO as GPIO

class Servo:
    def __init__(self, servoPin, dutyCycle, offset):
        self.servoPin = servoPin
        self.dutyCycle = dutyCycle
        self.offset = offset
        GPIO.setup(self.servoPin, GPIO.OUT)
        self.servoPwm = GPIO.PWM(self.servoPin, self.dutyCycle)
        
    def move(self, deg):
        self.duty=1./20.*(deg + self.offset)+2
        self.servoPwm.start(self.duty)

    def stop(self):
        self.servoPwm.stop()

if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)

    servo1 = Servo(15, 50, 17) # pin 15, 50 hz, -2 deg offset
    
    deg=float(sys.argv[1])

    servo1.move(deg)
    
    time.sleep(.6) #Give it 1/2 second then shut it down.

    servo1.stop()
    
    GPIO.cleanup()
