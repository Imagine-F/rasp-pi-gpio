from gpiozero import RGBLED
import time
from ADCDevice import *

led = RGBLED(red=22, green=27, blue=17, active_high=False)
adc = ADCDevice()

def setup():
    global adc
    if(adc.detectI2C(0x48)):
        adc = PCF8591()
    elif(adc.detectI2C(0x4b)):
        adc = ADS7830()
    else:
        exit(-1)
    
def loop():
    while True:     
        value_Red = adc.analogRead(0)
        value_Green = adc.analogRead(1)
        value_Blue = adc.analogRead(2)
        led.red   =value_Red/255 
        led.green =value_Green/255
        led.blue  =value_Blue/255
        print ('ADC Value value_Red: %d ,\tvlue_Green: %d ,\tvalue_Blue: %d'%(value_Red,value_Green,value_Blue))
        time.sleep(0.01)

def destroy():
    adc.close()
    led.close()
    
if __name__ == '__main__':
    print ('Program is starting ... ')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
        print("Ending program")
