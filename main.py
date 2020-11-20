import bcrypt
from jwtoken import CreateTokenForUser,GetTokenFromTokenId,GetUserFromToken
from users import CreateUser,userExist,PasswordMatchesForUser,User



print(userExist("andrew"))


#CreateUser(username,password,email):


usr = User()
username = input("Enter your new username: ")
password = input("enter your new password: ")
email = input("enter your new emailaddress: ")

if not userExist(username):
    CreateUser(username,password,email);

usr.SetUser(username)
print(usr.id)
tokenId = CreateTokenForUser(usr)
print("token created:"+str(tokenId))

token = GetTokenFromTokenId(str(tokenId))

print(token)
print(GetUserFromToken(token).email)

print(PasswordMatchesForUser(username,"test"))

print(PasswordMatchesForUser(username,password))



