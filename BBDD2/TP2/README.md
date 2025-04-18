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
[10](#10)

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
```js
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
<hr style="height:1px; border:none; background-color:#e1e4e8;" />


### 2.

-> [Script](./scripts/script2.mongodb.js)

- Queremos los empleados que tengan mas de 25 y menos de 40 años:
```js
db.empleados.find({
    $and: [
        {edad: {$gt: 25}}, // mayor a 25
        {edad: {$lt: 40}} // menor a 40
    ] 
})
```

```js
[
  {
    _id: ObjectId('68019d5e85074e01beb5f8a3'),
    nombre: 'Pepe',
    edad: 32,
    puesto: 'Backend Developer JR'
  }
]
```
<hr style="height:1px; border:none; background-color:#e1e4e8;" />

### 3.

-> [Script](./scripts/script3.mongodb.js)


- Queremos recuperar solo el nombre y la edad de los empleados:
```js
use("empresa");

db.empleados.find(
    {}, // esto indica que no hay filtro
    { _id: 0, nombre: 1, puesto: 1 } // 0 no selecciona, 1 si (edad no se selecciona directamente) 
)
```

```json
[
  {
    "nombre": "Pepe",
    "puesto": "Backend Developer JR"
  },
  {
    "nombre": "Juan",
    "puesto": "Ingeniero de Datos"
  }
]
```

<hr style="height:1px; border:none; background-color:#e1e4e8;" />

### 4.

-> [Script](./scripts/script4.mongodb.js)

- Agregamos a cada documento (empleado) el campo direccion con datos de la calle, la ciudad y codigo postal:
```js
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
```

```js
[  
  {
    _id: ObjectId('68019d5e85074e01beb5f8a3'),
    nombre: 'Pepe',
    edad: 32,
    puesto: 'Backend Developer JR',
    direccion: { calle: 'calle123', ciudad: 'Bahia Blanca', codigo_postal: 8000 }
  },
  {
    _id: ObjectId('68019d5e85074e01beb5f8a4'),
    nombre: 'Juan',
    edad: 41,
    puesto: 'Ingeniero de Datos',
    direccion: { calle: 'calle123', ciudad: 'Bahia Blanca', codigo_postal: 8000 }
  }
]
```


<hr style="height:1px; border:none; background-color:#e1e4e8;" />

### 5.

-> [Script](./scripts/script5.mongodb.js)

- Creamos una nueva coleccion llamada ventas:
```js
use("empresa");

db.createCollection("ventas");
```

<details>
<summary>(open) Insertamos documentos creados con IA</summary>

```js
db.ventas.insertMany([
    { producto: "Laptop", cantidad: 1, precio_unitario: 1200 },
    { producto: "Mouse", cantidad: 2, precio_unitario: 25 },
    { producto: "Teclado", cantidad: 3, precio_unitario: 45 },
    { producto: "Monitor", cantidad: 1, precio_unitario: 200 },
    { producto: "Impresora", cantidad: 1, precio_unitario: 150 },
    { producto: "Laptop", cantidad: 2, precio_unitario: 1200 },
    { producto: "Mouse", cantidad: 1, precio_unitario: 25 },
    { producto: "Teclado", cantidad: 1, precio_unitario: 45 },
    { producto: "Monitor", cantidad: 2, precio_unitario: 200 },
    { producto: "Impresora", cantidad: 1, precio_unitario: 150 }
]);
```
</details>

- Agrupamos por producto y sumamos la cantidad de venta_total (cantidad * precio_unitario):

```js
db.ventas.aggregate({
    $group: {
        _id: "$producto", // agrupamos por producto
        total_ventas: { $sum: { $multiply: ["$cantidad", "$precio_unitario"] } }
        // total_venta = cantidad * precio_unitario
    }
});
```

```json
[
  {
    "_id": "Teclado",
    "total_ventas": 360
  },
  {
    "_id": "Impresora",
    "total_ventas": 600
  },
  {
    "_id": "Laptop",
    "total_ventas": 7200
  },
  {
    "_id": "Mouse",
    "total_ventas": 150
  },
  {
    "_id": "Monitor",
    "total_ventas": 1200
  }
]
```

<hr style="height:1px; border:none; background-color:#e1e4e8;" />

### 6.

-> [Script](./scripts/script6.mongodb.js)

<hr style="height:1px; border:none; background-color:#e1e4e8;" />

### 7.

-> [Script](./scripts/script7.mongodb.js)

<hr style="height:1px; border:none; background-color:#e1e4e8;" />

### 8.

-> [Script](./scripts/script8.mongodb.js)

<hr style="height:1px; border:none; background-color:#e1e4e8;" />

### 9.

<hr style="height:1px; border:none; background-color:#e1e4e8;" />

### 10.

-> [Script](./scripts/script10.mongodb.js)
