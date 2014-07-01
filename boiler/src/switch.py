import RPi.GPIO as GPIO
from get_props import prop
import psycopg2
import logging
import check_temp

def switch_boiler(shed_state):
      
    try:
        roomTemp = check_temp.temp('room').get_temp()
        radTemp = check_temp.temp('rad').get_temp()
        outsideTemp = check_temp.temp('outside').get_temp()
        
        conn_string = prop('database')
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        sql =   """
                delete from current_state
                """
        cursor.execute(sql)
        conn.commit()
         
        sql =   """
                insert into current_state (state) values (%(state)s)
                """
        cursor.execute(sql, {'state': shed_state})
        conn.commit()
        
        sql =   """
        insert into log (room_temp, rad_temp, outside_temp, datestamp, state) values (%(roomtemp)s, %(radtemp)s, 
        %(outsidetemp)s, (select now()), %(state)s)
        """
        
        cursor.execute(sql, {'roomtemp':roomTemp, 'radtemp':radTemp, 'outsidetemp':outsideTemp, 'state':shed_state})
        conn.commit()
        
    except Exception as e:
        logging.debug('error in database connection in switch_boiler: %s' % e)
     
    try:
        pin = int(prop('gpio'))
        # use P1 header pin numbering convention
        GPIO.setmode(GPIO.BOARD)
        # Set up the GPIO channels - one input and one output
        GPIO.setwarnings(False)
        GPIO.setup(pin, GPIO.OUT)
         
        if shed_state == 'ON':
            GPIO.output(pin, GPIO.HIGH)
        elif shed_state == 'OFF':
            GPIO.output(pin, GPIO.LOW)
    except Exception as e:
        logging.debug('Error switching boiler state %s' % e)