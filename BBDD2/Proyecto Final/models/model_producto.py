from bson import ObjectId

def obtener_productos(db):
    """
    Hace un lookup para devolver directamente el nombre del proveedor ademas del producto
    """
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
    return list(db.productos.aggregate(pipeline))
 
def insert_producto(db, producto):
    resultado = db.productos.insert_one(producto)
    return str(resultado.inserted_id)

def borrar_producto(db, producto_id):
    resultado = db.productos.delete_one({"_id": ObjectId(producto_id)})
    return resultado.deleted_count > 0

def actualizar_producto(db, producto_id, producto):
    resultado = db.productos.update_one(
        {"_id": ObjectId(producto_id)},
        {"$set": producto}
    )
    return resultado.modified_count > 0

def modificar_stock(db, producto_id, cantidad):
    """
    Modifica el stock de un producto.
    """
    
    producto = db.productos.find_one({"_id": ObjectId(producto_id)})  # Verifica si el producto existe
    
    if producto:
        stock_actual = producto.get("stockActual", 0)
        nuevo_stock = int(stock_actual) + int(cantidad)
        
        if nuevo_stock < 0:
            return False
        
        
        resultado = db.productos.update_one(
            {"_id": ObjectId(producto_id)},
            {"$set": {"stockActual": nuevo_stock}}
        )
    return resultado.modified_count > 0

def obtener_stock_por_producto(db, producto_id):
    stock_producto = db.productos.find_one({"_id": ObjectId(producto_id)}, {"_id":1,"nombre":1,"stockActual": 1, "stock_minimo":1})
    if stock_producto:
        return {
            "_id": str(stock_producto["_id"]),
            "nombre": stock_producto.get("nombre"),
            "stockActual": stock_producto.get("stockActual", 0),
            "stockMinimo": stock_producto.get("stockMinimo", 0)
        }
        

def obtener_productos_con_stock_bajo(db):
    pipeline = [
        {
            "$match": {
                "$expr": {
                    "$lt": ["$stockActual", "$stockMinimo"]
                }
            }
        },
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
        {
            "$project": {
                "proveedor": 0
            }
        }
    ]
    return list(db.productos.aggregate(pipeline))