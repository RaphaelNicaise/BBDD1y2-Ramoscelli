from flask import Blueprint, jsonify, request
from bson import ObjectId

from database.conn_database import client_db
from models.producto import (
    obtener_productos,
    obtener_producto_por_codigo,
    create_producto
)

productos_bp = Blueprint('productos', __name__)

try:
    productos = client_db["productos"] # Colección de productos en la base de datos
except Exception as e:
    print(f"Error conectando a la base de datos: {e}")

@productos_bp.route('/productos', methods=['GET'])
def get_productos():
    try:
        print("Endpoint /productos llamado")
        productos_list = obtener_productos()
        print(f"Se encontraron {len(productos_list)} productos")
        for producto in productos_list:
            producto['_id'] = str(producto['_id'])
            if 'proveedorId' in producto:
                producto['proveedorId'] = str(producto['proveedorId'])
        return jsonify(productos_list), 200
    except Exception as e:
        print(f"Error en get_productos: {e}")
        return jsonify({"error": str(e)}), 500

@productos_bp.route('/productos/<string:codigo>', methods=['GET'])
def get_producto(codigo):
    try:
        print(f"Endpoint /productos/{codigo} llamado")
        producto = obtener_producto_por_codigo(codigo)
        if producto:
            producto['_id'] = str(producto['_id'])
            producto['codigo'] = str(producto['codigo'])
            if 'proveedorId' in producto:
                producto['proveedorId'] = str(producto['proveedorId'])
            print(f"Producto encontrado: {producto}")
            return jsonify(producto), 200
        else:
            print("Producto no encontrado")
            return jsonify({"error": "Producto no encontrado"}), 404
    except Exception as e:
        print(f"Error en get_producto: {e}")
        return jsonify({"error": str(e)}), 500

@productos_bp.route('/productos', methods=['POST'])
def agregar_producto():
        try:
            
            if request.is_json:
                data = request.get_json()
            else:
                data = request.form.to_dict()  
            print("Endpoint /productos POST llamado")
            create_producto(data)
            return jsonify({"message": "Producto creado"}), 201
        except Exception as e:
            print(f"Error en create_producto: {e}")
            return jsonify({"error": str(e)}), 500