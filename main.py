from flask import Flask, render_template, request

app = Flask(__name__)

# ======================================
# PÁGINA PRINCIPAL
# ======================================
@app.route('/')
def inicio():
    return render_template('index.html')


# ======================================
# EJERCICIO 1
# ======================================
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():

    promedio = 0
    estado = ""

    if request.method == 'POST':

        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        # Calcular promedio
        promedio = (nota1 + nota2 + nota3) / 3

        # Validar aprobación
        if promedio >= 40 and asistencia >= 75:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"

    return render_template(
        'ejercicio1.html',
        promedio=promedio,
        estado=estado
    )


# ======================================
# EJERCICIO 2
# ======================================
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():

    nombre_mayor = ""
    cantidad = 0

    if request.method == 'POST':

        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        nombres = [nombre1, nombre2, nombre3]

        # Obtener nombre más largo
        nombre_mayor = max(nombres, key=len)

        # Cantidad de caracteres
        cantidad = len(nombre_mayor)

    return render_template(
        'ejercicio2.html',
        nombre_mayor=nombre_mayor,
        cantidad=cantidad
    )


# ======================================
# EJECUTAR APP
# ======================================
if __name__ == '__main__':
    app.run(debug=True)
