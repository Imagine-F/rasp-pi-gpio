from gpiozero import DigitalOutputDevice, Button
import time

relayPin = 17
buttonPin = 18
relay = DigitalOutputDevice(relayPin)
button = Button(buttonPin)

def onButtonPressed():
    relay.toggle()
    if relay.value :
        print("Turn on relay ...")
    else :
        print("Turn off relay ... ")    

def loop():
    button.when_pressed = onButtonPressed
    while True:
        time.sleep(1)
    
def destroy():
    relay.close()
    button.close()

if __name__ == '__main__':
    print ('Program is starting...')
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
        print("Ending program")