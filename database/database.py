import psycopg2


class DataBase:
    def __init__(self,db:str, user:str,password:str,host:str,port:str):
        self.db = db
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        

    def GetConnection(self):
        return psycopg2.connect(database=self.db, user=self.user, password=self.password, host=self.host, port=self.port)

    def InitUserTable(self):
        print("inituser tables")
        con = psycopg2.connect(database=self.db, user=self.user, password=self.password, host=self.host, port=self.port)
        cur = con.cursor()
        cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
        rows = cur.fetchall()
        userTableFound = False
        for row in rows:
            print(row[0])
            if row[0] == "users":
                 userTableFound = True
        
        if not userTableFound:
            print("creating users table")
            fd = open('app/sqlfiles/CREATEUSERSTABLE.sql', 'r')
            sqlFile = fd.read()
            cur.execute(sqlFile)

        con.commit()
        con.close()

    def InitUserDatabase(self):
        con = psycopg2.connect(database="postgres", user=self.user, password=self.password, host=self.host, port=self.port)
        con.autocommit = True
        cur = con.cursor()
        cur.execute("SELECT datname FROM pg_database")
        rows = cur.fetchall()
        userdatabaseFound = False
        for row in rows:
            if row[0] == "userdatabase":
                userdatabaseFound = True
        
        if not userdatabaseFound:
            print("Creating user database")
            cur.execute("CREATE DATABASE userdatabase")


        con.close()

    def InialiseDatabase(self):
        print("init database")
        self.InitUserDatabase()
        self.InitUserTable()
            

    def printTables(self):
        print("Printing user table")
        con = self.GetConnection()
        cur = con.cursor()
        cur.execute("SELECT * from users")
        rows = cur.fetchall()

        for row in rows:
            print("id =", row[0])
            print("date =", row[1])
            print("username =", row[2])
            print("email =", row[4])

        con.close()


  