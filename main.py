import bcrypt

password = b"super secret password"

hashed = bcrypt.hashpw(password, bcrypt.gensalt())
hashed2 = bcrypt.hashpw(password,bcrypt.gensalt())

print(hashed)

if bcrypt.checkpw(password, hashed):
    print("It Matches!")
else:
    print("It Does not Match :(")

if bcrypt.checkpw(password, hashed2):
    print("It Matches!")
else:
    print("It Does not Match :(")