from app.connection import GetConnection
import bcrypt
import datetime
from datetime import timedelta
from datetime import date
from typing import NewType
from json import dumps

class User:
    id = 0
    username = ""
    email = ""
    
    def ToDict(self):
        return {"username":self.username,"email":self.email,"id":self.id  }
    
    def SetUser(self,uname):
        con = GetConnection()
        cursor = con.cursor()
        sqlite_get_with_param = "SELECT id,email FROM users where username = :username ;"
        cursor.execute(sqlite_get_with_param, {"username":uname})
        rows = cursor.fetchall()
        length = len(rows)
        if(length > 0):
            self.id = rows[0][0]
            self.username = uname
            self.email = rows[0][1]
        
def userExist(username)-> bool:
    con = GetConnection()
    cursor = con.cursor()
    sqlite_insert_with_param = "SELECT id FROM users where username = :username ;"
    cursor.execute(sqlite_insert_with_param, {"username":username})
    rows = cursor.fetchall()
    length = len(rows)
    cursor.close()
    if length == 0:
        return False
    else:
        return True
    
def CreateUser(username,password,email):
    hashval = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    user = (username,hashval,email,datetime.datetime.utcnow())
    con = GetConnection()
    cursor = con.cursor()
    sqlite_insert_with_param = "INSERT INTO users (username,password,email,date) VALUES(?, ?, ?, ?)"
    cursor.execute(sqlite_insert_with_param, user)
    con.commit()
    cursor.close()
    return True

def PasswordMatchesForUser(username: str,password: str) ->bool:
    con = GetConnection()
    cursor = con.cursor()
    sqlite_insert_with_param = "SELECT password FROM users where username = :username ;"
    cursor.execute(sqlite_insert_with_param, {"username":username})
    rows = cursor.fetchall()
    length = len(rows)
    if(length > 0):
        hashed = rows[0][0]
        if bcrypt.checkpw(password.encode('utf-8'), hashed):
            return True
   
    return False
