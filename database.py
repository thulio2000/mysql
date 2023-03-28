import mysql.connector

config = { #configuration details needed to connect to the mysql db server
    'user': 'root',
    'password': 'q0fmUEe16wNq)~2G',
    'host': 'localhost',
    'database': 'capsule2'
}

db = mysql.connector.connect(**config) #connects to mysql
cursor = db.cursor() #cursor object to execute queries
