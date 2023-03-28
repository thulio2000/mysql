import mysql.connector
from mysql.connector import errorcode
from database import cursor

DB_NAME = 'capsule2'

TABLES = {}

TABLES['logs'] = (  # schema for the logs table
    "CREATE TABLE `logs` ("
    "`id` int(11) NOT NULL AUTO_INCREMENT,"
    "`text` varchar(250) NOT NULL,"
    "`user` varchar(250) NOT NULL,"
    "`created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    "PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB"
)


def create_database():  # creates database using cursor.execute
    cursor.execute(
        "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    print("Database {} created!".format(DB_NAME))


def create_tables():  # uses cursor.execute to create each table in the dictionary
    cursor.execute("USE {}".format(DB_NAME))

    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table ({}) ".format(table_name), end="")
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Already Exists")
            else:
                print(err.msg)


create_database()
create_tables()
