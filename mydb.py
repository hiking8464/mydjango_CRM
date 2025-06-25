import mysql.connector
from decouple import config


host = config('MYSQL_HOST')
root = config('MYSQL_USER')
password = config('MYSQL_PASSWORD')
database = mysql.connector.connect(
    host = host,
    user = root,
    passwd = password,
)

# prepare a cursor
cursorObject = database.cursor()

# create a databse
cursorObject.execute('CREATE DATABASE mydb')
print('Done')