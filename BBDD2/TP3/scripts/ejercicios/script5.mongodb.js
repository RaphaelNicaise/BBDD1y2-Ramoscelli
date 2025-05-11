use('tiendaOnline');

db.ventas.aggregate([
    {$lookup: {
      from: "productos",
      localField: "producto_id",
      foreignField: "_id",
      as: 'producto'
    }}
]);

db.ventas.aggregate([
    {$lookup: {
        from: "productos",
        localField: "producto_id",
        foreignField: "_id",
        as: 'producto'
    }},
    {$project: {
        "_id": 1,
        "producto.nombre": 1, // dejo estos campos que son los que me sirven para la agrupacion
        "total": {$multiply: ["$cantidad", "$precio_unitario"]} // creamos campo total
    }},
    {$group: {
        _id: "$producto.nombre",
        "total_vendido": {$sum: "$total"} // sumamos total de cada producto
    }}
]);