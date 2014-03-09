from bottle import route, redirect, request, run, jinja2_template, \
                    debug, static_file, response, template, get
import hashlib
import uuid
from password import check_password
from get_props import prop
from session import get_sessionid, set_session, check_session
import psycopg2

@route('/')
def login():
    pysessionid = get_sessionid()
    response.set_cookie('pysessionid', pysessionid, secret=prop('cookieSecret')[0], httponly=True)
    return template('login')

@route('/main', method='POST')
def main():
    rqstSession = request.get_cookie('pysessionid', secret=prop('cookieSecret')[0])
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_password(password, username) is True:
        set_session(rqstSession)            
        return template('main')
    else:
        return template('login')


@route('/getschedule', method='any')
def get_schedule():
    rqstSession = request.get_cookie('pysessionid', secret=prop('cookieSecret')[0])
    if check_session(rqstSession) is True:
        conn_string = prop('database')[0]
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        sql =   """
                select id_shed, day, time, state from schedule order by seq, time
                """
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        
        return template('sched_table', rows=result)
    else:
        pysessionid = ''
        response.set_cookie('pysessionid', pysessionid, secret=prop('cookieSecret')[0], Expires='Thu, 01-Jan-1970 00:00:10 GMT', httponly=True)
        redirect('/login')




@route('/edit/:id_shed', method='any')
def edit_item(id_shed):
    rqstSession = request.get_cookie('pysessionid', secret=prop('cookieSecret')[0])
    if check_session(rqstSession) is True:
        if request.forms.get('save','').strip():
            id_shed = request.forms.get('id_shed','').strip()
            state = request.forms.get('state','').strip()
            time = request.forms.get('time','').strip()
        
            conn_string = prop('database')[0]
            conn = psycopg2.connect(conn_string)
            cursor = conn.cursor()
            sql =   """
                    update schedule set time = %(time)s, state = %(state)s where id_shed = %(id_shed)s
                    """
            cursor.execute(sql, {'time':time, 'state':state, 'id_shed':id_shed})
            conn.commit()
            redirect('/getschedule')
        else:
            conn_string = prop('database')[0]
            conn = psycopg2.connect(conn_string)
            cursor = conn.cursor()
            sql =   """
                    select id_shed, day, time, state from schedule where id_shed = %(id_shed)s
                    """
            cursor.execute(sql, {'id_shed':id_shed})
            cur_data = cursor.fetchone()
     
            return template('edit_schedule', old=cur_data, id_shed=id_shed)
    else:
        pysessionid = ''
        response.set_cookie('pysessionid', pysessionid, secret=prop('cookieSecret')[0], Expires='Thu, 01-Jan-1970 00:00:10 GMT', httponly=True)
        redirect('/login')

@route('/newschedule', method='any')
def new_schedule():
    rqstSession = request.get_cookie('pysessionid', secret=prop('cookieSecret')[0])
    if check_session(rqstSession) is True:
        if request.forms.get('save','').strip():
            day = request.forms.get('day', '').strip()
            state = request.forms.get('state','').strip()
            time = request.forms.get('time','').strip()
            seq_dict={'MONDAY':1, 'TUESDAY':2, 'WEDNESDAY':3, 'THURSDAY':4, 'FRIDAY':5, 'SATURDAY':6, 'SUNDAY':7}
            seq=seq_dict[day]
            conn_string = prop('database')[0]
            conn = psycopg2.connect(conn_string)
            cursor = conn.cursor()
            
            sql =   """
                    insert into schedule (id_shed, day, time, state) values (nextval('schedule_id_shed_seq'), %(day)s, %(time)s, %(state)s)
                    """
            cursor.execute(sql, {'time':time, 'state':state, 'day':day})
            conn.commit()
            cursor.close()
            redirect('/getschedule')
        else:
            return template('new_schedule')
    else:
        pysessionid = ''
        response.set_cookie('pysessionid', pysessionid, secret=prop('cookieSecret')[0], Expires='Thu, 01-Jan-1970 00:00:10 GMT', httponly=True)
        redirect('/login')


###########





run(host='192.168.0.5', port=99, debug=True)
