from flask import Blueprint, request, jsonify, redirect, url_for, render_template
from bson import ObjectId
from datetime import datetime

from models import model_movimiento, model_producto
from database import conn_database

movimientos_bp = Blueprint('movimientos', __name__)

@movimientos_bp.route('/', methods=['GET'])
def get_movimientos():
    """
    Obtiene y muestra los movimientos, permitiendo filtrar por fecha.

    Renderiza movimientos.html 
    """
    fecha_inicio = request.args.get('fecha_inicio')
    fecha_fin = request.args.get('fecha_fin')
    
    if fecha_inicio and fecha_fin:
        try:
            fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
            fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d')
            
            if fecha_inicio > fecha_fin:
                fecha_inicio, fecha_fin = fecha_fin, fecha_inicio
                
            fecha_fin = fecha_fin.replace(hour=23, minute=59, second=59)
            
            movimientos = model_movimiento.obtener_movimiento_por_fecha(conn_database.client_db, fecha_inicio, fecha_fin)
        
        except ValueError:
            movimientos = model_movimiento.obtener_movimientos(conn_database.client_db)
    else:
        movimientos = model_movimiento.obtener_movimientos(conn_database.client_db)
    
    productos = model_producto.obtener_productos(conn_database.client_db)
    return render_template('movimientos.html', movimientos=movimientos, productos=productos)

@movimientos_bp.route('/agregar', methods=['GET', 'POST'])
def agregar_movimiento():
    """
    Muestra el formulario para agregar un movimiento y procesa el envío.

    Renderiza agregar_movimiento.html y desp redirige
    """
    if request.method == 'POST':
        movimiento = request.form.to_dict()
        try:
            model_movimiento.insertar_movimiento(conn_database.client_db, movimiento)
            return redirect(url_for('movimientos.get_movimientos'))
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
    return render_template('agregar_movimiento.html')