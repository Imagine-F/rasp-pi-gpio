from gpiozero import RGBLED
import time
import random

led = RGBLED(red=17, green=18, blue=27, active_high=False)

def setColor(r_val,g_val,b_val):   
    led.red=r_val/100             
    led.green = g_val/100         
    led.blue = b_val/100          

def loop():
    while True :
        r=random.randint(0,100)
        g=random.randint(0,100)
        b=random.randint(0,100)
        setColor(r,g,b)
        print ('r=%d, g=%d, b=%d ' %(r ,g, b))
        time.sleep(1)
        
def destroy():
    led.close()

if __name__ == '__main__': 
    print ('Program is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
        print("Ending program")