from head import Head
import time
from adafruit_servokit import ServoKit

def survey(head, angle_increment, time_increment):
   start_angle = 0
   end_angle = 180
   angle = start_angle
   while head.angle < end_angle:
      head.turn(angle)
      time.sleep(time_increment)
      angle += angle_increment
   head.return_home()

def head_return(head, angle):
   head.turn(angle)

if __name__ == "__main__":
   kit = ServoKit(channels=16)

   head_channel = kit.servo[0]

   head = Head(head_channel, 90)

   survey(head, 5, 0.5)
