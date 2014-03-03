import os
import calendar
import time
from get_props import prop
import hashlib

def set_session(sessionid):
    sessionDir = prop('sessionDir')[0]
    file = '%s%s' % (sessionDir, sessionid)
    open(file, 'a').close()

def check_session(sessionid):
    sessionDir = prop('sessionDir')[0]
    sessions = os.listdir(sessionDir)
    t = int(os.path.getmtime('%s%s' % (sessionDir, sessionid)))
    ct = calendar.timegm(time.gmtime())
    if ct - t > 1800:
        os.remove('%s%s' % (sessionDir, sessionid))
    if sessionid in sessions:
        file = '%s%s' % (sessionDir, sessionid)
        open(file, 'w').close
        return True
    else:
        return False
    
def get_sessionid():
    pysessionid = hashlib.md5(os.urandom(512)).hexdigest()
    return pysessionid