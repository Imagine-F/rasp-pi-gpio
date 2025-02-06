from gpiozero import AngularServo
import time
 
myGPIO=18
SERVO_DELAY_SEC = 0.001 
myCorrection=0.0
maxPW=(2.5+myCorrection)/1000
minPW=(0.5-myCorrection)/1000
servo =  AngularServo(myGPIO,initial_angle=0,min_angle=0, max_angle=180,min_pulse_width=minPW,max_pulse_width=maxPW)

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
        print("Ending program")