import bcrypt
from users import CreateUser,userExist,PasswordMatchesForUser

def testthing(name: str)->str:
    return "hello world"

print(userExist("andrew"))

print(PasswordMatchesForUser("andrew","rabbit"))

print(PasswordMatchesForUser("andrew","rabbit2"))



print(PasswordMatchesForUser("sarahwang","sarahwang123"))

print(PasswordMatchesForUser("sarahwang","sarahwang1234"))



