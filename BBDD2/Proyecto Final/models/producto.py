from datetime import datetime
from bson import ObjectId

class Producto:
    def __init__(self, codigo, nombre, categoria, precio, stock_actual, stock_minimo, proveedorId, fechaUltimaActualizacion=None, _id=None):
        self._id = _id if _id else ObjectId()
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock_actual = stock_actual
        self.stock_minimo = stock_minimo
        self.proveedorId = proveedorId # ObjectId
        self.fechaUltimaActualizacion = fechaUltimaActualizacion if fechaUltimaActualizacion else datetime.utcnow()

    def to_dict(self):
        return {
            "_id": str(self._id),
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock_actual": self.stock_actual,
            "stock_minimo": self.stock_minimo,
            "proveedorId": str(self.proveedorId),
            "fechaUltimaActualizacion": self.fecha_ultima_actualizacion.isoformat()
        }
        
    @staticmethod
    def from_dict(data):
        return Producto(
            codigo=data["codigo"],
            nombre=data["nombre"],
            categoria=data["categoria"],
            precio=data["precio"],
            stock_actual=data["stock_actual"],
            stock_minimo=data["stock_minimo"],
            proveedorId=ObjectId(data["proveedorId"]),
            fechaUltimaActualizacion=datetime.fromisoformat(data["fechaUltimaActualizacion"]),
            _id=ObjectId(data["_id"]) if "_id" in data else None
        )