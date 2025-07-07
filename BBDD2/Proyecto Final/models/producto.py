from datetime import datetime
from bson import ObjectId

from database.conn_database import client_db

productos = client_db["productos"]

def obtener_productos():
    pipeline = [
  {
        "$lookup": {
            "from": "proveedores",           
            "localField": "proveedorId",     
            "foreignField": "_id",           
            "as": "proveedor"
        }
    },
    
    {
        "$unwind": {
            "path": "$proveedor",
            "preserveNullAndEmptyArrays": True
        }
    },
    {
        "$addFields": {
            "proveedorNombre": "$proveedor.nombre"
        }
    },
    
    {        "$project": {
            "proveedor": 0
        }
    }
        
]
    return list(productos.aggregate(pipeline))

def obtener_producto_por_codigo(codigo):
    producto = productos.find_one({"codigo": codigo})
    if producto:
        producto['_id'] = str(producto['_id'])
        if 'proveedorId' in producto:
            producto['proveedorId'] = str(producto['proveedorId'])
        return producto
    return None


def create_producto(data):
    try:
        print("Creando producto con los siguientes datos:", data)
        
        if productos.find_one({"codigo": data["codigo"]}):
            raise ValueError("El código del producto ya existe.")
        
        # Convertir proveedorId a ObjectId si existe y no es None ni vacío
        if 'proveedorId' in data and data['proveedorId']:
            try:
                data['proveedorId'] = ObjectId(data['proveedorId'])
            except Exception as e:
                raise ValueError("proveedorId inválido: debe ser un ObjectId válido")

        data["fechaUltimaActualizacion"] = datetime.utcnow()
        
        result = productos.insert_one(data)
        
        new_producto = productos.find_one({"_id": result.inserted_id})
        new_producto['_id'] = str(new_producto['_id'])
        if 'proveedorId' in new_producto:
            new_producto['proveedorId'] = str(new_producto['proveedorId'])
        
        print("Producto creado exitosamente:", new_producto)
        return new_producto
    except Exception as e:
        print(f"Error al crear producto: {e}")
        raise
