#Eliminar registros desde python a mysql
import mysql.connector

personas_db = mysql.connector.connect(
    host="localhost", #127.0.0.1
    user="root",
    password ="admin",
    database="personas_db",
    charset='utf8'
)

#ejecutar la sentencia delete
cursor = personas_db.cursor()
sentencia_sql = 'DELETE FROM personas WHERE id=%s'
valores =(3,)
cursor.execute(sentencia_sql, valores)
personas_db.commit()
print(f"Se ha eliminado del registro")
cursor.close()
personas_db.close()