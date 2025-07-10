from bson import ObjectId
from datetime import datetime

from models import model_producto

def obtener_movimientos(db):
    """
    Hace un lookup para devolver directamente el nombre del producto ademas del movimiento
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
    Inserta un nuevo movimiento en la colección de movimientos.
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