CRATE TABLE Alumnos (
    id INT AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
);

CREATE TABLE Materias (
    id INT AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    profesor VARCHAR(50) NOT NULL,
);

CREATE TABLE tabla_intermedia (
    id INT AUTO_INCREMENT,
    id_alumno INT,
    id_materia INT,
    PRIMARY KEY (id),
    FOREIGN KEY (id_alumno) REFERENCES Alumnos(id_alumno) ON DELETE CASCADE,
    FOREIGN KEY (id_materia) REFERENCES Materias(id_materia)
);