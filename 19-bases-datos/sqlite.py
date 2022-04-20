#Importa modulo sqlite3
import sqlite3

#Hacer conexión a la base de datos
conexion = sqlite3.connect('pruebas.db')

#Crear cursor
cursor = conexion.cursor()

#Crear tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"id INTEGER PRIMARY KEY AUTOINCREMENT, "+
"titulo VARCHAR(255), "+
"description TEXT, "+
"precio INT(255)"
")")

#Guardar cambios
conexion.commit()

# Borrar registro de una tabla
cursor.execute("DELETE FROM productos")
conexion.commit()

#Insertar datos
"""
cursor.execute("INSERT INTO productos VALUES(null, 'Producto1', 'Lenovo Ideapad 720s',2500)")
conexion.commit()
"""

#Insertar muchos pruductos
productos = [
    ("Telefono movil", "Sony Xperia", 2500),
    ("Computador Portatil", "Lenovo Ideapad", 1800),
    ("Televisor 60", "LG TV 60", 1670),
    ("Tablet", "Xiomi pad 5",900)
]
cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)
conexion.commit()

#Leer datos de una base de datos
cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()

for producto in productos:
    print(producto)



#Cerrar conexión a la base de datos
conexion.close()



