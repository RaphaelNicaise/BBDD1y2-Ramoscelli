// Crear un pipeline que obtenga las ventas totales por mes, indicando también el producto más vendido de cada mes.

use('tiendaOnline')

db.ventas.aggregate([
    {$lookup: { // unimos con la coleccion productos
        from: "productos",
        localField: "producto_id",
        foreignField: "_id",
        as: "producto"
    }},
    {$unwind: "$producto"}, 
    {$project: { // agarramos los datos que necesitamos
        _id: 1,
        producto: "$producto.nombre", 
        cantidad: 1,
        mes: {$month: "$fecha"}, // extrae el mes de la fecha
    }},
    {$group:
        {
            _id: { mes: "$mes", producto: "$producto" }, // agrupamos por mes y producto
            totalVentas: {$sum: "$cantidad"}, // sumamos la cantidad de ventas
        }
    },
    {$sort: { // ordenamos por mes y total de ventas
        "_id.mes": 1,
        totalVentas: -1
    }},
    {$group: { 
        _id: "$_id.mes", // agrupamos por mes
        productoMasVendido: {$first: "$_id.producto"},// first devuelve el primer elemento de la lista
        totalVentas: {$sum: "$totalVentas"}
    }},
    {$project: { // viuelvo a mostrar lo q nos interesa
        _id: 0,
        mes: "$_id",
        productoMasVendido: 1,
        totalVentas: 1
    }}
])