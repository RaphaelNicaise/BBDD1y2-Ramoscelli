from flask import Blueprint, request, jsonify, redirect, url_for, render_template

from models import model_proveedor
from database import conn_database

proveedores_bp = Blueprint('proveedores', __name__)

@proveedores_bp.route('/', methods=['GET'])
def get_proveedores():
    proveedores = model_proveedor.obtener_proveedores(conn_database.client_db)
    return render_template('proveedores.html', proveedores=proveedores)

@proveedores_bp.route('/agregar', methods=['POST'])
def agregar_proveedor():
    """
    Procesa el formulario para agregar un nuevo proveedor.

    Redirige a la lista de proveedores o retorna error.
    """
    nombre = request.form.get('nombre')
    telefono = request.form.get('telefono')
    email = request.form.get('email')
    contacto = request.form.get('contacto')
    
    if not nombre or not telefono or not email:
        return jsonify({"error": "Todos los campos son obligatorios"}), 400
    
    proveedor = {
        "nombre": nombre,
        "telefono": telefono,
        "email": email,
        "contacto": contacto
    }
    
    proveedor_id = model_proveedor.insertar_proveedor(conn_database.client_db, proveedor)
    
    return redirect(url_for('proveedores.get_proveedores'))

@proveedores_bp.route('/eliminar/<proveedor_id>', methods=['POST'])
def eliminar_proveedor(proveedor_id):
    if not model_proveedor.borrar_proveedor(conn_database.client_db, proveedor_id):
        return jsonify({"error": "Proveedor no encontrado"}), 404
    
    return redirect(url_for('proveedores.get_proveedores'))