from gpiozero import Buzzer, Button  
import time

buzzer = Buzzer(17)
button = Button(18)

def onButtonPressed():
    buzzer.on()
    print("Button is pressed, buzzer turned on >>>")
    
def onButtonReleased():
    buzzer.off()
    print("Button is released, buzzer turned off <<<")

def loop():
    button.when_pressed = onButtonPressed
    button.when_released = onButtonReleased
    while True :
        time.sleep(1)
        
def destroy():
    buzzer.close()
    button.close()

if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
        print("Ending program")