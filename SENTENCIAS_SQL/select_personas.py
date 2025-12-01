#Seleccionar registros desde python a mysql

import mysql.connector

personas_db = mysql.connector.connect(
    host="localhost", #127.0.0.1
    user="root",
    password ="admin",
    database="personas_db",
    charset='utf8'
)

#ejecutar la sentencia select
cursor = personas_db.cursor()
cursor.execute("SELECT * FROM personas");
resultado = cursor.fetchall()
for persona in resultado:
    print(persona)

cursor.close()
personas_db.close()