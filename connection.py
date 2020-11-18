import sqlite3

def GetConnection():
    con = sqlite3.connect('users.db')
    return con