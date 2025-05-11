use('tiendaOnline');

db.productos.aggregate([
    {  $project: {
      "nombre": 1,
      "precio": 1,
      "precio_con_impuesto": {$multiply: ["$precio", 1.21 ]}, // precio con iva
    }}
]);

db.ventas.aggregate([
    {
        $project: {
            "_id": 1,
            "cliente.nombre": 1,
            "total": 1,
            "descuento": {$multiply: ["$total", 0.10]} 
        }
    }
]);