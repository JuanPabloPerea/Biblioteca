from flask import Flask, render_template, request, redirect, url_for,session,flash
import conexion

app = Flask(__name__)

app.secret_key = "ja"
"""
class User:
    def __init__(self, id, password):
        self.id = id
        self.password = password
    def __repr__(self):
        return f'<USer: {self.id}>'

users = []
users.append(User(id=1,password="pass"))
"""

#aqui se verifica las casillas tengan algo, para eso usamos el metodo post y el metodo get
#y se redirecciona con el metodo urldirect

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == "POST" :
        user = request.form['usu']
        pas = request.form['pass']
        aux = []
        if conexion.validarUsuario(user,pas,aux) == 0:
            return render_template('Inicio.html')
        else:
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
def Sesion():
    return render_template("Sesion.html")

@app.route('/misLibros', methods=['POST','GET'])
def libros():
    return render_template("Libros.html")

@app.route('/sacarLibros', methods=['POST','GET'])
def Prestamo():
    return render_template("Prestamo.html")

if __name__ == '__main__':
    app.run()
