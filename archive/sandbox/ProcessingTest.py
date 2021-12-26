import multiprocessing
from multiprocessing import Process, current_process, Queue
import time
import logging

class Worker:
    def __init__(self, queue):
        self.queue = queue

    def initiate(self):
        while True:
            data = self.queue.get()
            processed = data * 2
            print "Processed %d in %s" % (processed, current_process().name)

if __name__ == "__main__":

    try:
        motorQueue = Queue()

        data = [44,1,5,3,5,1,5,54,1,51,6,5,8]

        multiprocessing.log_to_stderr()
        logger = multiprocessing.get_logger()
        logger.setLevel(logging.INFO)

        motors = Worker(motorQueue)

        process_motors = Process(target=motors.initiate, name="motors thread", args=())
        process_motors.start()

        for item in data:
            motorQueue.put(item)
            time.sleep(2)
        while True:
            pass
    except KeyboardInterrupt:
        print "parent received control-c"
        process_motors.terminate()
            

        
