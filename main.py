from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/registro',)
def registro():
    return render_template('registro.html')

@app.route('/inicio', methods=['POST'])
def inicio():
    if request.method == 'POST':
        usuario= request.form['user']
        contraseña= request.form['contraseña']
    return render_template('inicio.html')

@app.route('/misLibros')
def misLibros():
    return render_template('misLibros.html')

@app.route('/buscar')
def buscar():
    return render_template('buscar.html')

if __name__ == "__main__":
    app.run(debug=True)
