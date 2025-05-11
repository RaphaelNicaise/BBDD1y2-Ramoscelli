use('tiendaOnline');

db.productos.aggregate([
    {
        "$group": {
            _id: "$categoria",
            max: {"$max": "$precio" }, 
            min: {"$min": "$precio" },
            prom: {"$avg": "$precio" }
        }
    },
    {
        "$sort":{
            "prom": -1 // ordenamos por promedio de precio descendente
        }
    }
]);

db.ventas.aggregate([
    {
        "$group": {
            "_id": "$cliente.pais",
            "cantidad_transacciones": {"$sum": 1}, // suma 1 por cada transaccion
            "montototal": {"$sum": "$total"} // suma el total de cada transaccion
        }
    },
    {
        "$sort": {"montototal": -1} // sort por monto total descendente
    }
]);
