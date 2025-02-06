
from gpiozero import DistanceSensor
from time import sleep

trigPin = 23
echoPin = 24
sensor = DistanceSensor(echo=echoPin, trigger=trigPin ,max_distance=3)

def loop():
    while True:
        print('Distance: ', sensor.distance * 100,'cm')
        sleep(1)
        
if __name__ == '__main__':
    print ('Program is starting...')
    try:
        loop()
    except KeyboardInterrupt:
        sensor.close()
        print("Ending program")
