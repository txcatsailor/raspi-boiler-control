import RPi.GPIO as GPIO

def switch_boiler(shed_state):
    # use P1 header pin numbering convention
    GPIO.setmode(GPIO.BOARD)

    # Set up the GPIO channels - one input and one output
    GPIO.setup(22, GPIO.OUT)
    
    if shed_state == 'ON':
        GPIO.output(22, GPIO.HIGH)
    elif shed_state == 'OFF':
        GPIO.output(22, GPIO.LOW)
        