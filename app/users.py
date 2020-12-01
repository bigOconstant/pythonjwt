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
        #GetUserForUserName
        returnedUser = DatabaseFactory().GetDataBase().GetUserForUserName(uname)
        self.id = returnedUser["id"]
        self.username = returnedUser["username"]
        self.email = returnedUser["email"]
        
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
