import psycopg2
import hashlib
import uuid
from get_props import prop
import logging
from password import hash_password

password = 'tuppence'
salt = '1e2dfa5c10d8494781260083d09cc1e5'
dbpassword='f92e1acd78d6cdb7266a21ab72967c1dbe834202e0bdcd9a09a4a5d3ce82cee5c64761c04a780d04b8c06c938c1a232fea9d411c1a2b2c5582c7507d6410e2cb'
dbsalt = '1e2dfa5c10d8494781260083d09cc1e5'


logging.debug('username/password to check is %s' % (password))
if dbpassword is not None:
    test = hash_password(password, dbsalt)
    logging.debug('test password hash %s' % test)
    if test == dbpassword:
        logging.debug('password correct')
        print('True')
    else: 
        logging.debug('password incorrect')
        print('False')
else:
    print('False')

    
    #f92e1acd78d6cdb7266a21ab72967c1dbe834202e0bdcd9a09a4a5d3ce82cee5c64761c04a780d04b8c06c938c1a232fea9d411c1a2b2c5582c7507d6410e2cb