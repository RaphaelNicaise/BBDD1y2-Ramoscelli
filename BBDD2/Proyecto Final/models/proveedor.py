from datetime import datetime
from bson import ObjectId

{
  "_id": {
    "$oid": "68658eca63637778c4023ca5"
  },
  "nombre": "Distribuidora Tech",
  "contacto": "Juan López",
  "telefono": "+1234567890",
  "email": "ventas@distritech.com",
  "productosOfrecidos": [
    "PROD001",
    "PROD002"
  ]
}

class Proveedor:
    def __init__(self, nombre, contacto, telefono, email, productosOfrecidos, _id=None, fechaCreacion=None):
        
        self._id = _id if _id is not None else ObjectId()
        self.nombre = nombre
        self.contacto = contacto
        self.telefono = telefono
        self.email = email
        self.productosOfrecidos = productosOfrecidos
        self.fechaCreacion = fechaCreacion if fechaCreacion is not None else datetime.now()

    def to_dict(self):
        return {
            "_id": str(self._id),
            "nombre": self.nombre,
            "contacto": self.contacto,
            "telefono": self.telefono,
            "email": self.email,
            "productosOfrecidos": self.productosOfrecidos,
            "fechaCreacion": self.fechaCreacion.isoformat()
        }