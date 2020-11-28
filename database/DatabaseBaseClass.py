class DatabaseBaseClass:
    def InitUserTable(self):
        print("Initializing User Table")

    def InitUserDatabase(self):
        print("Initializing user Database")

    def InitializeDatabase(self):
        
        print("Initilizing Database")
        
instance = DatabaseBaseClass()

instance.InitUserDatabase()