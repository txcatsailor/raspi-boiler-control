from bottle import route, redirect, request, run, jinja2_template, \
                    debug, static_file, response, template
import hashlib
import uuid
from password import check_password
from get_props import prop
from session import get_sessionid, set_session, check_session

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

@route('/getshedule', method='GET')
def get_schedule():
    rqstSession = request.get_cookie('pysessionid')
    if check_session(rqstSession) is True:
        return template('getschedule')

@route('/setshedule', method='POST')
def set_schedule():
    rqstSession = request.get_cookie('pysessionid')
    if check_session(rqstSession) is True:
        days = request.forms.allitems()

    
run(host='192.168.0.5', port=99, debug=True)
