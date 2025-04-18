use("empresa");

db.createCollection("ventas");

db.ventas.insertMany([
    { producto: "Laptop", cantidad: 1, precio_unitario: 1200 },
    { producto: "Mouse", cantidad: 2, precio_unitario: 25 },
    { producto: "Teclado", cantidad: 3, precio_unitario: 45 },
    { producto: "Monitor", cantidad: 1, precio_unitario: 200 },
    { producto: "Impresora", cantidad: 1, precio_unitario: 150 },
    { producto: "Laptop", cantidad: 2, precio_unitario: 1200 },
    { producto: "Mouse", cantidad: 1, precio_unitario: 25 },
    { producto: "Teclado", cantidad: 1, precio_unitario: 45 },
    { producto: "Monitor", cantidad: 2, precio_unitario: 200 },
    { producto: "Impresora", cantidad: 1, precio_unitario: 150 }
]);

db.ventas.aggregate({
    $group: {
        _id: "$producto", // agrupamos por producto
        total_ventas: { $sum: { $multiply: ["$cantidad", "$precio_unitario"] } }
        // total_venta = cantidad * precio_unitario
    }
});
