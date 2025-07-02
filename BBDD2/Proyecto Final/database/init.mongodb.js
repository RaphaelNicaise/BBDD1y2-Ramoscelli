use ('Inventario');

db.productos.insertOne([
{
  _id: ObjectId,
  codigo: "PROD001",
  nombre: "Laptop HP",
  categoria: "Electrónicos",
  precio: 799.99,
  stockActual: 15,
  stockMinimo: 5,
  proveedorId: ObjectId,
  fechaUltimaActualizacion: ISODate
}
]);

db.movimientos.insertOne([
{
  _id: ObjectId,
  productoId: ObjectId,
  tipo: "entrada", // "entrada" o "salida"
  cantidad: 10,
  motivo: "Compra a proveedor",
  fecha: ISODate,
  usuario: "admin"
}
]);


db.proovedores.insertOne([
// Colección: proveedores
{
  _id: ObjectId,
  nombre: "Distribuidora Tech",
  contacto: "Juan López",
  telefono: "+1234567890",
  email: "ventas@distritech.com",
  productosOfrecidos: ["PROD001", "PROD002"]
}]);    
