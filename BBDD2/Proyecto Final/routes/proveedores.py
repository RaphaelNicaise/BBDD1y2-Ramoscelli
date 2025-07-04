from flask import Blueprint, jsonify
from bson import ObjectId

from database.conn_database import client_db

proveedores_bp = Blueprint('proveedores', __name__)

try:
    proveedores = client_db["proveedores"]  # Colección de proveedores en la base de datos
except Exception as e:
    print(f"Error conectando a la base de datos: {e}")
    
    

@proveedores_bp.route('/proveedores', methods=['GET'])
def get_proveedores():
    try:
        print("Endpoint /proveedores llamado")
        proveedores_list = list(proveedores.find({}))
        print(f"Se encontraron {len(proveedores_list)} proveedores")
        for proveedor in proveedores_list:
            proveedor['_id'] = str(proveedor['_id'])
        return jsonify(proveedores_list), 200
    except Exception as e:
        print(f"Error en get_proveedores: {e}")
        return jsonify({"error": str(e)}), 500 
    
@proveedores_bp.route('/proveedores/<string:nombre>', methods=['GET'])
def get_proveedor_by_nombre(nombre):
    try:
        print(f"Buscando proveedor con nombre: {nombre}")
        proveedor = proveedores.find_one({"nombre": nombre})
        if proveedor:
            proveedor['_id'] = str(proveedor['_id'])
            print(f"Proveedor encontrado: {proveedor}")
            return jsonify(proveedor), 200
        else:
            print("Proveedor no encontrado")
            return jsonify({"error": "Proveedor no encontrado"}), 404
    except Exception as e:
        print(f"Error en get_proveedor_by_nombre: {e}")
        return jsonify({"error": str(e)}), 500