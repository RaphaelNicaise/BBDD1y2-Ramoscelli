use("colegio");

db.cursos.aggregate([
    {
        $lookup: {
            from: "alumnos",
            localField: "_id", // campo id del curso
            foreignField: "cursos.curso", // campo id del curso en la coleccion alumnos
            as: "alumnos"
        }
    }
]);