CREATE DATABASE IF NOT EXISTS biblioteca;

USE biblioteca;

DROP TABLE IF EXISTS Cuotas;
DROP TABLE IF EXISTS Prestamos;
DROP TABLE IF EXISTS Libros;
DROP TABLE IF EXISTS Usuarios;

CREATE TABLE usuarios (
    dni CHAR(20) PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    telefono VARCHAR(15) NOT NULL,
    fecha_registro DATE NOT NULL 
);


CREATE TABLE Libros (
    lid INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    genero VARCHAR(50),
    editorial VARCHAR(100),
    anio_publicacion YEAR
);

CREATE INDEX idx_titulo ON Libros(titulo);
CREATE INDEX idx_autor ON Libros(autor);

CREATE TABLE Prestamos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dni_usuario CHAR(20) NOT NULL,
    lid INT NOT NULL,
    fecha_prestamo DATE NOT NULL,
    fecha_devolucion DATE,
    FOREIGN KEY (dni_usuario) REFERENCES Usuarios(dni) ON DELETE CASCADE,
    FOREIGN KEY (lid) REFERENCES Libros(lid) ON DELETE CASCADE
);

CREATE TABLE Cuotas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dni_usuario CHAR(20) NOT NULL,
    monto DECIMAL(10, 2) NOT NULL,
    mes INT NOT NULL,
    anio INT NOT NULL,
    estado_pago ENUM('PENDIENTE', 'PAGADO') DEFAULT 'PENDIENTE',
    FOREIGN KEY (dni_usuario) REFERENCES Usuarios(dni) ON DELETE CASCADE,
    UNIQUE (dni_usuario, mes, anio)
);

