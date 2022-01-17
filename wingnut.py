import multiprocessing
from redis import Redis
from rq import Queue, Connection, Worker
import logging
import lgpio
import yaml
import os


logging.basicConfig(level=logging.WARNING)
cwd = os.path.dirname(__file__)
config_file = os.path.join(cwd,"wingnut.yaml")

class Wingnut:
    def __init__(self):
        with open(config_file, "r") as configfile:
            self.config = yaml.safe_load(configfile)
        self.worker_count = self.config["worker"]["count"]
        self.worker_queues = self.config["worker"]["queues"]
        self.servoPin = self.config["configuration"]["gpio_pins"]["servoPin"]
        self.leftMotorPin1 = self.config["configuration"]["gpio_pins"]["leftMotorPin1"]
        self.leftMotorPin2 = self.config["configuration"]["gpio_pins"]["leftMotorPin2"]
        self.leftMotorEnablePin = self.config["configuration"]["gpio_pins"]["leftMotorEnablePin"]
        self.rightMotorPin1 = self.config["configuration"]["gpio_pins"]["rightMotorPin1"]
        self.rightMotorPin2 = self.config["configuration"]["gpio_pins"]["rightMotorPin2"]
        self.rightMotorEnablePin = self.config["configuration"]["gpio_pins"]["rightMotorEnablePin"]
        self.sonarTriggerPin = self.config["configuration"]["gpio_pins"]["sonarTriggerPin"]
        self.sonarEchoPin = self.config["configuration"]["gpio_pins"]["sonarEchoPin"]

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

if __name__ == "__main__":
    wingnut = Wingnut()
    wingnut.start_workers()
