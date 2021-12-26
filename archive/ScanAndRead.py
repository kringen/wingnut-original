import time
import RPi.GPIO as GPIO
from Servo import Servo
from Sonar import Sonar



if __name__ == "__main__":
    GPIO.setmode(GPIO.BOARD)

    sonar1 = Sonar(11,13)
    servo1 = Servo(15, 50, 17)
    
    # move to 45 degrees
    servo1.move(45)
    time.sleep(1)
    # take a reading
    distance45 = sonar1.getDistance()
    print(distance45)
    
    # move to 45 degrees
    servo1.move(90)
    time.sleep(1)
    # take a reading
    distance90 = sonar1.getDistance()
    print(distance90)

    # move to 45 degrees
    servo1.move(135)
    time.sleep(1)
    # take a reading
    distance135 = sonar1.getDistance()
    print(distance135)
    
    # return to facing front
    servo1.move(90)
    time.sleep(1)
    servo1.stop()
    
    GPIO.cleanup()
    

