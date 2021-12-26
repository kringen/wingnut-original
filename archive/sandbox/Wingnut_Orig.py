import RPi.GPIO as GPIO, urllib2, random, subprocess#, threading
import time



GPIO.setmode(GPIO.BOARD)

########## Setup Ultrasonic proximity detection
TRIG = 	# Ultrasonic emitter port
ECHO = 	# Ultrasonic receiver port
GPIO.setup(TRIG, GPIO.OUT)	# Set emmiter pin as output
GPIO.output(TRIG, 0)		# Set inital emitter value low
GPIO.setup(ECHO, GPIO.IN)	# Set receiver pin as input

########## Setup motor driver pins

MOTOR_B_ENB = 37 # Orange
MOTOR_B_IN4 = 35 # Yellow 
MOTOR_B_IN3 = 33 # Green
MOTOR_A_IN2 = 31 # Blue
MOTOR_A_IN1 = 29 # Purple
MOTOR_A_ENA = 32 # Gray

GPIO.setup(MOTOR_B_ENB, GPIO.OUT)
GPIO.setup(MOTOR_B_IN4, GPIO.OUT)
GPIO.setup(MOTOR_B_IN3, GPIO.OUT)
GPIO.setup(MOTOR_A_IN2, GPIO.OUT)
GPIO.setup(MOTOR_A_IN1, GPIO.OUT)
GPIO.setup(MOTOR_A_ENA, GPIO.OUT)

#p = GPIO.PWM(PWM_PIN, 1000) # create pwm at port 12 at 1 Hz
#p.start(1) # start at 0% duty cycle


okToSpeak = True



def getDistance():
	time.sleep(0.1)	# Give sensor 100 milliseconds to settle.

	# send 10 microsecond high
	GPIO.output(TRIG, 1)
	time.sleep(0.00001)
	GPIO.output(TRIG, 0)

	while GPIO.input(ECHO) == 0: 	# This loop runs until signal received
		pass
	start = time.time()

	while GPIO.input(ECHO) == 1: 	# Received the echo so loop until signal is low
		pass
	stop = time.time()

	return round((stop - start) * 17000,1)	# Calculate distance in CM

def pwmTest():
	global direction
	for dc in range(0,101, 5):
		p.ChangeDutyCycle(dc)
		print dc
		time.sleep(500.0 / 1000.0)
	for dc in range(100, -1, -5):
		p.ChangeDutyCycle(dc)
		print dc
		time.sleep(500.0 / 1000.0)

def RandomLine(afileName):
   with open(afileName, "r") as afile:
       line = next(afile)
       for num, aline in enumerate(afile):
           if random.randrange(num + 2): continue
           line = aline
       return line

def CheckIfOkToSpeak():
	global okToSpeak
	threading.Timer(10, CheckIfOkToSpeak).start()
	if okToSpeak == True:
		okToSpeak = False
	else: okToSpeak = True
	
def SpeechFromText(phrase):
   print (phrase)
   googleSpeechURL = "http://translate.google.com/translate_tts?tl=en&q=" + phrase
   subprocess.call(['mplayer', '-ao', 'alsa', '-really-quiet', '-noconsolecontrols', googleSpeechURL])

def SaySomethingRandom(context):
	if context == "niceResponse":
		filePath = "/home/pi/response_expressions.txt"
	elif context == "gettingClose":
		filePath = "/home/pi/proximity_expressions.txt"
	elif context == "takingControl":
		filePath = "/home/pi/taking_control.txt"
	else:
		filePath = "/home/pi/nothing_particular.txt"
	SpeechFromText (RandomLine(filePath))
	
try:
	#CheckIfOkToSpeak() #Set background thread to run periodically
	while True:
		distance = getDistance()
		#writeText("Obj: " + str(distance) + " cm",30,4)	
		print distance
		#if distance < 10:
		#	if okToSpeak == True:
		#		thread.start_new_thread(SaySomethingRandom, ("gettingClose",))
		#		okToSpeak = False
except:
	pass
	p.stop()	
	GPIO.cleanup()
	print "Exiting"
