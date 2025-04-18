use("empresa");

db.createCollection("empleados");

db.empleados.insertMany([
    {nombre:'Rapha', edad: 20, puesto: 'pasante'},
    {nombre:'Pepe', edad: 32, puesto: 'Backend Developer'},
    {nombre:'Juan', edad: 41, puesto: 'Ingeniero de Datos'}
]);

db.empleados.updateOne(
    {nombre: 'Pepe'},
    {$set: {puesto: 'Backend Developer JR'}}
);

db.empleados.deleteOne(
    {puesto: 'pasante'}
);
