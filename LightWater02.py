
from gpiozero import OutputDevice
import time
LSBFIRST = 1
MSBFIRST = 2
dataPin   = OutputDevice(17)
latchPin  = OutputDevice(27)
clockPin  = OutputDevice(22)
   
def shiftOut(order,val):      
    for i in range(0,8):
        clockPin.off()
        if(order == LSBFIRST):
            dataPin.on() if (0x01&(val>>i)==0x01) else dataPin.off()
        elif(order == MSBFIRST):
            dataPin.on() if (0x80&(val<<i)==0x80) else dataPin.off()
        clockPin.on()

def loop():
    while True:
        x=0x01
        for i in range(0,8):
            latchPin.off()
            shiftOut(LSBFIRST,x)
            latchPin.on()
            x<<=1
            time.sleep(0.1)
        x=0x80
        for i in range(0,8):
            latchPin.off()
            shiftOut(LSBFIRST,x)
            latchPin.on()
            x>>=1
            time.sleep(0.1)

def destroy():   
    dataPin.close()
    latchPin.close()
    clockPin.close() 

if __name__ == '__main__':
    print ('Program is starting...' )
    try:
        loop()  
    except KeyboardInterrupt:
        destroy()
        print("Ending program")
