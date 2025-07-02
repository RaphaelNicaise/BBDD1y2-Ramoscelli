use ('Inventario');

id_producto = ObjectId();
id_proovedor = ObjectId();

db.productos.insertOne(
{
  _id: id_producto,
  codigo: "PROD001",
  nombre: "Laptop HP",
  categoria: "Electrónicos",
  precio: 799.99,
  stockActual: 15,
  stockMinimo: 5,
  proveedorId: id_proovedor,
  fechaUltimaActualizacion: ISODate()
}
);

db.movimientos.insertOne(
{
  _id: ObjectId(),
  productoId: id_producto,
  tipo: "entrada", // "entrada" o "salida"
  cantidad: 10,
  motivo: "Compra a proveedor",
  fecha: ISODate(),
  usuario: "admin"
}
);


db.proovedores.insertOne(
// Colección: proveedores
{
  _id: id_proovedor,
  nombre: "Distribuidora Tech",
  contacto: "Juan López",
  telefono: "+1234567890",
  email: "ventas@distritech.com",
  productosOfrecidos: ["PROD001", "PROD002"]
});    
