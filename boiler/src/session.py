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
    d = os.listdir(sessionDir)
    try:
        for f in d: 
        
            #t = int(os.path.getmtime('%s%s' % (sessionDir, sessionid)))
            t = int(os.path.getmtime('%s%s' % (sessionDir, f)))
            ct = calendar.timegm(time.gmtime())
            if ct - t > 1800:
                os.remove('%s%s' % (sessionDir, f))
    except Exception as e:
        print(e)
        pass
    try:
        sessions = os.listdir(sessionDir)
        if sessionid in sessions:
                file = '%s%s' % (sessionDir, sessionid)
                open(file, 'w').close
                return True
    except:
            return False
        
def get_sessionid():
    pysessionid = hashlib.md5(os.urandom(512)).hexdigest()
    return pysessionid