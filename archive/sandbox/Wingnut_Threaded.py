import RPi.GPIO as GPIO
import multiprocessing
from multiprocessing import Process, current_process, Queue
from flask import Flask, Response, request, json, render_template
import time
import logging

import Motors


app = Flask(__name__)

# Default End Point
@app.route('/', methods = ['GET'])
def api_root():
    index_data = {
                "title" : "Wingnut API",
                "sensorReading":{
					"deviceID":"5d681c54e66ff4a5654e55c6d5a5b54",
					"metricTypeID":6,
					"uomID":4,
					"actual":{"y":18,"p":17.50,"r":120},
					"setPoints":{"y":25,"p":45,"r":10}
				 },
		"trainingReading":{
					"deviceID":"5d681c54e66ff4a5654e55c6d5a5b54",
					"metricTypeID":6,
					"uomID":4,
					"currentPostureID":2,
					"actual":{"y":18,"p":17.50,"r":120},
					"setPoints":{"y":25,"p":45,"r":100}
				 }
        }

    try:
        print(request.headers)
        return render_template('index.html', data = index_data)
    except:
        return "sorry, error"
    
# End point for controlling the motors

@app.route('/MotorController',  methods = ['POST'])
def post_motorData():
    global motorQueue
    
    if request.headers['Content-Type'] == 'application/json':
        # Populate variables from json object
        motorData = json.dumps(request.json)
        motorQueue.put(motorData)
        return "Setting motors: " + motorData
    else:
        return "415 Unsupported Media Type"


class MotorController:
    def __init__(self, queue):
        self.queue = queue

    def listen(self):
        while True:
            data = json.loads(self.queue.get())
            print("############################")
            print(data)
            leftMotorDirection = data["leftMotorDirection"]
            rightMotorDirection = data["rightMotorDirection"]
            leftMotorSpeed = data["leftMotorSpeed"]
            rightMotorSpeed = data["rightMotorSpeed"]

            leftMotor.direction = leftMotorDirection
            leftMotor.setDirection()
            leftMotor.dutyCycle = leftMotorSpeed
            leftMotor.setSpeed()

            rightMotor.direction = rightMotorDirection
            rightMotor.setDirection()
            rightMotor.dutyCycle = rightMotorSpeed
            rightMotor.setSpeed()
            
            print("Left Motor Direction: %s, Right Motor Direction: %s, Left Motor Ratio: %f, Right Motor Ratio: %f, Left Motor DC: %f, Right Motor DC: %f" % (leftMotor.direction, rightMotor.direction, leftMotor.ratio, rightMotor.ratio, leftMotor.dutyCycle, rightMotor.dutyCycle))
            
            
if __name__ == "__main__":

    GPIO.setmode(GPIO.BOARD)

    try:
        
        # Set up logging
        multiprocessing.log_to_stderr()
        logger = multiprocessing.get_logger()
        logger.setLevel(logging.INFO)

        # Motors
        leftMotor = Motors.Motor(33,35,37,200,"forward",10,1)
        leftMotor.startMotor()
        leftMotor.setDirection()
        leftMotor.setSpeed()
        rightMotor = Motors.Motor(31,29,32,200,"forward",10,1)
        rightMotor.startMotor()
        rightMotor.setDirection()
        rightMotor.setSpeed()
        
        # Create the queue to send motors data
        motorQueue = Queue()
        mc = MotorController(motorQueue)
        
        # Start the motor thread
        motorProcess = Process(target=mc.listen, name="Motor thread", args=())
        motorProcess.start()

        app.run(host="0.0.0.0",debug=1)
        
        while True:
            pass
    except KeyboardInterrupt:
        print ("parent received control-c")
    except:
        print("Other error occurred.")
    finally:
        motorProcess.terminate()
        leftMotor.motorCleanup()
        rightMotor.motorCleanup()
        GPIO.cleanup()
            

        
