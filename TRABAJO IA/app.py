from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultados = {}
    intentos = 0

    if request.method == "POST":
        # Ejercicio 1: Aumento de Sueldo
        if 'sueldo' in request.form:
            sueldo = float(request.form['sueldo'])
            if sueldo < 4000:
                aumento = sueldo * 0.15
            else:
                aumento = sueldo * 0.08
            resultados['ejercicio1'] = f'Aumento: S/ {aumento:.2f}'

        # Ejercicio 2: Descuento Parque
        if 'edad' in request.form:
            edad = int(request.form['edad'])
            precio = 50
            if edad < 10:
                descuento = precio * 0.25
                precio_final = precio - descuento
            else:
                precio_final = precio
            resultados['ejercicio2'] = f'Precio a pagar: S/ {precio_final:.2f}'

        # Ejercicio 3: Descuento Tienda
        if 'mes' in request.form and 'importe' in request.form:
            mes = request.form['mes'].lower()
            importe = float(request.form['importe'])
            if mes == "octubre":
                descuento = importe * 0.15
                total = importe - descuento
            else:
                total = importe
            resultados['ejercicio3'] = f'Total a cobrar: S/ {total:.2f}'

        # Ejercicio 4: Validar Número Menor que 10
        if 'numero4' in request.form:
            numero4 = int(request.form['numero4'])
            if numero4 < 10:
                resultados['ejercicio4'] = f'Número correcto: {numero4}'
            else:
                resultados['ejercicio4'] = 'El número debe ser menor que 10'

        # Ejercicio 5: Validar Rango (0, 20)
        if 'numero5' in request.form:
            numero5 = int(request.form['numero5'])
            if 0 < numero5 < 20:
                resultados['ejercicio5'] = f'Número correcto: {numero5}'
            else:
                resultados['ejercicio5'] = 'El número debe estar en el rango (0, 20)'

        # Ejercicio 6: Contar intentos
        if 'numero6' in request.form:
            numero6 = int(request.form['numero6'])
            intentos += 1
            if 0 < numero6 < 20:
                resultados['ejercicio6'] = [f'Número correcto: {numero6}', intentos]
            else:
                resultados['ejercicio6'] = [f'El número debe estar en el rango (0, 20)', intentos]

        # Ejercicio 7: Sumar los primeros n números
        if 'n' in request.form:
            n = int(request.form['n'])
            suma = sum(range(1, n + 1))
            resultados['ejercicio7'] = f'Suma: {suma}'

        # Ejercicio 8: Sumar hasta que se ingrese 0
        if 'numero8' in request.form:
            suma8 = 0
            while True:
                numero8 = int(request.form['numero8'])
                if numero8 == 0:
                    break
                suma8 += numero8
            resultados['ejercicio8'] = f'Suma total: {suma8}'

        # Ejercicio 9: Sumar hasta que la suma sea mayor a 100
        if 'numero9' in request.form:
            suma9 = 0
            while suma9 <= 100:
                numero9 = int(request.form['numero9'])
                suma9 += numero9
            resultados['ejercicio9'] = f'Suma total: {suma9}'

        # Ejercicio 10: Calcular pago por horas
        if 'horas_normales' in request.form and 'horas_extras' in request.form and 'hijos' in request.form:
            horas_normales = int(request.form['horas_normales'])
            horas_extras = int(request.form['horas_extras'])
            hijos = int(request.form['hijos'])
            pago_hora_normal = 10  # Precio por hora normal (por ejemplo)
            pago_hora_extra = pago_hora_normal * 1.5  # Hora extra es 50% más cara
            bono_hijos = hijos * 0.5  # Bono por hijos

            pago_normal = horas_normales * pago_hora_normal
            pago_extra = horas_extras * pago_hora_extra
            pago_total = pago_normal + pago_extra + bono_hijos

            resultados['ejercicio10'] = f'Pago total: S/ {pago_total:.2f}'

    return render_template("index.html", resultados=resultados, intentos=intentos)

if __name__ == "__main__":
    app.run(debug=True)
