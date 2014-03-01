import psycopg2
import logging

def check_override(conn_string, id_shed):
    
    logging.basicConfig(level=logging.DEBUG)
    
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
            logging.debug("override not null, doesn't match schedule")
            return False
        logging.debug("shedule overridden")
        return True
    except Exception as e:
        logging.debug(e)
        return False

# conn_string = "host='localhost' dbname='boiler' user='postgres' password='tuppence'"
# id_shed = 16
# check_override(conn_string, id_shed)
    
    