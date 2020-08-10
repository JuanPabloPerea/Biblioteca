import mysql.connector as prueba

mariadb_conexion = prueba.connect(host='localhost', port='3306',
                                  user='root', password='abc123', database='miprueba')

cursor = mariadb_conexion.cursor()
try:
    cursor.execute("SELECT ID,NOMBRE FROM Usuarios")

except prueba.error as error:
    print("Error: {}".format(error))
mariadb_conexion.close()

