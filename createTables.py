import sqlite3
import datetime
from datetime import timedelta
con = sqlite3.connect('users.db')
c = con.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER NOT NULL PRIMARY KEY, date text, username text, password text, email text)''')

c.execute('''CREATE TABLE IF NOT EXISTS tokens
(id INTEGER NOT NULL PRIMARY KEY, creationdate text, expirationdate text, token text, userid INTEGER NOT NULL)''')

td = timedelta(days=4)
data_tuple = (datetime.datetime.utcnow(), datetime.datetime.utcnow()+ td, "secretToken",1)

sqlite_insert_with_param = """INSERT INTO 'tokens'
                          ('creationdate', 'expirationdate', 'token','userid') 
                          VALUES (?, ?, ?,?);"""
c.execute(sqlite_insert_with_param, data_tuple)
con.commit()
c.close()