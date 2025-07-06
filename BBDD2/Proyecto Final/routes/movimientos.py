from flask import Blueprint, jsonify
from bson import ObjectId

from database.conn_database import client_db

movimientos_bp = Blueprint('movimientos', __name__)


@movimientos_bp.route('/movimientos', methods=['GET'])
def get_movimientos():
    try:
        print("Endpoint /movimientos llamado")
        movimientos = client_db["movimientos"]  # Colección de movimientos en la base de datos
        movimientos_list = list(movimientos.find({}))
        print(f"Se encontraron {len(movimientos_list)} movimientos")
        for movimiento in movimientos_list:
            movimiento['_id'] = str(movimiento['_id'])
            movimiento['productoId'] = str(movimiento['productoId'])
            movimiento['fecha'] = movimiento['fecha'].isoformat()
        return jsonify(movimientos_list), 200
    except Exception as e:
        print(f"Error en get_movimientos: {e}")
        return jsonify({"error": str(e)}), 500
    
@movimientos_bp.route('/movimientos/<string:producto_id>', methods=['GET'])
def get_movimientos_by_producto(producto_id):
    try:
        print(f"Buscando movimientos para el producto con ID: {producto_id}")
        movimientos = client_db["movimientos"]  # Colección de movimientos en la base de datos
        movimientos_list = list(movimientos.find({"productoId": ObjectId(producto_id)}))
        if not movimientos_list:
            print("No se encontraron movimientos para este producto")
            return jsonify({"error": "No se encontraron movimientos para este producto"}), 404
        for movimiento in movimientos_list:
            movimiento['_id'] = str(movimiento['_id'])
            movimiento['productoId'] = str(movimiento['productoId'])
            movimiento['fecha'] = movimiento['fecha'].isoformat()
        return jsonify(movimientos_list), 200
    except Exception as e:
        print(f"Error en get_movimientos_by_producto: {e}")
        return jsonify({"error": str(e)}), 500