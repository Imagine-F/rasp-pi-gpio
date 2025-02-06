import sys
from time import sleep
from gpiostepper import Stepper

motorPins = (18, 23, 24, 25)
number_of_steps = 32
step_motor = Stepper(motorPins, number_of_steps = number_of_steps)   
speed = 600
amount_of_gear_reduction = 64
number_of_steps_per_revolution_geared_output = number_of_steps * amount_of_gear_reduction
step_motor.set_speed(speed)
def loop():
    while True:
        step_motor.step(number_of_steps_per_revolution_geared_output) # rotating 360 deg clockwise
        sleep(0.5)
        step_motor.step(-number_of_steps_per_revolution_geared_output)# rotating 360 deg anticlockwise
        sleep(0.5)

if __name__ == "__main__":
    print ('Program is starting...')
    try:
        loop()
    except KeyboardInterrupt:
        print("Ending program")
        