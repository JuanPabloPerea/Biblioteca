from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("Inicio.html")

@app.route('/registro')
def index():
    return render_template("NuevoUsuario.html")

@app.route('/dashboard')
def dash():
    return render_template("Sesion.html")

@app.route('/misLibros')
def misLibros():
    return render_template("Libros.html")

@app.route('/sacarLibros')
def prestamo():
    return render_template("Prestamo.html")

if __name__ == '__main__':
    app.run()
