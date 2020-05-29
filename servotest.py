import time
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)

angle = 0

while angle < 170:
	kit.servo[0].angle = angle
	time.sleep(.5)
	angle += 5

