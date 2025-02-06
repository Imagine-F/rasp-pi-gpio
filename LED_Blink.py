from gpiozero import LED
from time import sleep

led = LED(17)

def loop():
    while True:
        led.on()
        print ('led turned on >>>')
        sleep(1)
        led.off()
        print ('led turned off <<<')
        sleep(1)

if __name__ == '__main__':
    print ('Program is starting ... \n')
    try:
        loop()
    except KeyboardInterrupt:
        print("Ending program")
