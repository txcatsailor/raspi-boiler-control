import psycopg2
import hashlib
import uuid
from get_props import prop

def get_password(userid):
    userid = userid.upper()
    conn_string = prop('database')[0]
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    
    sql =   """
            select password, salt from users where userid = %(userid)s
            """
    cursor.execute(sql, {'userid':userid})
    row = cursor.fetchone()
    if row is not None:
        dbpassword = row[0]
        dbsalt = row[1]
        return dbpassword, dbsalt
    else:
        return None, None
    
def check_password(password, userid):
    userid = userid.upper()
    dbpassword, dbsalt = get_password(userid)
    if dbpassword is not None:
        test = hash_password(password, dbsalt)
        print(test)
        if test == dbpassword:
            return True
        else: 
            return False
    else:
        return False

def hash_password(password, salt):
    if salt == '0':
        salt = uuid.uuid4().hex
        hashed_password = hashlib.sha512(password.encode(encoding='utf_8') + salt.encode(encoding='utf_8')).hexdigest()
        return salt, hashed_password
    else:
        hashed_password = str(hashlib.sha512(password.encode(encoding='utf_8') + salt.encode(encoding='utf_8')).hexdigest())
        return hashed_password