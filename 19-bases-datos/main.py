import mysql.connector

# Conexión a la base de datos

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "master_python"
)

mycursor = database.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS master_python")
mycursor.execute("SHOW DATABASES")

for bd in mycursor:
    print(bd)

# Crear Tablas

mycursor.execute("CREATE TABLE IF NOT EXISTS customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("SHOW TABLES")

for table in mycursor:
    print(table)