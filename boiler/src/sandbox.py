import psycopg2
from get_props import prop
import datetime
import logging
from datetime import timedelta
from password import hash_password

@route('/newuser', method='any')
def new_user():
    rqstSession = request.get_cookie('pysessionid', secret=prop('cookieSecret')[0])
    if check_session(rqstSession) is True:
        if request.forms.get('save','').strip():
            username = request.forms.get('username', '').strip()
            password = request.forms.get('password','').strip()
            confpassword = request.forms.get('confpassword','').strip()
            salt = '0'
            if password == confpassword:
                hash_password(username, salt)
            else:
                return template('newuser')
        else:
            return template('newuser')
    else:
          pysessionid = ''
          response.set_cookie('pysessionid', pysessionid, secret=prop('cookieSecret')[0], Expires='Thu, 01-Jan-1970 00:00:10 GMT', httponly=True)
          redirect('/login') 
    

# @route('/newschedule', method='any')
# def new_schedule():
#     rqstSession = request.get_cookie('pysessionid', secret=prop('cookieSecret')[0])
#     if check_session(rqstSession) is True:
#         if request.forms.get('save','').strip():
#             day = request.forms.get('day', '').strip()
#             state = request.forms.get('state','').strip()
#             time = request.forms.get('time','').strip()
#             seq_dict={'MONDAY':1, 'TUESDAY':2, 'WEDNESDAY':3, 'THURSDAY':4, 'FRIDAY':5, 'SATURDAY':6, 'SUNDAY':7}
#             seq=seq_dict[day]
#             conn_string = prop('database')[0]
#             conn = psycopg2.connect(conn_string)
#             cursor = conn.cursor()
#             
#             sql =   """
#                     insert into schedule (id_shed, day, time, state, seq) values (nextval('schedule_id_shed_seq'), %(day)s, %(time)s, %(state)s, %(seq)s)
#                     """
#             cursor.execute(sql, {'time':time, 'state':state, 'day':day, 'seq':seq})
#             conn.commit()
#             cursor.close()
#             redirect('/getschedule')
#         else:
#             return template('new_schedule')
#     else:
#         pysessionid = ''
#         response.set_cookie('pysessionid', pysessionid, secret=prop('cookieSecret')[0], Expires='Thu, 01-Jan-1970 00:00:10 GMT', httponly=True)
#         redirect('/login') 