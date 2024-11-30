DROP PROCEDURE IF EXISTS insertar_usuario;
DROP PROCEDURE IF EXISTS insertar_libro;
DROP PROCEDURE IF EXISTS insertar_prestamo;
DROP PROCEDURE IF EXISTS insertar_cuota;
DROP PROCEDURE IF EXISTS existe_cuota;
DROP FUNCTION IF EXISTS calcular_multa;
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
    IN fecha_prestamo DATE
)
BEGIN
    INSERT INTO prestamos (dni_usuario, lid, fecha_prestamo)
    VALUES (dni_usuario, lid, fecha_prestamo);
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

DELIMITER //

CREATE FUNCTION calcular_multa(
    fecha_prestamo DATE,
    fecha_devolucion DATE,
    dias_limite INT,
    monto_cuota DECIMAL(10,2)
) 
RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
    DECLARE dias_retraso INT;
    DECLARE dias_sobrepasados INT;
    DECLARE multa DECIMAL(10,2);

    IF fecha_devolucion IS NULL THEN
        SET fecha_devolucion = CURDATE();
    END IF;

    SET dias_retraso = DATEDIFF(fecha_devolucion, fecha_prestamo);
    
    SET dias_sobrepasados = dias_retraso - dias_limite;
    
    IF dias_sobrepasados <= 0 THEN
        SET multa = 0;
    ELSE
        SET multa = dias_sobrepasados * 0.03 * monto_cuota;
    END IF;

    RETURN multa;
END //

DELIMITER ;

