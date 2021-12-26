# apt-get install python-gps
# enable serial using raspi-config
# stty -F /dev/ttyACM0 9600

import gps

session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

while True:
    try:
        report = session.next()
        print(report)
        if report['class'] == 'TPV':
            coords = open("/home/pi/Devel/gps/coords.txt","w")
            coords.write(str(report.time))
            coords.write(",")
            coords.write(str(report.lat))
            coords.write(",")
            coords.write(str(report.lon))
            coords.write(",")
            coords.write(str(report.alt))
            coords.write(",")
            coords.write(str(report.speed))
            coords.close()
    except KeyError:
        pass
    except KeyboardInterrupt:
        quit()
    except StopIteration:
        session = None
        print "GPSD has terminated"
