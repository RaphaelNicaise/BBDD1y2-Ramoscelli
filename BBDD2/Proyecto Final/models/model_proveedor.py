from bson import ObjectId

def obtener_proveedores(db):
    return list(db.proveedores.find())

def insertar_proveedor(db, proveedor):
    
    resultado = db.proveedores.insert_one(proveedor)
    return str(resultado.inserted_id)

def borrar_proveedor(db, proveedor_id):
    
    resultado = db.proveedores.delete_one({"_id": ObjectId(proveedor_id)})
    # borrar productos asociados al proveedor
    db.productos.delete_many({"proveedorId": ObjectId(proveedor_id)})

    return resultado.deleted_count > 0