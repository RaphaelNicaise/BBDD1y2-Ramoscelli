use("empresa");

db.empleados.find({
    $and: [
        {edad: {$gt: 25}}, // mayor a 25
        {edad: {$lt: 40}} // menor a 40
    ] 
});

