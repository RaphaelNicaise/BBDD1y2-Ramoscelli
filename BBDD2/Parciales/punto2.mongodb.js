use('parcial')

// orden de los stages
//match para filtrar la fecha entre 13/05 hasta hoy
//lookup para unir pedidos con platoS
// sort para ordenar por total de porciones 
// limit por los 3 platos
//project para nombre plato y total porciones 

db.pedidos.aggregate([
    {$match: {
        fecha: {
            $gte: ISODate("2025-05-13T00:00:00Z"),
            $lte: new Date()
        }
    }
    },
    {$lookup: {
        from: "platos",
        localField: "plato_id",
        foreignField: "_id",
        as: "plato_info"
    }
    },
    {$sort: {"plato_info.porciones_disponibles": -1}}, // 1 asc -1 desc
    {$limit: 
        3
    },
    {$project: {
        _id: 0,
        nombreplato: "$plato_info.nombre",
        totalPorciones: "$plato_info.porciones_disponibles"
    }
    }
])