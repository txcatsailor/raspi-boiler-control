import psycopg2
import hashlib
import uuid
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
    logging.debug('get password for %s' % userid)
    conn_string = prop('database')
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    
    sql =   """
            select password, salt from users where userid = %(userid)s
            """
    cursor.execute(sql, {'userid':userid})
    row = cursor.fetchone()
    if row is not None:
        dbpassword = row[0]
        dbsalt = str(row[1])
        logging.debug('db password hash %s' % dbpassword)
        logging.debug('db password salt %s' % dbsalt)
        return dbpassword, dbsalt
    else:
        logging.debug('No details found for user')
        return None, None
    
def check_password(password, userid):
    logging.debug('username/password to check is %s/%s' % (password, userid))
    dbpassword, dbsalt = get_password(userid)
    if dbpassword is not None:
        test = hash_password(password, dbsalt)
        logging.debug('test password hash %s' % test)
        if test == dbpassword:
            logging.debug('password correct')
            return True
        else: 
            logging.debug('password incorrect')
            return False
    else:
        return False

def hash_password(password, salt):
    if salt == '0':
        logging.debug('hashing password')
        logging.debug('generate salt')
        salt = uuid.uuid4().hex
        logging.debug('salt = %s' % salt)
        hashed_password = crypt(password, salt)
        logging.debug('hashed password = %s' % hashed_password)
        return salt, hashed_password
    else:
        logging.debug('hash password for compare')
        hashed_password = crypt(password, salt)
        logging.debug('hashed password = %s' % hashed_password)
        return hashed_password

def crypt(password, salt):
    hashed_password = hashlib.sha512(password.encode(encoding='utf_8') + salt.encode(encoding='utf_8')).hexdigest()
    return hashed_password