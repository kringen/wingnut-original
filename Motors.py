import RPi.GPIO as GPIO
import time

class Motor:

    def __init__(self, pin1, pin2, enablePin, freq, direction, dutyCycle, ratio):
        self.pin1 = pin1
        self.pin2 = pin2
        self.enablePin = enablePin
        self.freq = freq
        self.direction = direction
        self.dutyCycle = dutyCycle
        self.ratio = ratio

    def startMotor(self):
        print("Initializing motor GPIO pins:" )
        GPIO.setup(self.pin1, GPIO.OUT)
        GPIO.setup(self.pin2, GPIO.OUT)
        GPIO.setup(self.enablePin, GPIO.OUT)
        print("Setting up Motor PWM at " + str(self.freq) + " Hz")
        self.pwm = GPIO.PWM(self.enablePin, self.freq)
        self.pwm.start(0) # start at 0% duty cycle
    
    def setDirection(self):
        if self.direction == "forward":
            GPIO.output(self.pin2, GPIO.HIGH)
            GPIO.output(self.pin1, GPIO.LOW)
        if self.direction == "reverse":
            GPIO.output(self.pin1, GPIO.HIGH)
            GPIO.output(self.pin2, GPIO.LOW)
        print(self.direction)
        
    def setSpeed(self):
        self.pwm.ChangeDutyCycle(self.dutyCycle)
        print("setting speed to %f" % (self.dutyCycle))
    def motorCleanup(self):
        self.pwm.stop()
      
if __name__ == "__main__":

    GPIO.setmode(GPIO.BOARD)
    
    # 37 = Orange
    # 35 = Yellow 
    # 33 = Green
    # 31 = Blue
    # 29 = Purple
    # 32 = Gray

    leftMotor = Motor(33,35,37,200,"forward",0,1)
    leftMotor.startMotor()

    rightMotor = Motor(31,29,32,200,"forward",0,1)
    rightMotor.startMotor()

    try:
        direction = "forward"
        while (True): 	# infinite loop
            if direction == "forward":
                direction = "reverse"
            else:
                direction = "forward"
            leftMotor.direction = direction
            leftMotor.setDirection()
            rightMotor.direction = direction
            rightMotor.setDirection()
            for dc in range(10,50, 2):
                rightMotor.dutyCycle = dc
                rightMotor.ratio = 1.0
                rightMotor.setSpeed()
                
                leftMotor.dutyCycle = dc
                leftMotor.ratio = 1.0
                leftMotor.setSpeed()
                print("Left Motor Direction: %s, Right Motor Direction: %s, Left Motor Ratio: %f, Right Motor Ratio: %f, Left Motor DC: %f, Right Motor DC: %f" % (leftMotor.direction, rightMotor.direction, leftMotor.ratio, rightMotor.ratio, leftMotor.dutyCycle, rightMotor.dutyCycle))
            
                time.sleep(0.60)
    except:
        pass
    finally:
        leftMotor.motorCleanup()
        rightMotor.motorCleanup()
        GPIO.cleanup()
