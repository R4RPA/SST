import sqlite3

# connect to database (creates a new one if it doesn't exist)
conn = sqlite3.connect('../Database/example.db')

# create a cursor to execute SQL commands
c = conn.cursor()

# create table
c.execute('''CREATE TABLE ScriptInfo
             (ID INTEGER PRIMARY KEY AUTOINCREMENT,
              Department TEXT,
              Software TEXT,
              ScriptName TEXT,
              ShortDescription TEXT,
              Functionalities TEXT,
              Features TEXT,
              KeyWords TEXT,
              Owner TEXT,
              Created_On DATETIME,
              Edited_On DATETIME,
              Deleted_On DATETIME)''')

# commit changes and close connection
conn.commit()
conn.close()
