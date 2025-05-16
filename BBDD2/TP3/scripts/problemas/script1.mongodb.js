// Crear un pipeline que obtenga los productos más valorados (puntuación promedio más alta) con al menos 2 valoraciones.
use('tiendaOnline')
db.productos.aggregate([
    {
        $project: {
            nombre: 1,
            puntuacionPromedio: { $avg: "$valoraciones.puntuacion" },
            cantidadValoraciones: { $size: "$valoraciones" }
    }},
    {
        $match: {
            cantidadValoraciones: { $gte: 2 } // devuelve los q tengan almenos 2 valoraciones
    }},
    {
        $sort: {
            puntuacionPromedio: -1 // ordena de mayor a menor
        }
    }
])