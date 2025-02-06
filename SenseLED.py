from gpiozero import LED,MotionSensor
import time

ledPin = 18
sensorPin = 17
led    = LED(ledPin)     
sensor = MotionSensor(sensorPin)
sensor.wait_for_no_motion()
def loop():
    currentstate = False
    previousstate = False
    while True:
        currentstate = sensor.motion_detected
        if currentstate == True and previousstate == False:
            led.on()
            print("Motion detected!led turned on >>>")
            previousstate = True
        elif currentstate == False and previousstate == True:
            led.off()
            print("No Motion!led turned off <<")
            previousstate = False
        time.sleep(0.01)

def destroy():
    led.close() 
    sensor.close()                     

if __name__ == '__main__': 
    print ('Program is starting...')
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
        print("Ending program")