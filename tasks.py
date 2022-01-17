import logging
import polly
import redis
import psutil

logging.basicConfig(level=logging.WARNING)

def create_task(queue, qualifier):
    if queue == "mode":
        set_mode(qualifier)
    if queue == "status":
        set_status()
        get_status(qualifier)
    return True

def set_mode(qualifier):
    logging.debug("Setting mode: {}".format(qualifier))
    speak("Setting mode. {}".format(qualifier))

def set_status():
    r = redis.Redis()

    diagnostics = {}
    diagnostics["power_level"] = 100
    diagnostics["temperature"] = psutil.sensors_temperatures()['coretemp'][0].current
    diagnostics["free_memory_mb"] = round(psutil.virtual_memory().free / 1024 / 1024,0)
    diagnostics["cpu_percent"] = psutil.cpu_percent()
    diagnostics["free_disk_space"] = round(psutil.disk_usage('/').free / 1024 / 1024 / 1024,0)
    r = redis.Redis()
    r.mset(diagnostics)


def get_status(qualifier):
    r = redis.Redis()

    power_level = r.get("power_level").decode("utf-8")
    temperature = r.get("temperature").decode("utf-8")
    free_memory_mb = r.get("free_memory_mb").decode("utf-8")
    cpu_percent = r.get("cpu_percent").decode("utf-8")
    free_disk_space = r.get("free_disk_space").decode("utf-8")
    phrase = """
    All systems nominal.
    Power level is at {} %.
    CPU temperature is {} degrees Celcius.
    CPU load is {} %.
    Free memory is {} megabytes.
    Free disk space is {} gigabytes.
    """.format(power_level,temperature, cpu_percent, free_memory_mb, free_disk_space)
    polly.speak(phrase, "Joanna")

def speak(phrase):
    polly.speak(phrase, "Joanna")