from flask import Flask, jsonify
import random

app = Flask(__name__)


@app.route("/saludar", methods=["GET"])
def saludar():
    return jsonify({"saludo": "Hola!"})

@app.route("/cachipun", methods=["GET"])
def cachipun():
    opciones = ["Piedra","Papel", "Tijera"]
    eleccion = random.choice(opciones)
    return jsonify({"mensaje": eleccion})


if __name__ == "__main__":
    # Ejecuta el servidor en modo debug en el puerto 5000
    app.run(debug=True, port=5000)