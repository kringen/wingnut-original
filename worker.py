import redis
from rq import Queue, Connection, Worker

def run_worker():
    redis_url = "redis://localhost:6379"
    redis_connection = redis.from_url(redis_url)
    with Connection(redis_connection):
        worker = Worker(["default","mode"])
        worker.work()

if __name__ == "__main__":
    run_worker()
