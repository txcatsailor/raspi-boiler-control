import RPi.GPIO as GPIO
from get_props import prop

def switch_boiler(shed_state):
    pin = prop('gpio')
    # use P1 header pin numbering convention
    GPIO.setmode(GPIO.BOARD)

    # Set up the GPIO channels - one input and one output
    GPIO.setup(pin, GPIO.OUT)
    
    if shed_state == 'ON':
        GPIO.output(pin, GPIO.HIGH)
    elif shed_state == 'OFF':
        GPIO.output(pin, GPIO.LOW)
        