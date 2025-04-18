use("empresa");

db.empleados.updateMany(
    {}, // actualizamos todos
    {
        $set: {
            "direccion":{
                "calle": "calle123",
                "ciudad": "Bahia Blanca",
                "codigo_postal": 8000
            }
        }
    }
);
