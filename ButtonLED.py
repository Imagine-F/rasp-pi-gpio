from gpiozero import LED, Button

led = LED(17)
button = Button(18)

def loop():
    while True:
        if button.is_pressed:
            print("Button is pressed, led turned on >>>")
        else :
            led.off()
            print("Button is released, led turned off <<<")    

if __name__ == '__main__':
    print ('Program is starting...')
    try:
        loop()
    except KeyboardInterrupt:
        print("Ending program")
