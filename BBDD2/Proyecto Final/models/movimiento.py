from datetime import datetime
from bson import ObjectId

from database.conn_database import client_db

movimientos = client_db["movimientos"]



def get_movimientos_query():
    pipeline = [
        {
            "$lookup": {
                "from": "productos",
                "localField": "productoId",
                "foreignField": "_id",
                "as": "producto_info"
            }
        },
        {
            "$unwind": "$producto_info"
        },
        {
            "$addFields": {
                "codigo_producto": "$producto_info.codigo"
            }
        },
        {
            "$project": {
                "producto_info": 0
            }
        }    
    ]
    return list(movimientos.aggregate(pipeline))

def get_movimientos_by_codigo_producto(codigo):
    pipeline = [
        {
            "$lookup": {
                "from": "productos",
                "localField": "productoId",
                "foreignField": "_id",
                "as": "producto_info"
            }
        },
        {
            "$unwind": "$producto_info"
        },
        {
            "$match": {
                "producto_info.codigo": codigo
            }
        },
        {
            "$addFields": {
                "codigo_producto": "$producto_info.codigo"
            }
        },
        {
            "$project": {
                "producto_info": 0
            }
        }        
    ]
    return list(movimientos.aggregate(pipeline))