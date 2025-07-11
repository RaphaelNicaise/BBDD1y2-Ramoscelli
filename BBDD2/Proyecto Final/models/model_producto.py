from bson import ObjectId

def obtener_productos(db):
    """
    Obtiene todos los productos y agrega el nombre del proveedor.

    Args:
        db: Conexión a la base de datos.

    Returns:
        list: Lista de productos con el nombre del proveedor.
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
    """
    Inserta un nuevo producto en la base de datos.

    Args:
        db: Conexión a la base de datos.
        producto (dict): Diccionario con los datos del producto.

    Returns:
        str: ID del producto insertado.
    """
    resultado = db.productos.insert_one(producto)
    return str(resultado.inserted_id)

def borrar_producto(db, producto_id):
    """
    Elimina un producto de la base de datos.

    Args:
        db: Conexión a la base de datos.
        producto_id: ID del producto a eliminar.

    Returns:
        bool: True si se eliminó correctamente, False en caso contrario.
    """
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
    Modifica el stock de un producto en la base de datos.

    Args:
        db: Conexión a la base de datos.
        producto_id: ID del producto a modificar.
        cantidad: Cantidad a sumar o restar al stock actual.

    Returns:
        bool: True si el stock se modificó correctamente, False en caso contrario.
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
    """
    Obtiene el stock actual y mínimo de un producto.

    Args:
        db: Conexión a la base de datos.
        producto_id: ID del producto.

    Returns:
        dict: Diccionario con el ID, nombre, stock actual y stock mínimo del producto.
    """
    stock_producto = db.productos.find_one({"_id": ObjectId(producto_id)}, {"_id":1,"nombre":1,"stockActual": 1, "stock_minimo":1})
    if stock_producto:
        return {
            "_id": str(stock_producto["_id"]),
            "nombre": stock_producto.get("nombre"),
            "stockActual": stock_producto.get("stockActual", 0),
            "stockMinimo": stock_producto.get("stockMinimo", 0)
        }
        

def obtener_productos_con_stock_bajo(db):
    """
    Obtiene los productos cuyo stock actual es menor que el stock mínimo y agrega el nombre del proveedor.

    Args:
        db: Conexión a la base de datos.

    Returns:
        list: Lista de productos con stock bajo y el nombre del proveedor.
    """
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