use('tiendaOnline');

db.ventas.aggregate([
    {$project: {
        "total": 1,
        "mes" : { $month: "$fecha" },
    }},
    {$group: {
        "_id": "$mes",
        "total_vendido": { $sum: "$total" },
    }}
]);

db.ventas.aggregate([
    {$project: {
        "total": 1,
        "nombre_dia" : { $dayOfWeek: "$fecha" }, // esta funcion devuelve el numero del dia de la semana
    }}, 
    {$group: {
        "_id": "$nombre_dia",
        "total_vendido": { $sum: "$total" },
    }},
    {$sort: { "total_vendido": -1 }}, // ordenamos descendente
    {$limit: 1} // el dia con mayor venta (devuelve 4 = miercoles)
    // domingo = 1 lunes = 2 martes = 3 miercoles = 4 jueves = 5 viernes = 6 sabado = 7
]);