import time
from ADCDevice import *

adc = ADCDevice()

def setup():
    global adc
    if(adc.detectI2C(0x48)):
        adc = PCF8591()
    elif(adc.detectI2C(0x4b)):
        adc = ADS7830()
    else:
        print("No correct I2C address found, \n"
        "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
        "Program Exit. \n");
        exit(-1)
        
def loop():
    while True:
        value = adc.analogRead(0)
        voltage = value / 255.0 * 3.3
        print ('ADC Value : %d, Voltage : %.2f'%(value,voltage))
        time.sleep(0.1)

def destroy():
    adc.close()
    
if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        destroy()
        print("Ending program")
        