from gpiozero import TonalBuzzer,Button
from gpiozero.tones import Tone
import time
import math

buzzer = TonalBuzzer(17)
button = Button(18)

def loop():
    while True:
        if button.is_pressed:
            alertor()
            print ('alertor turned on >>> ')
        else :
            stopAlertor()
            print ('alertor turned off <<<')
def alertor():
    buzzer.play(Tone(220.0)) 
    time.sleep(0.1)
        
def stopAlertor():
    buzzer.stop()
            
def destroy():
    buzzer.close()                  

if __name__ == '__main__':
    print ('Program is starting...')
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
        print("Ending program")