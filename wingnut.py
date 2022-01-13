import multiprocessing
from redis import Redis
from rq import Queue, Connection, Worker
import logging
import lgpio
import yaml
import os


logging.basicConfig(level=logging.DEBUG)
cwd = os.path.dirname(__file__)
config_file = os.path.join(cwd,"wingnut.yaml")

class Wingnut:
    def __init__(self):
        with open(config_file, "r") as configfile:
            self.config = yaml.safe_load(configfile)
        self.worker_count = self.config["worker"]["count"]
        self.worker_queues = self.config["worker"]["queues"]
        self.servoPin = self.config["configuration"]["servoPin"]
        self.leftMotorPin1 = self.config["configuration"]["leftMotorPin1"]
        self.leftMotorPin2 = self.config["configuration"]["leftMotorPin2"]
        self.leftMotorEnablePin = self.config["configuration"]["leftMotorEnablePin"]
        self.rightMotorPin1 = self.config["configuration"]["rightMotorPin1"]
        self.rightMotorPin2 = self.config["configuration"]["rightMotorPin2"]
        self.rightMotorEnablePin = self.config["configuration"]["rightMotorEnablePin"]
        self.sonarTriggerPin = self.config["configuration"]["sonarTriggerPin"]
        self.sonarEchoPin = self.config["configuration"]["sonarEchoPin"]

        self.distanceCenter = 0
        self.distanceLeft = 0
        self.distanceRight = 0
        self.closestObject = ""
        self.closestObjectDistance = 0

        self.diagnostics = {}

        self.redis_url = self.config["configuration"]["redis_url"]
        self.redis_connection = Redis.from_url(self.redis_url)

    def start_workers(self):
        for i in range(self.worker_count):
            # Listen for tasks
            with Connection(self.redis_connection):
                worker = Worker(self.worker_queues)
                multiprocessing.Process(target=worker.work).start()

    def set_diagnostics(self):
        ##### SHOULD THIS GO HERE?
        ### NO - maybe move it to its own service?
        diagnostics = {}
        diagnostics["power_level"] = 100
        diagnostics["temperature"] = 40
        diagnostics["free_memory_mb"] = 500
        diagnostics["free_disk_space"] = 20
        r = Redis()
        r.mset(diagnostics)


if __name__ == "__main__":
    wingnut = Wingnut()
    wingnut.set_diagnostics()
    wingnut.start_workers()
    #wingnut.start_ui()
    #wingnut.get_diagnostics()
