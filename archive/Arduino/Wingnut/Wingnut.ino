#include <Wire.h>
 
#define SLAVE_ADDRESS 0x04

double temp;

int option = 0;
int voltPin = 0;
float vout = 0.0;
float vin = 0.0;
float R1 = 20000.0;
float R2 = 5000.0;
int value = 0;
int voltsInt = 7;
int voltsMod = 9;
int returnVal;

void setup(){
    // Setup voltage pin as input
    pinMode(voltPin, INPUT);
    
    // initialize i2c as slave
    Wire.begin(SLAVE_ADDRESS);
   
    // define callbacks for i2c communication
    Wire.onReceive(receiveData);
    Wire.onRequest(requestCallback);

}
void loop(){
  
getVoltage();
delay(50);
   
}

void requestCallback()
{
      Wire.write(returnVal);
}

void receiveData(int byteCount){
    int command = Wire.read();
    if(command == 1)
    {
      // Return integer part of voltage
      returnVal = voltsInt;
    }
    
    if(command == 2)
    {
      // Return Mod part ov voltage
      returnVal = voltsMod;
    }
}

void getVoltage() {
    value = analogRead(voltPin);
    vout = (value * 5.0) / 1024.0;
    vin = vout / (R2/(R1+R2)); 
    voltsInt = (int)floor(vin);
    voltsMod = (int)(vin - voltsInt) * 100;
}
