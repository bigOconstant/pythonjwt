# from flask import Flask,request
import json
import uvicorn
import requests
from users import userExist, PasswordMatchesForUser,User,CreateUser
from jwtoken import CreateTokenForUser,GetTokenFromTokenId
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

class UserLogin(BaseModel):
    username: str
    password: str

class UserRegister(BaseModel):
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

@app.route('/register', methods=['POST']) #GET requests will be blocked
async def register(usr: UserRegister):
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

#
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)