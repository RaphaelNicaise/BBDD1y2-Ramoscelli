from bson import ObjectId

def obtener_proveedores(db):
    """
    Obtiene todos los proveedores de la base de datos.

    Args:
        db: Conexión a la base de datos.

    Returns:
        list: Lista de proveedores.
    """
    return list(db.proveedores.find())

def insertar_proveedor(db, proveedor):
    """
    Inserta un nuevo proveedor en la base de datos.

    Args:
        db: Conexión a la base de datos.
        proveedor (dict): Diccionario con los datos del proveedor.

    Returns:
        str: ID del proveedor insertado.
    """
    resultado = db.proveedores.insert_one(proveedor)
    return str(resultado.inserted_id)

def borrar_proveedor(db, proveedor_id):
    """
    Elimina un proveedor de la base de datos y los productos asociados.

    Args:
        db: Conexión a la base de datos.
        proveedor_id: ID del proveedor a eliminar.

    Returns:
        bool: True si se eliminó correctamente, False en caso contrario.
    """
    resultado = db.proveedores.delete_one({"_id": ObjectId(proveedor_id)})
    # borrar productos asociados al proveedor
    db.productos.delete_many({"proveedorId": ObjectId(proveedor_id)})

    return resultado.deleted_count > 0