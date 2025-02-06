import os
os.system("sudo pigpiod")
from gpiozero import AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory
import time

my_factory = PiGPIOFactory() 
myGPIO=18
SERVO_DELAY_SEC = 0.001 
myCorrection=0.0
maxPW=(2.5+myCorrection)/1000
minPW=(0.5-myCorrection)/1000
servo =  AngularServo(myGPIO,initial_angle=0,min_angle=0, max_angle=180,min_pulse_width=minPW,max_pulse_width=maxPW,pin_factory=my_factory)

def loop():
    while True:
        for angle in range(0, 181, 1):
            servo.angle = angle
            time.sleep(SERVO_DELAY_SEC)
        time.sleep(0.5)
        for angle in range(180, -1, -1):
            servo.angle = angle
            time.sleep(SERVO_DELAY_SEC)
        time.sleep(0.5)

if __name__ == '__main__':
    print ('Program is starting...')
    try:
        loop()
    except KeyboardInterrupt:
        servo.close()
        os.system("sudo killall pigpiod")
        print("Ending program")