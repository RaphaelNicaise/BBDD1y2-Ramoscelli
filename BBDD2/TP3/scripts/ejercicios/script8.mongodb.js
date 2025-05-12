/*
Obtener un informe de ventas que incluya:

Top 3 productos más vendidos (por cantidad)
Para cada producto: nombre, categoría, total de unidades vendidas, monto total generado
Puntuación promedio en valoraciones

*/

use('tiendaOnline');

db.ventas.aggregate([
    {$lookup: {
      from: "productos",
      localField: "producto_id",
      foreignField: "_id",
      as: "producto"
    }},
    {$group: {
        _id: "$producto._id",
        nombre: {$first: "$producto.nombre"},
        categoria: {$first: "$producto.categoria"},
        totalUnidadesVendidas: {$sum: "$cantidad"},
        montoTotalGenerado: {$sum: {$multiply: ["$cantidad", "$producto.precio"]}},
        puntuacionPromedio: {$avg: "$producto.valoracion"}
    }},
    {$sort: {totalUnidadesVendidas: -1}},
    {$limit: 3}
]);