# app/app.py
"""
Este módulo define una aplicación Flask simple que actúa como una calculadora.
Proporciona operaciones de suma, resta, multiplicación y división.
"""

import os
from flask import Flask, render_template, request
from .calculadora import sumar, restar, multiplicar, dividir

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """Maneja las solicitudes GET y POST para realizar operaciones
    de cálculo y renderizar el resultado."""
    resultado = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operacion = request.form["operacion"]

            if operacion == "sumar":
                resultado = sumar(num1, num2)
            elif operacion == "restar":
                resultado = restar(num1, num2)
            elif operacion == "multiplicar":
                resultado = multiplicar(num1, num2)
            elif operacion == "dividir":
                resultado = dividir(num1, num2)
            else:
                resultado = "Operación no válida"
        except ValueError:
            resultado = "Error: Introduce números válidos"
        except ZeroDivisionError:
            resultado = "Error: No se puede dividir por cero!"

    return render_template("index.html", resultado=resultado)


@app.route("/health")
def health():
    """Verifica la salud de la aplicación."""
    return "OK", 200


if __name__ == "__main__":  # pragma: no cover
    # Quita debug=True para producción
    app_port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, port=app_port, host="0.0.0.0")
