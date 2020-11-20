import bcrypt
from jwtoken import CreateTokenForUser,GetTokenFromTokenId,GetUserFromToken
from users import CreateUser,userExist,PasswordMatchesForUser,User

def testthing(name: str)->str:
    return "hello world"

print(userExist("andrew"))


usr = User()
usr.SetUser("sarahwang")
print(usr.id)
tokenId = CreateTokenForUser(usr)
print("token created:"+str(tokenId))

token = GetTokenFromTokenId(str(tokenId))

print(token)
print(GetUserFromToken(token).email)

print(PasswordMatchesForUser("sarahwang","sarahwang123"))

print(PasswordMatchesForUser("sarahwang","sarahwang1234"))



