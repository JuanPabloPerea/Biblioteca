from flask import Flask, render_template, request,flash
import mysql.connector as conn
import conexion

app = Flask(__name__)

app.secret_key = "ja"
user_id = []
aux = ""
"""
class User:
    def __init__(self, id, password):
        self.id = id
        self.password = password
    def __repr__(self):
        return f'<USer: {self.id}>'

users = []
users.append(User())
"""

#aqui se verifica las casillas tengan algo, para eso usamos el metodo post y el metodo get
#y se redirecciona con el metodo urldirect

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == "POST" :
        user = request.form['usu']
        pas = request.form['pass']
        if conexion.validarUsuario(user,pas) == 0:
            return render_template('NuevoUsuario.html')
        else:
            user_id.append(user)
            print(user_id[0])
            return render_template('Sesion.html')
    else:
        return render_template('Inicio.html')

@app.route('/registro', methods=['POST','GET'])
def registrarse():
    if request.method == "POST":
        id = request.form['nueUsu']
        user = request.form['nomUsu']
        apellido = request.form['apeUsu']
        edad = request.form['edadUsu']
        tel = request.form['telUsu']
        password = request.form['passUsu']
        confir = request.form['passUsu2']
        if password == confir:
            conexion.registrarUsu(id,confir,user,apellido,edad,tel)
            return (render_template('Inicio.html'))
        else:
            flash("la clave y la contraseña no coinciden")
            return render_template('NuevoUsuario.html')
    else:
        return render_template('NuevoUsuario.html')

@app.route('/dashboard')
def sesion():
    print(user_id)
    return render_template("Sesion.html")

@app.route('/libros', methods=['POST','GET'])
def devolucion():
    if request.method == "POST":
        id = request.form['id']
        usuario = user_id[0]
        conexion.devolverLibro(id, usuario)
        return render_template("Sesion.html")
    else:
        usuario = user_id[0]
        user = "root"
        password = "abc123"
        database = "BiblioUd"
        prueba = conn.connect(host='localhost', port='3306',
                              user=user, password=password, database=database)
        cursor = prueba.cursor()
        dato = (int(usuario),)

        sql = "select id,nombreLibro, autor, descripcion from (select id_libro,cedula_Usuario from Prestamo where cedula_Usuario = (%s)) as pres " \
              "inner join Libro on pres.id_libro = Libro.id "
        try:
            cursor.execute(sql, dato)
            aux = cursor.fetchall()
            return render_template("Libros.html", prests=aux)
        except prueba.error as error:
            print("Error: {}".format(error))
        prueba.close()


@app.route('/sacarLibros', methods=['POST', 'GET'])
def prestamo():
    print(user_id)
    if request.method == "POST":
        id = request.form['id']
        usuario = user_id[0]
        conexion.pedirLibro(id,usuario)
        return render_template("Sesion.html")
    else:
        user = "root"
        password = "abc123"
        database = "BiblioUd"
        prueba = conn.connect(host='localhost', port='3306',
                          user=user, password=password, database=database)
        cursor = prueba.cursor()
        sql = "select id,nombreLibro, autor, descripcion from Libro"
        try:
            cursor.execute(sql)
            aux = cursor.fetchall()
            return render_template("Prestamo.html", libros=aux)
        except prueba.error as error:
            print("Error: {}".format(error))
        prueba.close()

if __name__ == '__main__':
    app.run()
