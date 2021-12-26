import random, subprocess, time

def RandomLine(afileName):
   with open(afileName, "r") as afile:
       line = next(afile)
       for num, aline in enumerate(afile):
           if random.randrange(num + 2): continue
           line = aline
       return line
	

def SpeechFromText(phrase):
   print (phrase)
   randFile = "/tmp/" + str(random.randint(1,10000)) + ".wav"
   subprocess.call(['pico2wave', '-w', randFile, phrase])
   subprocess.call(['aplay', randFile])
   
def SaySomethingRandom(context):
	if context == "niceResponse":
		filePath = "/home/pi/response_expressions.txt"
	elif context == "gettingClose":
		filePath = "/home/pi/proximity_expressions.txt"
	elif context == "takingControl":
		filePath = "/home/pi/taking_control.txt"
	SpeechFromText (RandomLine(filePath))

if __name__ == '__main__':
	SaySomethingRandom("niceResponse")
