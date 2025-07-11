from bson import ObjectId
from datetime import datetime


def seed_data(db):
    """
    Inserta datos de ejemplo en la base de datos si todas las colecciones están vacías.

    Args:
        db: Conexión a la base de datos MongoDB.
    """
    if db.productos.count_documents({}) == 0 and db.proveedores.count_documents({}) == 0 and db.movimientos.count_documents({}) == 0:
        id_producto = ObjectId()
        id_proveedor = ObjectId()

        db.productos.insert_one({
            "_id": id_producto,
            "codigo": "PROD001",
            "nombre": "Laptop HP",
            "categoria": "Electrónicos",
            "precio": 799.99,
            "stockActual": 15,
            "stockMinimo": 5,
            "proveedorId": id_proveedor,
            "fechaUltimaActualizacion": datetime.utcnow()
        })

        db.movimientos.insert_one({
            "_id": ObjectId(),
            "productoId": id_producto,
            "tipo": "entrada",
            "cantidad": 10,
            "motivo": "Compra a proveedor",
            "fecha": datetime.utcnow(),
            "usuario": "admin"
        })

        db.proveedores.insert_one({
            "_id": id_proveedor,
            "nombre": "Distribuidora Tech",
            "contacto": "Juan López",
            "telefono": "+1234567890",
            "email": "ventas@distritech.com",
            "productosOfrecidos": ["PROD001", "PROD002"]
        })
        print("Datos seed insertados")