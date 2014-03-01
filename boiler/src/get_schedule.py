import psycopg2
import logging
from get_props import prop

def get_shedule():
    
    logging.basicConfig(level=logging.DEBUG)
    
    sql = """
            select day, time, state from schedule
          """
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
    
    