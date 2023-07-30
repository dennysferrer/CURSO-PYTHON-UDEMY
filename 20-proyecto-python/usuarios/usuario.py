import datetime
import hashlib
from usuarios import conexionDB

cursor = conexionDB.cursor
database = conexionDB.database

class Usuario:

    def __init__(self, nombre, apellido, email, password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password
    
    def registrar(self):
        fecha = datetime.datetime.now()

        #Cifrar password
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf-8'))

        sql = "INSERT INTO usuarios VALUES (NULL, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellido, self.email, cifrado.hexdigest(), fecha)
        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        
        except:
            result = [0, self]
        
        return result


    def identificar(self):
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"

        # Cifrar password
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf-8'))

        usuario = (self.email, cifrado.hexdigest())

        try:
            cursor.execute(sql, usuario)
            result = cursor.fetchone()
            return result
        except Exception as e:
            print(e)
            print("Error en la consulta de los datos ...")

