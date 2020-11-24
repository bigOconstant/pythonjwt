# from flask import Flask,request
import json
import os
import uvicorn

curdir = os.getcwd()
print(curdir)
from app.users import userExist, PasswordMatchesForUser,User,CreateUser
from app.jwtoken import CreateTokenForUser,GetTokenFromTokenId,GetUserFromToken
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path

my_file = Path("user.db")

if not my_file.is_file():
    curdir = os.getcwd()
    print(curdir)
    exec(open(curdir+'/app/createTables.py').read())

class UserLogin(BaseModel):
    username: str
    password: str

class UserCreate(BaseModel):
    username: str
    password: str
    email: str
    
app = FastAPI()

@app.get("/")
async def root():
    return "Welcome to the User Service."

@app.post("/login/")
async def login(usr: UserLogin):
    # req_data = request.get_json()\
    print("hit login")
    password = usr.password
    username = usr.username
    response = {"success":False,"message":"user does not exist","token":""}

    if not userExist(username):
        return json.dumps(response)

    if not PasswordMatchesForUser(username,password):
        response = {"success":False,"message":"password incorrect","token":""}
        return json.dumps(response)
    
    usr = User()
    usr.SetUser(username)
    tokenid = CreateTokenForUser(usr)
    tokenString = GetTokenFromTokenId(tokenid)
    response = {"success":True,"message":"success","token":tokenString}
    return json.dumps(response)

@app.post("/register")
async def register(usr: UserCreate):
    response = {"success":False,"message":"username already in use"}
    password = usr.password
    username = usr.username
    
    email = usr.email

    if userExist(username):
        return json.dumps(response)

    success = CreateUser(username,password,email)

    if success:
        response = {"success":True,"message":"User Created Successfully"}
    else:
        response = {"success":False,"message":"Error Creating User"}
    return json.dumps(response)


@app.get("/user")
async def GetUser(token: str = ""):
    if (token == ""):
         returnVal = {"success":False}
    
    usr = GetUserFromToken(token)
    if usr.id <1:
        return {"success":False}
    else:
        returnVal = {"username":usr.username,"email":usr.email,"id":usr.id,"success":True}
        return returnVal
#
    

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=5000)
