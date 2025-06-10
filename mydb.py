import mysql.connector
database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'harsha2001',
)

# prepare a cursor
cursorObject = database.cursor()

# create a databse
cursorObject.execute('CREATE DATABASE mydb')
print('Done')