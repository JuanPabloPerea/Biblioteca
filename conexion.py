import mysql.connector as conn
from datetime import timedelta, datetime
user = "root"
password = "abc123"
database = "BiblioUd"

# funcion de pedir un libro
def pedirLibro(idlibro , cedula):

    # funciones par sacar la fechas y darles el fromato necesario para subirlas a mysql

    now = datetime.now()
    pres = now + timedelta(days=24)
    today = datetime.strftime(now, '%Y/%m/%d')
    prestamo = datetime.strftime(pres, "%Y/%m/%d")
    # se hace la conexion a la base de datos

    prueba = conn.connect(host='localhost', port='3306',
                          user=user, password=password, database=database)
    cursor = prueba.cursor()
    # se crean lo querys necesarios, se hace de esta forma para evitar
    # el error de los datos no tiene formato valido

    dato = (9,today,prestamo,0,cedula,idlibro,0)
    sql1 = "insert into Prestamo (Id,fechaPrestamo, fechaEntrega,multa,cedula_usuario,id_libro,devuelto)"\
           "values (%s,%s,%s,%s,%s,%s,%s)"
    libro = (idlibro,)
    sql2 = "update Libro set prestadas = prestadas + 1 where id = (%s) "
    try:
        cursor.execute(sql1, dato)
        cursor.execute(sql2, libro)
        prueba.commit()
    except prueba.error as error:
        print("Error: {}".format(error))
    prueba.close()

def devolverLibro (idlibro, cedula ):
    prueba = conn.connect(host='localhost', port='3306',
                          user=user, password=password, database=database)
    cursor = prueba.cursor()
    devolucion = (cedula, idlibro)
    sql1 = "update Prestamo set devuelto = 1 where cedula_Usuario = (%s) and id_libro = (%s)"
    libro = (idlibro,)
    sql2 = "update Libro set prestadas = prestadas - 1 where id = (%s) "
    try:
        cursor.execute(sql1, devolucion)
        cursor.execute(sql2, libro)
        prueba.commit()
    except prueba.error as error:
        print("Error: {}".format(error))
    prueba.close()

def registrarUsu (cedula,passw,nombre,apellido,edad,celular):
    prueba = conn.connect(host='localhost', port='3306',
                          user=user, password=password, database=database)
    cursor = prueba.cursor()
    datos = (cedula,passw,nombre,apellido,edad,celular)
    sql = "insert into Usuario (cedula,password,nombre,apellido,edad,celular)"\
          "values (%s,%s,%s,%s,%s,%s)"
    try:
        cursor.execute(sql, datos)
        prueba.commit()
    except prueba.error as error:
        print("Error: {}".format(error))
    prueba.close()

def validarUsuario (cedula, passw):
    prueba = conn.connect(host='localhost', port='3306',
                          user=user, password=password, database=database)
    cursor = prueba.cursor()
    datos = (cedula, passw)
    sql = "select * from Usuario where cedula = (%s) " \
          "and password = (%s)"
    try:
        cursor.execute(sql, datos)
        for i in cursor:
            print (i)
    except prueba.error as error:
        print("Error: {}".format(error))
    prueba.close()

validarUsuario(40979866,"cba213")
"""
def eliminar ():
    prueba = conn.connect(host='localhost', port='3306',
                          user=user, password=password, database=database)
    cursor = prueba.cursor()
    sql = "delete from Usuario where cedula = 1026595374"
    try:
        cursor.execute(sql)
        prueba.commit()
    except prueba.error as error:
        print("Error: {}".format(error))
    prueba.close()
eliminar()
"""