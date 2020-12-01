from app.connection import GetConnection
import bcrypt
import datetime
from datetime import timedelta
from datetime import date
from typing import NewType
from json import dumps

from app.database.DatabaseBaseClass import DatabaseFactory


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
    return DatabaseFactory().GetDataBase().UserExist(username)
    
def CreateUser(username,password,email):
    hashval = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    DatabaseFactory().GetDataBase().CreateUser(username,hashval,email)
    return True

def PasswordMatchesForUser(username: str,password: str) ->bool:
    hashedpassword = DatabaseFactory().GetDataBase().GetPasswordForUser(username)
    if bcrypt.checkpw(password.encode('utf-8'), hashedpassword):
            return True
    return False
