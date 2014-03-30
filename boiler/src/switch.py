import RPi.GPIO as GPIO
from get_props import prop
import psycopg2
import logging

def switch_boiler(shed_state):
    
    try:
        conn_string = prop('database')
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        sql =   """
                delete from current_state
                """
        cursor.execute(sql)
        conn.commit()
        
        sql =   """
                insert into current_state (state) values ('%(state)s')
                """
        cursor.execute(sql, {'state': shed_state})
    except Exception as e:
        logging.debug(e)
    
    pin = prop('gpio')
    # use P1 header pin numbering convention
    GPIO.setmode(GPIO.BOARD)

    # Set up the GPIO channels - one input and one output
    GPIO.setup(pin, GPIO.OUT)
    
    if shed_state == 'ON':
        GPIO.output(pin, GPIO.HIGH)
    elif shed_state == 'OFF':
        GPIO.output(pin, GPIO.LOW)
        