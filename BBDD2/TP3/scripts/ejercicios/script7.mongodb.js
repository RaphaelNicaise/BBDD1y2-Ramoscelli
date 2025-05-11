use('tiendaOnline');

db.productos.aggregate([
    {$project: {
        "nombre": 1,
        "precio": 1,
        "clasificacion": {
            $switch: {
                branches: [
                    {case: { $gte: ["$precio", 500 ]}, then: "premium"}, // mayor o igual a 500
                    {case: { $and: [ { $gt: ["$precio", 100 ]},{ $lt: ["$precio", 500 ]} ] }, then: "estandar"}, // entre 100 y 500
                    {case: { $lte: ["$precio", 100 ]}, then: "economico"} // menor o igual a 100
                ]
            }
        }
    }}
]);

db.ventas.aggregate([
    // Clasificar las ventas según su total: "Pequeña" (<200), "Mediana" (200-800), "Grande" (>800).

    {$project: {
        "total": 1,
        "clasificacion": {
            $switch: {
                branches: [
                    {case: { $gte: ["$total", 800 ]}, then: "grande"}, // mayor o igual a 800
                    {case: { $and: [ { $gt: ["$total", 200 ]},{ $lt: ["$total", 800 ]} ] }, then: "mediana"}, // entre 200 y 800
                    {case: { $lte: ["$total", 200 ]}, then: "pequenia"} // menor o igual a 200
                ]
            }
        }
    }},
    {$group: {
        "_id": "$clasificacion",
        "total_vendido": { $sum: "$total" },
        "cantidad_ventas": { $sum: 1 }
    }},
])