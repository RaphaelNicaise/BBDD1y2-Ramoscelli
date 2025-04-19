use("colegio");

db.createCollection("cursos");

db.createCollection("alumnos");

// id de los cursos para despues asociarlos a los alumnos
// ObjectId() genera un id unico para cada curso

const id_curso1 = ObjectId();
const id_curso2 = ObjectId();
const id_curso3 = ObjectId();
const id_curso4 = ObjectId();

// aca insertamos los cursos con su respectivo id ya creado

db.cursos.insertMany([
    {
        _id: id_curso1,
        nombre: "Probabilidad y Estadistica",
        profesor: "Juan Perez",
        clases:[
            {dia:"martes", hora:"8am", aula:"704"},
            {dia:"jueves", hora:"8am", aula:"704"}
        ]
    },
    {
        _id: id_curso2,
        nombre: "Programacion I",
        profesor: "Damian Ene",
        clases:[
            {dia:"lunes", hora:"8am", aula:"707"},
            {dia:"miercoles", hora:"8am", aula:"707"}
        ]
    },
    {
        _id: id_curso3,
        nombre: "Programacion II",
        profesor: "Damian Ene",

        clases:[
            {dia:"lunes", hora:"10am", aula:"203"},
            {dia:"miercoles", hora:"10am", aula:"203"}
        ]
    },
    {
        _id: id_curso4,
        nombre: "Base de Datos I",
        profesor: "Gustavo Ramoscelli",
        clases:[
            {dia:"martes", hora:"10am", aula:"704"},
            {dia:"jueves", hora:"10am", aula:"704"}
        ]
    }
]);

// aca insertamos los alumnos, cada uno con una lista de cursos asociados

db.alumnos.insertMany([
    {   
        _id: ObjectId(), 
        nombre: "Raphael", 
        apellido: "Nicaise", 
        cursos:[
            {curso: id_curso1, estado: "cursando"},
            {curso: id_curso2, estado: "aprobada", nota:9},
            {curso: id_curso3, estado:"aprobada", nota: 10},
            {curso: id_curso4, estado: "aprobada", nota: 9}
        ]
    },        
    {
        _id: ObjectId(), 
        nombre: "Nereo", 
        apellido: "Champagen",
        cursos:[
            {curso: id_curso1, estado: "cursando"},
            {curso: id_curso2, estado: "cursando"},
            {curso: id_curso4, estado: "aprobada", nota: 7},
        ]
    },
    {
        _id: ObjectId(), 
        nombre: "Leandro", 
        apellido: "Laspada",
        cursos:[
            {curso: id_curso1, estado: "cursando"},
            {curso: id_curso2, estado: "cursando"},
            {curso: id_curso3, estado: "aprobada", nota: 8},
            {curso: id_curso4, estado: "aprobada", nota: 9}
        ]
    },
    {
        _id: ObjectId(), 
        nombre: "Patrtricio", 
        apellido: "Sardelli",
        cursos:[
            {curso: id_curso1, estado: "cursando"},
            {curso: id_curso2, estado: "cursando"},
            {curso: id_curso3, estado:"aprobada", nota: 10},
            {curso: id_curso4, estado:"aprobada", nota: 9}
        ]
    }
]);