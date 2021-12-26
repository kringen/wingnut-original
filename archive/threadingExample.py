import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

def worker(delay):
    logging.debug('Starting')
    time.sleep(delay)
    logging.debug('Exiting')

#  Start 2 threads manually
t = threading.Thread(name='my_service', target=worker, args=(5,))
w = threading.Thread(name='worker', target=worker, args=(10,))

w.start()
t.start()

#  Start 5 threads using a loop
for i in range(10,15):
    x = threading.Thread(name='worker' + str(i), target=worker, args=(i,))
    x.start()

