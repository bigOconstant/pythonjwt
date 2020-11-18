import jwt
from connection import GetConnection
from users import User
from json import dumps
import datetime
from datetime import timedelta
from datetime import date

def myconverter(o): # used to serialise datetime
    if isinstance(o, datetime.datetime):
        return o.__str__()

def CreateTokenForUser(usr: User):
    userobj = usr.ToDict()
    timeNow = datetime.datetime.utcnow()
    expireTime = timeNow+datetime.timedelta(days=5) # set it to expire in 5 days
    userobj['time'] = dumps(timeNow,default=myconverter) # add a time stamp so each token is unique
    encoded_jwt = jwt.encode(userobj, 'secret', algorithm='HS256')
    row = (timeNow,expireTime,encoded_jwt,usr.id)
    con = GetConnection()
    cursor = con.cursor()
    sqlite_insert_with_param = "INSERT INTO tokens (creationdate,expirationdate,token,userid) VALUES(?, ?, ?, ?)"
    cursor.execute(sqlite_insert_with_param, row)
    con.commit()
    rowid =  cursor.lastrowid
    cursor.close()
    return rowid
    