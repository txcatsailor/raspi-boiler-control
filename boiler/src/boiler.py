import psycopg2
import datetime
from datetime import timedelta
import logging
from get_props import prop
from override import check_override
from switch import switch_boiler
from check_temp import check_temp

def get_schedule():
    
    logFile = prop('logLocation')

#    logging.basicConfig(format='%(asctime)s: %(message)s ',filename=logFile[0], filemode='a', level=logging.DEBUG)
    logging.basicConfig(level=logging.DEBUG)
    
    #Define our connection string
    conn_string = prop('database')[0]
    
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
        
        if curr_state == 'ON':
            if check_temp() == 'low':
                switch_on = True
            else:
                switch_on = False
        
        if shed_state !=  curr_state:
            override = check_override(id_shed)
            if override is False:
                switch_boiler(shed_state)
    except Exception as e:
        logging.debug(e)
        
get_schedule()
