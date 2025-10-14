# Se crea una aplicación Flask
from flask import Flask, jsonify, request
import time

app = Flask(__name__)

# Simulación de una bd
users_db = {
    1: {"id": 1, "name": "Alice", "email": "alice@example.com"},
    2: {"id": 2, "name": "Bob", "email": "bob@example.com"},
    3: {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
}

#ruta de los usuarios get
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Endpoint síncrono para obtener información de un usuario"""
    print(f"🔵 Servidor: Recibida petición para usuario {user_id}")
    
    # Se simula un tiempo de procesamiento
    time.sleep(2)  # 2 segundos de "procesamiento"
    
    # Se busca el usuario por su id
    user = users_db.get(user_id)
    if user:
        print(f"🟢 Servidor: Enviando respuesta para usuario {user_id}")
        return jsonify({"status": "success", "data": user})
    else:
        print(f"🔴 Servidor: Usuario {user_id} no encontrado")
        return jsonify({"status": "error", "message": "User not found"}), 404

#ruta de los usuarios post
@app.route('/api/users', methods=['POST'])
def create_user():
    """Endpoint síncrono para crear un usuario"""
    print("🔵 Servidor: Recibida petición para crear usuario")
    
    # Se obtiene la información enviada por el cliente
    data = request.get_json()
    
    
    # Se valida que los campos necesarios estén presentes
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"status": "error", "message": "Missing required fields"}), 400
    
    # Se simula un tiempo de procesamiento
    time.sleep(1)
    
    # Se genera un nuevo id para el usuario
    new_id = max(users_db.keys()) + 1
    
    # Se crea el nuevo usuario
    new_user = {
        "id": new_id,
        "name": data['name'],
        "email": data['email']
    }
    
    # Se agrega el nuevo usuario a la base de datos simulada
    users_db[new_id] = new_user
    
    print(f"🟢 Servidor: Usuario {new_id} creado exitosamente")
    return jsonify({"status": "success", "data": new_user}), 201

if __name__ == '__main__':
    print("🚀 Iniciando servidor síncrono en http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
