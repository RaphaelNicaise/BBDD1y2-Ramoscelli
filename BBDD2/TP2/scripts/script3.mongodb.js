use("empresa");

db.empleados.find(
    {}, // esto indica que no hay filtro
    { _id: 0, nombre: 1, puesto: 1 } // 0 no selecciona, 1 si
);