import psycopg2
import logging
import datetime
from datetime import timedelta
from get_props import prop

logtype = prop('logtype')
if logtype == 'file':
    logFile = prop('loglocation')
    logging.basicConfig(format='%(asctime)s: %(message)s ',filename=logFile, filemode='a', level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.DEBUG)

def check_override(id_shed):

    conn_string = prop('database')  
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()

    sql =   """
            select id_shed, starttime, state from override
            """
    cursor.execute(sql)
    row = cursor.fetchone()
    
    try:
        over_shed = row[0]
        logging.debug("id_shed from override table = %d" % over_shed)
        logging.debug("id_shed from current schedule = %d" % id_shed)
        if over_shed != id_shed:
            cursor.execute("delete from override")
            conn.commit()
            logging.debug("override not null, doesn't match schedule")
            return False
        logging.debug("shedule overridden")
        return True
    except Exception as e:
        logging.debug(e)
        return False

def set_override():
 
    conn_string = prop('database')
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    
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
    shed_state = shed_row[3]
    
    if check_override(id_shed) is True:
        cursor.execute('delete from override')
        conn.commit()

    else:
        if shed_state == 'ON':
            state = 'OFF'
        else:
            state = 'ON'         
    
        cursor.execute('delete from override')
        conn.commit()
        
        sql =   """
                insert into override (id_over, id_shed, starttime, state) values (nextval('override_id_over_seq'), %(id_shed)s, %(time)s, %(state)s)"""
        cursor.execute(sql, {'id_shed':id_shed, 'time':time, 'state':state})
        conn.commit()
    cursor.close()
    

    
    