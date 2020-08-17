import mysql.connector as prueba

prueba = prueba.connect(host='localhost', port='3306',
                                  user='root', password='abc123', database='BibliUd')

cursor = prueba.cursor()

try:
    cursor.execute("SELECT ID,NOMBRE FROM Usuarios")

except prueba.error as error:
    print("Error: {}".format(error))
prueba.close()

