from flask import Flask, request, jsonify

app = Flask(__name__)

# Almacena la última lectura recibida
ultimo_dato = {}

@app.route('/')
def index():
    return "<h2>Servidor Central Activo</h2><p>Esperando datos...</p>"

@app.route('/data', methods=['POST'])
def recibir():
    global ultimo_dato
    ultimo_dato = request.json
    print("Dato recibido:", ultimo_dato)
    return jsonify({"status": "OK"}), 200

@app.route('/status')
def status():
    return jsonify(ultimo_dato)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
