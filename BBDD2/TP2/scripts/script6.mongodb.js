use("empresa");

db.createCollection("clientes");

db.clientes.insertMany([
    {nombre: 'Mauro', apellido: 'Icardi'},
    {nombre: 'Adam', apellido: 'Sandler'},
    {nombre: 'Diego', apellido: 'Latorre'},
    {nombre: 'Valeria', apellido: 'Lynch'},
    {nombre: 'Wanda', apellido: 'Nara'},
    {nombre: 'Lionel', apellido: 'Messi'}
]);

db.clientes.createIndex(
    {nombre: 1, apellido: 1}
);