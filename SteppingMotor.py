
from gpiozero import OutputDevice
import time 

motorPins = (18, 23, 24, 25)
motors = list(map(lambda pin: OutputDevice(pin), motorPins))
CCWStep = (0x01,0x02,0x04,0x08)
CWStep = (0x08,0x04,0x02,0x01)
     
def moveOnePeriod(direction,ms):    
    for j in range(0,4,1):
        for i in range(0,4,1):
            if (direction == 1):
                motors[i].on() if (CCWStep[j] == 1<<i) else motors[i].off()
            else :
                motors[i].on() if CWStep[j] == 1<<i else motors[i].off()
        if(ms<3):
            ms = 3
        time.sleep(ms*0.001)    
        
def moveSteps(direction, ms, steps):
    for i in range(steps):
        moveOnePeriod(direction, ms)
        
def motorStop():
    for i in range(0,4,1):
        motors.off()    
           
def loop():
    while True:
        moveSteps(0,3,512)
        time.sleep(0.5)
        moveSteps(1,3,512)  # rotating 360 deg anticlockwise
        time.sleep(0.5)
    
if __name__ == '__main__':
    print ('Program is starting...')
    try:
        loop()
    except KeyboardInterrupt:
        print("Ending program")
        