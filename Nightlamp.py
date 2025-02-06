from gpiozero import PWMLED
import time
from ADCDevice import *

ledPin = 17
led = PWMLED(ledPin)
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
        value = adc.analogRead(0)
        led.value = value / 255.0
        voltage = value / 255.0 * 3.3
        print ('ADC Value : %d, Voltage : %.2f'%(value,voltage))
        time.sleep(0.01)

def destroy():
    led.close()
    adc.close()
    
if __name__ == '__main__':
    print ('Program is starting ... ')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
        print("Ending program")
        