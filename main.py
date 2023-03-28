from database import cursor, db


def add_log(text, user):  # inserts a new record into the logs table with the given text and user values.
    sql = ("INSERT INTO logs(text, user) VALUES (%s, %s)")
    cursor.execute(sql, (text, user))
    db.commit()
    log_id = cursor.lastrowid
    print("Added log {}".format(log_id))


def get_logs():  # selects all the records from the logs table in the connected database
    sql = ("SELECT * FROM logs ORDER BY created DESC")
    cursor.execute(sql)
    result = cursor.fetchall()

    for row in result:
        print(row)


def get_log(id):  # This function selects a single record from the logs table where the id matches the given argument
    sql = ("SELECT * FROM logs WHERE id = %s")
    cursor.execute(sql, (id,))
    result = cursor.fetchone()

    for row in result:
        print(row)


def update_log(id, text): #This function updates the text column of a record in the logs table where the id column matches the argument
    sql = ("UPDATE logs SET text = %s WHERE id = %s")
    cursor.execute(sql, (text, id))
    db.commit()
    print("Log updated")


def delete_log(id): #This function deletes a record from the logs table where the id column matches the given argument
    sql = ("DELETE FROM logs WHERE id = %s")
    cursor.execute(sql, (id,))
    db.commit()
    print("Log removed")


"""add_log("This is log one", "Lucas")
add_log("This is log two", "Taichi")
add_log("This is log three", "Hikari")"""

# get_logs() #gets all logs in an array
# get_log(2) #gets the log from the inserted id
# update_log(2, 'Updated log successfully') #updates log with the string inserted

delete_log(2)
get_logs()
