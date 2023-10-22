import mysql.connector
import datetime

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master_python",
    port=3306
)

cursor = database.cursor(buffered=True)

class User:

    def __init__(self, name, last_name, email, password):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password

    def sign_up(self):
        date = datetime.datetime.now()
        sql = "INSERT INTO users VALUES(null, %s, %s, %s, %s, %s)"
        user = (self.name, self.last_name, self.email, self.password, date)

        cursor.execute(sql, user)
        database.commit()

        return [cursor.rowcount, self]

    def log_in(self):
        return self.name