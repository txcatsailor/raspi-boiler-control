from bottle import route, redirect, request, run, jinja2_template, \
                    debug, static_file, response, template
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

# def todo_list():
#     """
#     Show the main page which is the current TODO list
#     """
#     conn = sqlite3.connect("todo.db")
#     c = conn.cursor()
#     c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
#     result = c.fetchall()
#     c.close()
#  
#     output = template("make_table", rows=result)
#     return output

@route('/getschedule', method='POST')
def get_schedule():
    rqstSession = request.get_cookie('pysessionid', secret=prop('cookieSecret')[0])
    if check_session(rqstSession) is True:
        conn_string = prop('database')[0]
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        sql =   """
                select id_shed, day, time, state from schedule
                """
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        
        return template('sched_table', rows=result)
    else:
        pysessionid = ''
        response.set_cookie('pysessionid', pysessionid, secret=prop('cookieSecret')[0], Expires='Thu, 01-Jan-1970 00:00:10 GMT', httponly=True)
        login()

@route('/setschedule', method='POST')
def set_schedule():
    rqstSession = request.get_cookie('pysessionid')
    if check_session(rqstSession) is True:
#        days = request.forms.allitems()
        return "<p>Set Schedule</p>" 
    
run(host='192.168.0.5', port=99, debug=True)
