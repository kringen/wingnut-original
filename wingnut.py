from redis import Redis
from rq import Queue
import logging
from api import api
import lgpio

logger = logging.getLogger(__name__)

class WingNut:
    def __init__(self):
        self.log = logger
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

    def start_api(self):
        api.app.run(host="0.0.0.0",debug=1)

if __name__ == "__main__":

    wingnut = WingNut()
    wingnut.start_api()
