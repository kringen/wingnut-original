import logging

logging.basicConfig(filename='example.log', level=logging.DEBUG)

def create_task(queue, task_value):
    if queue == "mode":
        set_mode(task_value)
    return True

def set_mode(task_value):
    print("Setting mode: {}".format(task_value))
    logging.debug("Setting mode: {}".format(task_value))

def speak(phrase):
    print("Speaking")
