from redis import Redis
from rq import Queue
import logging
from ui import ui
import lgpio

logger = logging.getLogger(__name__)

class Wingnut:
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

        self.diagnostics = {}

    def start_ui(self):
        ui.app.run(host="0.0.0.0",debug=1)

    def get_diagnostics(self):
        ##### SHOULD THIS GO HERE?
        diagnostics = {}
        diagnostics["power_level"] = 100
        diagnostics["temperature"] = 40
        diagnostics["free_memory_mb"] = 500
        diagnostics["free_disk_space"] = 20
        r = Redis()
        r.mset(diagnostics)


if __name__ == "__main__":

    wingnut = Wingnut()
    wingnut.start_ui()
    wingnut.get_diagnostics()
