from gpiozero import DigitalOutputDevice, Button
import time

relayPin = 17
buttonPin = 18
relay = DigitalOutputDevice(relayPin)
button = Button(buttonPin)
debounceTime = 50

def loop():
    relayState = 0
    lastChangeTime = round(time.time()*1000)
    buttonState = 1
    lastButtonState = 1
    reading = 1
    while True:
        reading = not button.value  
        if reading != lastButtonState :
            lastChangeTime = round(time.time()*1000)
        if ((round(time.time()*1000) - lastChangeTime) > debounceTime):
            if reading != buttonState :
                buttonState = reading;
                if buttonState == 0:
                    print("Button is pressed!")
                    relayState = not relayState
                    if relayState:
                        print("Turn on relay ...")
                    else :
                        print("Turn off relay ... ")
                else :
                    print("Button is released!")
        relay.on() if (relayState==1) else relay.off() 
        lastButtonState = reading
    
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
        