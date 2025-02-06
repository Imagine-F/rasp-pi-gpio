from gpiozero import OutputDevice
import time
import threading

LSBFIRST = 1
MSBFIRST = 2
dataPin   = OutputDevice(24)
latchPin  = OutputDevice(23)
clockPin  = OutputDevice(18)
num = (0xc0,0xf9,0xa4,0xb0,0x99,0x92,0x82,0xf8,0x80,0x90)
digitPin = (17,27,22,10)
outputs = list(map(lambda pin: OutputDevice(pin), digitPin))
counter = 0
t = 0
    
def shiftOut(order,val):      
    for i in range(0,8):
        clockPin.off()
        if(order == LSBFIRST):
            dataPin.on() if (0x01&(val>>i)==0x01) else dataPin.off()
        elif(order == MSBFIRST):
            dataPin.on() if (0x80&(val<<i)==0x80) else dataPin.off()
        clockPin.on()
            
def outData(data):
    latchPin.off()
    shiftOut(MSBFIRST,data)
    latchPin.on()
    
def selectDigit(digit):
    outputs[0].off() if ((digit&0x08) == 0x08) else outputs[0].on()
    outputs[1].off() if ((digit&0x04) == 0x04) else outputs[1].on()
    outputs[2].off() if ((digit&0x02) == 0x02) else outputs[2].on()
    outputs[3].off() if ((digit&0x01) == 0x01) else outputs[3].on()

def display(dec):   # display function for 7-segment display
    outData(0xff)   # eliminate residual display
    selectDigit(0x01)   # Select the first, and display the single digit
    outData(num[dec%10])
    time.sleep(0.003)   # display duration
    outData(0xff)
    selectDigit(0x02)   # Select the second, and display the tens digit
    outData(num[dec%100//10])
    time.sleep(0.003)
    outData(0xff)
    selectDigit(0x04)   # Select the third, and display the hundreds digit
    outData(num[dec%1000//100])
    time.sleep(0.003)
    outData(0xff)
    selectDigit(0x08)   # Select the fourth, and display the thousands digit
    outData(num[dec%10000//1000])
    time.sleep(0.003)
def timer():       
    global counter
    global t
    t = threading.Timer(1.0,timer)      # reset time of timer to 1s
    t.start()                           # Start timing
    counter+=1                          
    print ("counter : %d"%counter)
    
def loop():
    global t
    global counter
    t = threading.Timer(1.0,timer)      # set the timer
    t.start()                           # Start timing
    while True:
        display(counter)                # display the number counter
        
def destroy():  
    global t
    dataPin.close()
    latchPin.close()
    clockPin.close()     
    t.cancel()     

if __name__ == '__main__':
    print ('Program is starting...' )
    try:
        loop()  
    except KeyboardInterrupt:
        destroy()
        print("Ending program")
 
