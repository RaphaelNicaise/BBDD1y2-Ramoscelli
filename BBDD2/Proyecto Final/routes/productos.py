from flask import Blueprint, jsonify
from bson import ObjectId
from database.conn_database import client_db

productos_bp = Blueprint('productos', __name__)

try:
    productos = client_db["productos"] # Colección de productos en la base de datos
    print("Conexión a la base de datos establecida")
except Exception as e:
    print(f"Error conectando a la base de datos: {e}")

@productos_bp.route('/productos', methods=['GET'])
def get_productos():
    try:
        print("Endpoint /productos llamado")
        productos_list = list(productos.find({}))
        print(f"Se encontraron {len(productos_list)} productos")
        for producto in productos_list:
            producto['_id'] = str(producto['_id'])
            if 'proveedorId' in producto:
                producto['proveedorId'] = str(producto['proveedorId'])
        return jsonify(productos_list), 200
    except Exception as e:
        print(f"Error en get_productos: {e}")
        return jsonify({"error": str(e)}), 500