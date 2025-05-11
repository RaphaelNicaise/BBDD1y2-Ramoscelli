use('tiendaOnline');

db.productos.aggregate([
    {$unwind: "$valoraciones"}, // separa cada valoracion en un documento dentro del documento padre (si o si a una lista)
    {$group: {
      _id: "$valoraciones.puntuacion", 
      "cantidad_con_esa_puntuacion": {$sum: 1} // cuenta las valoraciones hay con esa puntuacion
    }},
    {$sort: {cantidad_con_esa_puntuacion: -1}} // ordena de mas puntuaciones a meno
]);