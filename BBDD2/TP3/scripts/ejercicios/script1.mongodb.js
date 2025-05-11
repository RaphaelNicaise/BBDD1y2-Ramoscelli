use('tiendaOnline');

db.productos.aggregate([
    {
        "$match": {
            "categoria": "Electrónica",
            "precio": { "$gt": 500 }
        }
    }
]);

db.ventas.aggregate([
    {
        "$match": {
            "cliente.pais":"España",
            "estado": "Entregado"   
        }
    }
]);