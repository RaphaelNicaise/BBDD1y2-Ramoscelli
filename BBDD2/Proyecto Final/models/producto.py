from datetime import datetime
from bson import ObjectId

from database.conn_database import client_db

productos = client_db["productos"]

def obtener_productos():
    return list(productos.find({}))

def obtener_producto_por_codigo(codigo):
    producto = productos.find_one({"codigo": codigo})
    if producto:
        producto['_id'] = str(producto['_id'])
        if 'proveedorId' in producto:
            producto['proveedorId'] = str(producto['proveedorId'])
        return producto
    return None