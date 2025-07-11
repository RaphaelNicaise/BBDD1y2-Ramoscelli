from bson import ObjectId
from datetime import datetime

from models import model_producto

def obtener_movimientos(db):
    """
    Obtiene todos los movimientos y agrega el nombre del producto

    Args:
        db: Conexión a la base de datos.

    Returns:
        list: Lista de movimientos con el nombre del producto.
    """
    pipeline = [
        {
            "$lookup": {
                "from": "productos",           
                "localField": "productoId",     
                "foreignField": "_id",           
                "as": "producto"
            }
        },
        {
            "$unwind": {
                "path": "$producto",
                "preserveNullAndEmptyArrays": True
            }
        },
        {
            "$addFields": {
                "productoNombre": "$producto.nombre"
            }
        },
        {
            "$project": {
                "producto": 0
            }
        }
    ]
    return list(db.movimientos.aggregate(pipeline))
    
def obtener_movimiento_por_fecha(db, fecha_inicio, fecha_fin):
    """ 
    Obtiene los movimientos entre dos fechas y agrega el nombre del producto.

    Args:
        db: Conexión a la base de datos.
        fecha_inicio: Fecha de inicio (datetime).
        fecha_fin: Fecha de fin (datetime).

    Returns:
        list: Lista de movimientos con el nombre del producto.
    """
    pipeline = [
        {
            "$match": {
                "fecha": {
                    "$gte": fecha_inicio,
                    "$lte": fecha_fin
                }
            }
        },
        {
            "$lookup": {
                "from": "productos",           
                "localField": "productoId",     
                "foreignField": "_id",           
                "as": "producto"
            }
        },
        {
            "$unwind": {
                "path": "$producto",
                "preserveNullAndEmptyArrays": True
            }
        },
        {
            "$addFields": {
                "productoNombre": "$producto.nombre"
            }
        },
        {
            "$project": {
                "producto": 0
            }
        }
    ]
    return list(db.movimientos.aggregate(pipeline))

    
def insertar_movimiento(db, movimiento):
    """
    Inserta un nuevo movimiento en la base de datos y actualiza el stock del producto.

    Args:
        db: Conexión a la base de datos.
        movimiento (dict): Diccionario con los datos del movimiento.

    Raises:
        ValueError: Si el campo 'productoId' no está presente en el movimiento.

    Returns:
        str: ID del movimiento insertado.
    """
    if not movimiento.get("productoId"):
        raise ValueError("El campo 'productoId' es obligatorio")
    
    movimiento["productoId"] = ObjectId(movimiento["productoId"])
    movimiento["fecha"] = datetime.now()
    
    if movimiento["tipo"] == "entrada":
        res = model_producto.modificar_stock(db, movimiento["productoId"], movimiento["cantidad"])
    elif movimiento["tipo"] == "salida":
        res = model_producto.modificar_stock(db, movimiento["productoId"], -int(movimiento["cantidad"]))
        
    if res:
        resultado = db.movimientos.insert_one(movimiento)
    
        return str(resultado.inserted_id)