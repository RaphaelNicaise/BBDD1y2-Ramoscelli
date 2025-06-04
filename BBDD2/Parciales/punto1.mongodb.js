use('parcial')

    // inciso 1
db.platos.aggregate([
        {$match: {
            porciones_disponibles: {$lte: 12}
        }},
        {$project: {
                nombre: 1,
                porciones_disponibles: 1,
                _id: 0
            }
        }
    ]);


    // inciso 2
db.pedidos.aggregate([
        {$match: {
                fecha: {
                    $gte: ISODate("2025-05-10T00:00:00Z"),
                    $lte: ISODate("2025-05-10T23:59:59Z") // puse asi pq no se como hacer para que tome de un dia dado
                    // tambien podia poner LT isodate("2025-05-11T00:00:00Z") 
                }}},
        {$count:'totalpedidos'}
    ]);

    // inciso 3
db.pedidos.aggregate([
        {$group: {
            _id: '_id',
            platatotal: {$sum: "$total_pedido"}
        }},
        {$project: {
            platatotal: 1,
            _id: 0 // este no
        }}
    ]);
