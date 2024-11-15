DROP PROCEDURE IF EXISTS insertar_usuario;
DROP PROCEDURE IF EXISTS insertar_libro;
DROP PROCEDURE IF EXISTS insertar_prestamo;
DROP PROCEDURE IF EXISTS insertar_cuota;
DROP PROCEDURE IF EXISTS existe_cuota;

-- PROCEDURES

DELIMITER //
CREATE PROCEDURE insertar_usuario(
    IN dni CHAR(20),
    IN nombre VARCHAR(50),
    IN apellido VARCHAR(50),
    IN email VARCHAR(100),
    IN telefono VARCHAR(15)
)
BEGIN
    INSERT INTO usuarios (dni, nombre, apellido, email, telefono, fecha_registro)
    VALUES (dni, nombre, apellido, email, telefono, CURDATE());
END //


CREATE PROCEDURE insertar_libro(
    IN titulo VARCHAR(200),
    IN autor VARCHAR(100),
    IN genero VARCHAR(50),
    IN editorial VARCHAR(100),
    IN anio_publicacion YEAR
)
BEGIN
    INSERT INTO libros (titulo, autor, genero, editorial, anio_publicacion)
    VALUES (titulo, autor, genero, editorial, anio_publicacion);
END //


DELIMITER //
CREATE PROCEDURE insertar_prestamo(
    IN dni_usuario CHAR(20),
    IN lid INT,
    IN fecha_prestamo DATE,
    IN fecha_devolucion DATE
)
BEGIN
    INSERT INTO prestamos (dni_usuario, lid, fecha_prestamo, fecha_devolucion)
    VALUES (dni_usuario, lid, fecha_prestamo, fecha_devolucion);
END //

DELIMITER //
CREATE PROCEDURE insertar_cuota(
    IN dni_usuario CHAR(20),
    IN monto DECIMAL(10, 2),
    IN mes INT,
    IN anio INT
)
BEGIN
    INSERT INTO cuotas (dni_usuario, monto, mes, anio)
    VALUES (dni_usuario, monto, mes, anio);
END //

