import mysql.connector

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "thinkerdafy1988",
    database = "master_python",
    port = 3306
)

cursor = database.cursor(buffered = True)

  
