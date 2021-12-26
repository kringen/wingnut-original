import time
import logging

log = logging.getLogger("task_logger")


def create_task(task_type):
    time.sleep(int(task_type) * 10)
    return True

def set_mode(mode):
    print("Setting mode")

def speak(phrase):
    print("Speaking")
