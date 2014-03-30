import psycopg2
import datetime
from datetime import timedelta
import logging
from get_props import prop
from override import check_override
from switch import switch_boiler
from check_temp import check_temp

def get_schedule():
    logtype = prop('logtype')
    if logtype == 'file':
        logFile = prop('loglocation')
        logging.basicConfig(format='%(asctime)s: %(message)s ',filename=logFile, filemode='a', level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.DEBUG)
    
    #Define our connection string
    conn_string = prop('database')
    
    logging.debug("Connecting to database ->%s" % (conn_string))
    
    try:
        # get a connection, if a connect cannot be made an exception will be raised here
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        logging.debug("Connected!\n")
    except Exception as e:
        logging.debug("failed to connect to database -> %s" (e))
    

    try:
        #get current time and day of week
        day = datetime.date.today()
        time = datetime.datetime.now().time()
        dayOfWeek = datetime.date.strftime(day, '%A')
        
        logging.debug(dayOfWeek)
        
        #get schedule rows from database
        sql = """
              select id_shed, day, time, state from schedule where upper(day) = upper(%(day)s) and time <= %(curr_time)s order by time desc
              """
                
        cursor.execute(sql, {'day':dayOfWeek, 'curr_time':time})
        shed_row = cursor.fetchone()
        shed_row_str = str(shed_row)
        logging.debug('current schedule row = %s' % shed_row_str)
        
        while shed_row is None:
            pre_day = day-timedelta(days=1) 
            dayOfWeek = datetime.date.strftime(pre_day, '%A')
                        
            cursor.execute(sql, {'day':dayOfWeek, 'curr_time':time})
            shed_row = cursor.fetchone()
            shed_row_str = str(shed_row)
            logging.debug('current schedule row = %s' % shed_row_str)
        
        id_shed = shed_row[0]
        shed_day = shed_row[1]
        shed_time = shed_row[2]
        shed_state = shed_row[3]
        
    except Exception as e:
        logging.debug(e)
    
    try:
        sql = """
              select state from current_state
              """
        cursor.execute(sql)
        
        curr_state = cursor.fetchone()
    except Exception as e:
        logging.debug(e)
    
    try:
        temp = check_temp()
        logging.debug('temp is: %s' % temp)
        override = check_override(id_shed)
        
        #ON    FALSE    low    on
        #off    TRUE    low    on
        
        if shed_state == 'ON' and override is False and temp == 'LOW' and curr_state == 'OFF':
            switch_boiler('ON')        
        elif shed_state == 'OFF' and override is True and temp == 'LOW' and curr_state == 'OFF':
            switch_boiler('ON')        
        else:
            switch_boiler('OFF')
        
#         
#         if shed_state !=  curr_state and override == False: 
#             if shed_state == 'OFF':
#                 switch_boiler('OFF')
#             if shed_state == 'ON':
#                 if temp == 'LOW':
#                     switch_boiler('ON')
#         
#         if override is True and shed_state == 'OFF' and curr_state == 'OFF':
#             if temp == 'LOW':
#                 switch_boiler('ON')
#         
#         if override is False and shed_state == 'ON' and curr_state == 'OFF':
#         
#         if curr_state == 'ON' and temp == 'HIGH':
#             switch_boiler('OFF')
#         elif curr_state == 'ON' and temp == 'LOW':
            
        
    except Exception as e:
        logging.debug(e)
        
get_schedule()
