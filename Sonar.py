import RPi.GPIO as GPIO
import time

class Sonar:
        def __init__(self, triggerPin, echoPin):
                self.triggerPin = triggerPin
                self.echoPin = echoPin
                GPIO.setup(self.triggerPin, GPIO.OUT)
                GPIO.output(self.triggerPin, 0)
                GPIO.setup(self.echoPin, GPIO.IN)

        def getDistance(self):
                # send 10 microsecond high
                GPIO.output(self.triggerPin, 1)
                time.sleep(0.00001)
                GPIO.output(self.triggerPin, 0)

                while GPIO.input(self.echoPin) == 0: # this loop runs until signal received
                        pass
                start = time.time()

                while GPIO.input(self.echoPin) == 1: # received the echo and loop until signal is low
                        pass
                stop = time.time()

                #  Speed of sound is 35000 CM/second...half distance
                distance = (stop - start) * 17000

                return distance

if __name__ == '__main__':
        GPIO.setmode(GPIO.BOARD)

        sonar1 = Sonar(11,13)
        
        time.sleep(0.1)
    
	distance = sonar1.getDistance()
	print(distance)
	
	GPIO.cleanup()
