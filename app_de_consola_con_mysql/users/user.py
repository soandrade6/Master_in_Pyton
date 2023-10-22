import users.connection as connection
import datetime
import hashlib #To encrypt passwords

connect = connection.connect()
database = connect[0]
cursor = connect[1]

class User:

    def __init__(self, name, last_name, email, password):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password

    def sign_up(self):
        date = datetime.datetime.now()

        #Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))


        sql = "INSERT INTO users VALUES(null, %s, %s, %s, %s, %s)"
        user = (self.name, self.last_name, self.email, cifrado.hexdigest(), date)

        try:
            cursor.execute(sql, user)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result

    def log_in(self):
        # consulta para consulta si existe el usuario
        sql = "SELECT * FROM users WHERE email = %s AND password = %s"

        #Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        #Datos para la consulta
        user = (self.email, cifrado.hexdigest())

        cursor.execute(sql, user)
        result = cursor.fetchone()

        return result