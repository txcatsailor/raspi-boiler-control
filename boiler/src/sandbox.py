import check_temp
import psycopg2
from get_props import prop
shed_state = 'ON'
roomTemp = check_temp.temp('room').get_temp()
radTemp = check_temp.temp('rad').get_temp()
outsideTemp = check_temp.temp('outside').get_temp()

conn_string = prop('database')
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()

sql =   """
        insert into log (room_temp, rad_temp, outside_temp, datestamp, state) values (%(roomtemp)s, %(radtemp)s, 
        %(outsidetemp)s, (select now()), %(state)s)
        """
cursor.execute(sql, {'roomtemp':roomTemp, 'radtemp':radTemp, 'outsidetemp':outsideTemp, 'state':shed_state})
conn.commit()