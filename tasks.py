import logging

logging.basicConfig(level=logging.WARNING)

def create_task(queue, task_value):
    if queue == "mode":
        set_mode(task_value)
    return True

def set_mode(task_value):
    logging.debug("Setting mode: {}".format(task_value))

def speak(phrase):
    print("Speaking")
