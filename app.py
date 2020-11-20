from flask import Flask,request
import json
import requests
from users import userExist, PasswordMatchesForUser,User,CreateUser
from jwtoken import CreateTokenForUser,GetTokenFromTokenId
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1 style='text-align: center;'>Welcome to the User Service.</h1>"

@app.route('/login', methods=['POST']) #GET requests will be blocked
def login():
    req_data = request.get_json()
    print(req_data)
    password = req_data['password']
    username = req_data['username']
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
def register():
    req_data = request.get_json()
    response = {"success":False,"message":"username already in use"}
    password = req_data['password']
    username = req_data['username']
    email = req_data['email']

    if userExist(username):
        return json.dumps(response)

    success = CreateUser(username,password,email)

    if success:
        response = {"success":True,"message":"User Created Successfully"}
    else:
        response = {"success":False,"message":"Error Creating User"}
    return json.dumps(response)

    