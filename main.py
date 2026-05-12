from flask import Flask, render_template

app = Flask(__name__)

# Página principal
@app.route('/')
def inicio():
    return render_template('index.html')

# Ejercicio 1
@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html')

# Ejercicio 2
@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)