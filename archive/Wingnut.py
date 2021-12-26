import RPi.GPIO as GPIO
import time
import Motors
import Servo
import Sonar

class WingNut:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        self.servoPin = 15
        self.leftMotorPin1 = 33
        self.leftMotorPin2 = 35
        self.leftMotorEnablePin = 37
        self.rightMotorPin1 = 31
        self.rightMotorPin2 = 29
        self.rightMotorEnablePin = 32
        self.sonarTriggerPin = 11
        self.sonarEchoPin = 13

        self.distanceCenter = 0
        self.distanceLeft = 0
        self.distanceRight = 0
        self.closestObject = ""
        self.closestObjectDistance = 0

    def initializeServo(self):
        self.servo1 = Servo.Servo(self.servoPin, 50, 17) # pin 15, 50 hz, -2 deg offset

    def initializeMotors(self):
        # Motors
        self.leftMotor = Motors.Motor(self.leftMotorPin1,self.leftMotorPin2,self.leftMotorEnablePin,200,"forward",0,1)
        self.leftMotor.startMotor()
        self.leftMotor.setDirection()
        self.leftMotor.setSpeed()
        self.rightMotor = Motors.Motor(self.rightMotorPin1,self.rightMotorPin2,self.rightMotorEnablePin,200,"forward",0,1)
        self.rightMotor.startMotor()
        self.rightMotor.setDirection()
        self.rightMotor.setSpeed()

    def initializeSonar(self):
        self.sonar1 = Sonar.Sonar(self.sonarTriggerPin, self.sonarEchoPin)

    def regroup(self):
        self.servo1.move(90)
        time.sleep(1)
        self.servo1.stop()

    def moveForward(self, speed):
        self.rightMotor.dutyCycle = speed
        self.rightMotor.ratio = 1
        self.rightMotor.setSpeed()
        self.leftMotor.dutyCycle = speed
        self.leftMotor.ratio = .5
        self.leftMotor.setSpeed()

    def stop(self):
        self.moveForward(0)
        self.leftMotor.motorCleanup()
        self.rightMotor.motorCleanup()
        
    def scanAndRead(self):
        # move to 45 degrees
        self.servo1.move(45)
        time.sleep(1)
        # take a reading
        self.distanceLeft = self.sonar1.getDistance()
        print("Left: " + str(self.distanceLeft))
        
        # move to 45 degrees
        self.servo1.move(90)
        time.sleep(1)
        # take a reading
        self.distanceCenter = self.sonar1.getDistance()
        print("Center: " + str(self.distanceCenter))

        # move to 45 degrees
        self.servo1.move(135)
        time.sleep(1)
        # take a reading
        self.distanceRight = self.sonar1.getDistance()
        print("Right: " + str(self.distanceRight))

        if self.distanceRight < self.distanceCenter and self.distanceRight < self.distanceLeft:
            self.closestObject = "right"
            self.closestObjectDistance = self.distanceRight
        elif self.distanceLeft < self.distanceCenter and self.distanceLeft < self.distanceRight:
            self.closestObject = "left"
            self.closestObjectDistance = self.distanceLeft
        else:
            self.closestObject = "center"
            self.closestObjectDistance = self.distanceCenter

        print("Closest Object: " + self.closestObject)
        print(self.closestObjectDistance) 
       
        # return to facing front
        self.servo1.move(90)
        

    def cleanup(self):
        wingnut.leftMotor.motorCleanup()
        wingnut.rightMotor.motorCleanup()
        GPIO.cleanup()

if __name__ == "__main__":

    wingnut = WingNut()
    wingnut.initializeServo()
    wingnut.initializeMotors()
    wingnut.initializeSonar()
    wingnut.regroup()
    wingnut.moveForward(50)
    time.sleep(3)
    wingnut.stop()
    try:
        while True:
            #wingnut.scanAndRead() 
            pass
    except KeyboardInterrupt:
        print ("parent received control-c")
    except:
        pass
        print("Other error occurred.")
    finally:
        wingnut.cleanup()
            

        
