import psycopg2
from get_props import prop
import logging

def check_temp():
    logging.basicConfig(level=logging.DEBUG)
    try: 
        f=open('/sys/bus/w1/devices/28-0000058cd8ae/w1_slave', 'r')
        for l in f:
                if 't=' in l:
                        roomTemp=(float(l.split('=',1)[1].strip().replace('\n', '')))/1000
        f.close()
    except Exception as e:
        logging.debug(e)
    try:    
        f=open('/sys/bus/w1/devices/28-0000058e3500/w1_slave', 'r')
        for l in f:
                if 't=' in l:
                        radTemp=(float(l.split('=',1)[1].strip().replace('\n', '')))/1000
        f.close()
    except Exception as e:
        logging.debug(e)
     
    try:
        f=open('/sys/bus/w1/devices/28-0000058e2b9c/w1_slave', 'r')
        for l in f:
                if 't=' in l:
                        outsideTemp=(float(l.split('=',1)[1].strip().replace('\n', '')))/1000
        f.close()
    except Exception as e:
        logging.debug(e)
         
    
    logging.debug('Room Temp: %s, Radiator Temp: %s, Outside Temp: %s' % (roomTemp, radTemp, outsideTemp))
    
    try:
        tolerance = int(prop('tolerance')[0])
        
        conn_string = prop('database')[0]
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        
        sql =   """
                select target_temp from target_temp
                """
        cursor.execute(sql)
        
        target_temp = cursor.fetchone()
        
        if target_temp is None:
            logging.debug('No target temp set, setting default to 21')
            target_temp = 21
        
        upper = target_temp + tolerance
        lower = target_temp - tolerance
        
        if roomTemp in range(lower, upper):
            logging.debug('temp within range')
            return True
        elif roomTemp >= upper:
            logging.debug('high')
            return 'high'
        elif roomTemp <= lower:
            logging.debug('low')
            return 'low'
           
    except Exception as e:
        logging.debug(e)

check_temp() 