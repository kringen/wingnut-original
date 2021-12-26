import smbus
import time
bus = smbus.SMBus(1)

def writeI2C(address, value):
    bus.write_byte(address,value)
def readNumber(address):
    number = bus.read_byte(address)
    return number

def writeNumber(address, value):
    bus.write_byte(address,int(value))
    return -1
    
def getVoltageI2C(address):
    # send a command to return voltage
    bus.write_byte(address, 1)
    # read next 2 bytes to get voltage
    time.sleep(0.5)
    voltageInt = bus.read_byte(address)
    time.sleep(0.5)
    voltageMod = bus.read_byte(address)
    print("Voltage: " + str(voltageInt) + "." + str(voltageMod))

if __name__ == '__main__':
   #getVoltageI2C(0x04)
   bus.write_byte(0x04, 1)
   time.sleep(0.5)
   voltsInt = bus.read_byte(0x04)
   bus.write_byte(0x04, 2)
   time.sleep(0.05)
   voltsMod = bus.read_byte(0x04)
   print("Read: " + str(voltsInt) + "." + str(voltsMod))
       
