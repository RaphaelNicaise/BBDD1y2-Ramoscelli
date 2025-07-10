from flask import Blueprint, request, jsonify, redirect, url_for, render_template
from bson import ObjectId

from models import model_producto, model_proveedor
from database import conn_database

productos_bp = Blueprint('productos', __name__)

@productos_bp.route('/', methods=['GET'])
def get_productos():
    productos = model_producto.obtener_productos(conn_database.client_db)
    proveedores = model_proveedor.obtener_proveedores(conn_database.client_db)
    return render_template('productos.html', productos=productos, proveedores=proveedores)

@productos_bp.route('/agregar', methods=['POST'])
def agregar_producto():
    nombre = request.form.get('nombre')
    descripcion = request.form.get('descripcion')
    precio = request.form.get('precio')
    proveedor_id = request.form.get('proveedor_id')
    
    if not nombre or not precio or not proveedor_id:
        return jsonify({"error": "Todos los campos son obligatorios"}), 400
    
    producto = {
        "nombre": nombre,
        "descripcion": descripcion,
        "precio": float(precio),
        "proveedor_id": int(proveedor_id)
    }
    
    producto_id = model_producto.insertar_producto(conn_database.client_db, producto)
    
    return redirect(url_for('productos.get_productos'))

@productos_bp.route('/eliminar/<producto_id>', methods=['POST'])
def eliminar_producto(producto_id):
    if not model_producto.borrar_producto(conn_database.client_db, producto_id):
        return jsonify({"error": "Producto no encontrado"}), 404
    
    return redirect(url_for('productos.get_productos'))

@productos_bp.route('/editar/<producto_id>', methods=['GET', 'POST'])
def editar_producto(producto_id):
    db = conn_database.client_db

    if request.method == 'POST':
        nombre = request.form.get('nombre')
        categoria = request.form.get('categoria')
        precio = float(request.form.get('precio'))
        stock_actual = int(request.form.get('stockActual'))
        stock_minimo = int(request.form.get('stockMinimo'))
        proveedor_id = request.form.get('proveedorId')

        producto_actualizado = {
            "nombre": nombre,
            "categoria": categoria,
            "precio": precio,
            "stockActual": stock_actual,
            "stockMinimo": stock_minimo,
            "proveedorId": ObjectId(proveedor_id) if proveedor_id else None
        }

        model_producto.actualizar_producto(db, producto_id, producto_actualizado)
        return redirect(url_for('productos.get_productos'))

    # GET
    producto = db.productos.find_one({"_id": ObjectId(producto_id)})
    proveedores = model_proveedor.obtener_proveedores(db)

    return render_template('editar_prod.html', producto=producto, proveedores=proveedores)
