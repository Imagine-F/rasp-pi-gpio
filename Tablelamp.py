from gpiozero import LED, Button
import time

led = LED(17) # define LED pin according to BCM Numbering
button = Button(18) # define Button pin according to BCM Numbering

def onButtonPressed():
    led.toggle()
    if led.is_lit :
        print("Led turned on >>>")
    else :
        print("Led turned off <<<")    
def loop():
    #Button detect
    button.when_pressed = onButtonPressed
    while True:
        time.sleep(1)
def destroy():
    led.close()
    button.close()    
if __name__ == '__main__':
    print ('Program is starting...')
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
        print("Ending program")
