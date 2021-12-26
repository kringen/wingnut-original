class Head:
   def __init__(self, channel, angle):
      self.angle = angle
      self.home_angle = angle
      self.channel = channel

   def turn(self, angle):
      self.angle = angle
      print("head angle: {}".format(self.angle))
      self.channel.angle = angle

   def return_home(self):
      self.channel.angle = self.home_angle
