#!/usr/bin/env python3
#############################################################################
# Filename    : Motor.py
# Description : Control Motor with L293D
# Author      : www.freenove.com
# modification: 2023/05/11
########################################################################
from gpiozero import DigitalOutputDevice,PWMOutputDevice
import time
from ADCDevice import *
import smbus

motoRPin1 = DigitalOutputDevice(27)
motoRPin2 = DigitalOutputDevice(17)
enablePin = PWMOutputDevice(22,frequency=1000)
adc = ADCDevice()

def setup():
    global adc
    if(adc.detectI2C(0x48)):
        adc = PCF8591()
    elif(adc.detectI2C(0x4b)):
        adc = ADS7830()
    else:
        exit(-1)
def mapNUM(value,fromLow,fromHigh,toLow,toHigh):
    return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow) + toLow

def motor(ADC):
    value = ADC -128
    if (value > 0):
        motoRPin1.on()
        motoRPin2.off()
        print ('Turn Forward...')
    elif (value < 0):
        motoRPin1.off() 
        motoRPin2.on()
        print ('Turn Backward...')
    else :
        motoRPin1.off()
        motoRPin2.off()
        print ('Motor Stop...')
    b=mapNUM(abs(value),0,128,0,100)
    enablePin.value = b / 100.0 
    print ('The PWM duty cycle is %d%%\n'%(abs(value)*100/127))

def loop():
    while True:
        value = adc.analogRead(0)
        print ('ADC Value : %d'%(value))
        motor(value)
        time.sleep(0.2)

def destroy():
    motoRPin1.close()          
    motoRPin2.close()        
    enablePin.close()
    adc.close()

if __name__ == '__main__':  # Program entrance
    print ('Program is starting ... ')
    setup()
    try:
        loop()
    except KeyboardInterrupt: # Press ctrl-c to end the program.
        destroy()
        print("Ending program")
        
        
      
class ADCDevice(object):
    def __init__(self):
        self.cmd = 0
        self.address = 0
        self.bus=smbus.SMBus(1)
        # print("ADCDevice init")
        
    def detectI2C(self,addr):
        try:
            self.bus.write_byte(addr,0)
            print("Found device in address 0x%x"%(addr))
            return True
        except:
            print("Not found device in address 0x%x"%(addr))
            return False
            
    def close(self):
        self.bus.close()
        
class PCF8591(ADCDevice):
    def __init__(self):
        super(PCF8591, self).__init__()
        self.cmd = 0x40     # The default command for PCF8591 is 0x40.
        self.address = 0x48 # 0x48 is the default i2c address for PCF8591 Module.
        
    def analogRead(self, chn): # PCF8591 has 4 ADC input pins, chn:0,1,2,3
        value = self.bus.read_byte_data(self.address, self.cmd+chn)
        value = self.bus.read_byte_data(self.address, self.cmd+chn)
        return value
    
    def analogWrite(self,value): # write DAC value
        self.bus.write_byte_data(address,cmd,value)	

class ADS7830(ADCDevice):
    def __init__(self):
        super(ADS7830, self).__init__()
        self.cmd = 0x84
        self.address = 0x4b # 0x4b is the default i2c address for ADS7830 Module.   
        
    def analogRead(self, chn): # ADS7830 has 8 ADC input pins, chn:0,1,2,3,4,5,6,7
        value = self.bus.read_byte_data(self.address, self.cmd|(((chn<<2 | chn>>1)&0x07)<<4))
        return value

