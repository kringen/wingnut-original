#!/usr/bin/python3

from queue import Queue
from threading import Thread
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s %(message)s',)

# A thread that produces data
#def producer(out_q):
#    while True:
#        # Produce some data
#        data = "Test Data"
#        out_q.put(data)


# A thread that consumes data
def consumer(in_q):
    while True:
        # Get some data
        data = in_q.get()
        # Process the data
        logging.debug(data)

# Create the shared queue and launch both threads
q = Queue()
t1 = Thread(name="motor thread", target=consumer, args=(q,))
#t2 = Thread(target=producer, args=(q,))

t1.start()
#t2.start()

while True: 	# infinite loop
		for dc in range(0,101, 5):
			q.put(dc)
			#print(dc)
			time.sleep(500.0 / 1000.0)
