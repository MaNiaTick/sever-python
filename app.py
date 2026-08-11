from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/saludar", methods=["GET"])
def saludar():
    # Retorna un JSON con las palabras solicitadas
    return jsonify({"mensaje": ["saludo", "hola"]})


if __name__ == "__main__":
    # Ejecuta el servidor en modo debug en el puerto 5000
    app.run(debug=True, port=5000)