#!/bin/bash

# Based on multi-process image:
# https://docs.docker.com/config/containers/multi-service_container/
  
# Start the Redis Server
/usr/bin/redis-server &

# Start a worker
python3 worker.py &

# Start the web server
python3 webapp.py &

# Start the primary process
python3 main.py
  