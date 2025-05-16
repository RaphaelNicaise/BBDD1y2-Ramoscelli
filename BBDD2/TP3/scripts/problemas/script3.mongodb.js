// Crear un informe de clientes que incluya:

// Total gastado por cada cliente
// Número de compras realizadas
// Producto favorito (el que más ha comprado)
// Categoría preferida (donde más ha gastado)
// Fecha de primera y última compra

use('tiendaOnline');
db.ventas.aggregate([
    {$lookup: { // unimos con la coleccion productos
        from: "productos",
        localField: "producto_id",
        foreignField: "_id",
        as: "producto"
    }},
    {$unwind: "$producto"}, 
    {
    $group: {
      _id: { // por cada cliente producto y categoria)
        cliente: "$cliente.nombre",
        producto: "$producto.nombre",
        categoria: "$producto.categoria"
      },
      cantidad: {$sum: 1},
      totalGastadocliente: {$sum: "$total"},
      primeracompra: {$min: "$fecha"},
      ultimacompra: {$max: "$fecha"}
    }},
    {$group: {
        _id: "$_id.cliente",
        totalGastado: {$sum: "$totalGastadocliente"},
        comprastotal: {$sum: "$cantidad"},
        productoFav: {$first: "$_id.producto"},
        categoriaFav: {$first: "$_id.categoria"},
        primeracompra: {$min: "$primeracompra"},
        ultimacompra: {$max: "$ultimacompra"}
    }},
    {$project: {
        _id: 0,
        cliente: "$_id",
        totalGastado: 1,
        comprastotal: 1,
        productoFav: 1,
        categoriaFav: 1,
        primeracompra: 1,
        ultimacompra: 1
    }}
])