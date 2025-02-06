from gpiozero import LED
from time import sleep

ledPins = [17, 18, 27, 22, 23, 24, 25, 2, 3, 8]
leds = [LED(pin=pin) for pin in ledPins] 
    
def loop():
    while True:
        for index in range(0,len(ledPins),1):
            leds[index].off()  
            sleep(0.1)
            leds[index].on() 
        for index in range(len(ledPins)-1,-1,-1):
            leds[index].off()  
            sleep(0.1)
            leds[index].on() 

if __name__ == '__main__':
    print ('Program is starting...')
    try:
        loop()
    except KeyboardInterrupt:
        print("Ending program")
    finally:
        for index in range(0,len(ledPins),1): 
            leds[index].close()  

