import psycopg2
from get_props import prop
import logging

def check_temp():
    logtype = prop('logtype')
    if logtype == 'file':
        logFile = prop('loglocation')
        logging.basicConfig(format='%(asctime)s: %(message)s ',filename=logFile, filemode='a', level=logging.DEBUG)
    else:
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
         
#     roomTemp = 15.375
#     radTemp = 42.123
#     outsideTemp = 8.123
    
    
    logging.debug('Room Temp: %s, Radiator Temp: %s, Outside Temp: %s' % (roomTemp, radTemp, outsideTemp))
    
    try:
        tolerance = int(prop('tolerance'))
        
        conn_string = prop('database')
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        
        sql =   """
                select target_temp from target_temp
                """
        cursor.execute(sql)
        
        target_temp = cursor.fetchone()
        cursor.close()
        try:
            target_temp = target_temp[0]
            logging.debug(target_temp)
        except:
            target_temp = None
    
        if target_temp is None:
            logging.debug('No target temp set, setting default to 21')
            target_temp = 21
        
        upper = target_temp + tolerance
        lower = target_temp - tolerance
        logging.debug('lower = %s' % lower)
        logging.debug('upper = %s' % upper)
        if roomTemp >= lower and roomTemp <= upper:
            logging.debug('temp within range')
            return 'WITHIN'
        elif roomTemp >= upper:
            logging.debug('HIGH')
            return 'HIGH'
        elif roomTemp <= lower:
            logging.debug('LOW')
            return 'LOW'
           
    except Exception as e:
        logging.debug(e) 