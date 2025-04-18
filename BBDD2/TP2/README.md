# TP2 Bases de Datos 2

#### Participantes:
- [Raphael Nicaise](https://github.com/RaphaelNicaise)
- [Santiago Segal](https://github.com/Santucho12)
- [Abner Grgurich](https://github.com/Abner2646)
- [Nicolas Cordano](https://github.com/NACXIIX)

#### Puntos: 
[1](#1)
[2](#2)
[3](#3)
[4](#4)
[5](#5)
[6](#6)
[7](#7)
[8](#8)
[9](#9)

<hr style="height:1px; border:none; background-color:#e1e4e8;" />

Nos conectamos a la base de datos de MongoDB mediante **mongosh**:
<img src="./assets/image.png" alt="MongoDB Connection" width="600"/>

<hr style="height:1px; border:none; background-color:#e1e4e8;" />

### 1.

-> [Script](./scripts/script1.mongodb.js)

- Creamos la base de datos empresa: 
```js
use ("empresa");
```
- Creamos la coleccion empleados:
```js
db.createCollection("empleados");
```
- Insertamos 3 documentos (empleados) en la coleccion:
```js
db.empleados.insertMany([
    {nombre:'Rapha', edad: 20, puesto: 'pasante'},
    {nombre:'Pepe', edad: 32, puesto: 'Backend Developer'},
    {nombre:'Juan', edad: 41, puesto: 'Ingeniero de Datos'}
]);
```

- Hacemos update sobre un empleado:
```js
db.empleados.updateOne(
    {nombre: 'Rapha'},
    {$set: {puesto: 'Backend Developer'}}
);
```

- Hacemos delete sobre un empleado que sea pasante:
```js
db.empleados.deleteOne(
    {puesto: 'pasante'}
);
```

- Y asi queda la coleccion empleados:
```bash
empresa> db.empleados.find() ->
[
  {
    _id: ObjectId('68019d5e85074e01beb5f8a3'),
    nombre: 'Pepe',
    edad: 32,
    puesto: 'Backend Developer JR'
  },
  {
    _id: ObjectId('68019d5e85074e01beb5f8a4'),
    nombre: 'Juan',
    edad: 41,
    puesto: 'Ingeniero de Datos'
  }
]
```



### 2.

-> [Script](./scripts/script2.mongodb.js)

### 3.

-> [Script](./scripts/script3.mongodb.js)

### 4.

-> [Script](./scripts/script4.mongodb.js)

### 5.

-> [Script](./scripts/script5.mongodb.js)

### 6.

-> [Script](./scripts/script6.mongodb.js)

### 7.

-> [Script](./scripts/script7.mongodb.js)

### 8.

-> [Script](./scripts/script8.mongodb.js)

### 9.

-> [Script](./scripts/script9.mongodb.js)