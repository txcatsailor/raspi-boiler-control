
import psycopg2
from passlib.hash import sha512_crypt
from get_props import prop
import logging

logtype = prop('logtype')
if logtype == 'file':
    logFile = prop('loglocation')
    logging.basicConfig(format='%(asctime)s: %(message)s ',filename=logFile, filemode='a', level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.DEBUG)


def get_password(userid):
    userid = userid.upper()
    logging.debug('get auth for %s' % userid)
    conn_string = prop('database')
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()

    sql =   """
            select auth from users where userid = %(userid)s
            """
    cursor.execute(sql, {'userid':userid})
    row = cursor.fetchone()
    if row is not None:
        dbpassword = row[0]
        logging.debug('db auth hash %s' % dbpassword)
        return dbpassword
    else:
        logging.debug('No details found for user')
        return None

def check_password(password, userid):
    logging.debug('username/auth to check is %s/%s' % (userid, password))
    dbpassword = get_password(userid)
    if dbpassword is not None:
        if sha512_crypt.verify(password, dbpassword):
            logging.debug('auth correct')
            return True
        else:
            logging.debug('auth incorrect')
            return False
    else:
        return False

def hash_password(password):
    userid = 'awatson'
    logging.debug('hash auth')
    hashed_password = sha512_crypt.encrypt(password)
    logging.debug('hashed auth = %s' % hashed_password)
      
    conn_string = prop('database')
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    
    sql =   """
            insert into users (id_usrr, userid, auth) values (nextval('users_id_usrr_seq'), %(userid)s, %(auth)s)
            """
    cursor.execute(sql, {'userid':userid, 'auth':hashed_password})
    conn.commit()
    cursor.close()

password = 'tuppence'
#userid = 'SUZY'
hash_password(password)
#check_password(auth, userid)