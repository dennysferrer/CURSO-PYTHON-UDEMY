from usuarios import conexionDB

cursor = conexionDB.cursor
database = conexionDB.database

class Nota:

    def __init__(self, usuario_id, titulo, description):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.description = description

    def guardar(self):
        sql = "INSERT INTO notas VALUES (NULL, %s, %s, %s, NOW())"
        nota = (self.usuario_id, self.titulo, self.description)

        try:
            cursor.execute(sql, nota)
            database.commit()
            return [cursor.rowcount, self]
        except Exception as e:
            print(e)
            print("Error al guardar nota ...")

    def listar(self):
        sql = f"SELECT * FROM notas WHERE usuario_id = {self.usuario_id}"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
            print("Error en la consulta de las notas ...")

    def eliminar(self, titulo):
        sql = f"DELETE FROM notas WHERE usuario_id = {self.usuario_id} AND titulo LIKE '%{titulo}%'"
        try:
            cursor.execute(sql)
            database.commit()
            return [cursor.rowcount, self]
        except Exception as e:
            print(e)
            print("Error al borrar la nota ...")