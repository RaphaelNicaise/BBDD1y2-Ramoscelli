INSERT INTO usuarios (dni, nombre, apellido, email, telefono, fecha_registro) VALUES
('1234567890', 'Juan', 'Perez', 'juan.perez@mail.com', '1234567890', '2023-01-15'),
('2345678901', 'Maria', 'Lopez', 'maria.lopez@mail.com', '2345678901', '2023-02-20'),
('3456789012', 'Carlos', 'Martinez', 'carlos.martinez@mail.com', '3456789012', '2023-03-18'),
('4567890123', 'Ana', 'Garcia', 'ana.garcia@mail.com', '4567890123', '2023-04-10'),
('5678901234', 'Luis', 'Hernandez', 'luis.hernandez@mail.com', '5678901234', '2023-05-14'),
('6789012345', 'Laura', 'Rodriguez', 'laura.rodriguez@mail.com', '6789012345', '2023-06-30'),
('7890123456', 'Pedro', 'Martinez', 'pedro.martinez@mail.com', '7890123456', '2023-07-22'),
('8901234567', 'Sofia', 'Gonzalez', 'sofia.gonzalez@mail.com', '8901234567', '2023-08-19'),
('9012345678', 'Miguel', 'Fernandez', 'miguel.fernandez@mail.com', '9012345678', '2023-09-25'),
('0123456789', 'Elena', 'Perez', 'elena.perez@mail.com', '0123456789', '2023-10-05');


INSERT INTO libros (titulo, autor, genero, editorial, anio_publicacion) VALUES
('La sombra del viento', 'Carlos Ruiz Zafon', 'Ficcion', 'Planeta', 2001),
('Los hombres que no amaban a las mujeres', 'Stieg Larsson', 'Misterio', 'Norstedts Förlag', 2005),
('El codigo Da Vinci', 'Dan Brown', 'Misterio', 'Doubleday', 2003),
('Crepusculo', 'Stephenie Meyer', 'Romance', 'Little, Brown and Company', 2005),
('Los juegos del hambre', 'Suzanne Collins', 'Ciencia Ficcion', 'Scholastic Press', 2008),
('Harry Potter y la piedra filosofal', 'J.K. Rowling', 'Ficcion', 'Bloomsbury', 1997),
('El nombre del viento', 'Patrick Rothfuss', 'Ficcion', 'DAW Books', 2007),
('La chica del tren', 'Paula Hawkins', 'Misterio', 'Riverhead Books', 2015),
('El marciano', 'Andy Weir', 'Ciencia Ficcion', 'Crown Publishing Group', 2011),
('La verdad sobre el caso Harry Quebert', 'Joel Dicker', 'Misterio', 'Editions de Fallois', 2012);

INSERT INTO prestamos (dni_usuario, lid, fecha_prestamo, fecha_devolucion) VALUES
('1234567890', 1, '2024-09-15', '2024-09-22'),  -- Devuelto a tiempo
('2345678901', 2, '2024-09-20', '2024-09-27'),  -- Devuelto a tiempo
('3456789012', 3, '2024-10-05', NULL),  -- No devuelto aún
('4567890123', 4, '2024-10-10', '2024-10-17'),  -- Devuelto a tiempo
('5678901234', 5, '2024-10-15', NULL),  -- No devuelto aún
('6789012345', 6, '2024-10-20', '2024-10-27'),  -- Devuelto a tiempo
('7890123456', 7, '2024-11-01', NULL),  -- No devuelto aún
('8901234567', 8, '2024-11-05', '2024-11-12'),  -- Devuelto a tiempo
('9012345678', 9, '2024-09-25', '2024-10-02'),  -- Devuelto a tiempo
('0123456789', 10, '2024-10-10', NULL);  -- No devuelto aún

INSERT INTO cuotas (dni_usuario, monto, mes, anio, estado_pago) VALUES
('2345678901', 50.00, 10, 2024, 'PAGADO'),
('3456789012', 50.00, 10, 2024, 'PENDIENTE'),
('4567890123', 50.00, 10, 2024, 'PAGADO'),
('5678901234', 50.00, 10, 2024, 'PENDIENTE'),
('6789012345', 50.00, 10, 2024, 'PAGADO'),
('7890123456', 50.00, 10, 2024, 'PENDIENTE'),
('8901234567', 50.00, 10, 2024, 'PAGADO'),
('9012345678', 50.00, 10, 2024, 'PAGADO'),
('0123456789', 50.00, 10, 2024, 'PENDIENTE'),
('1234567890', 50.00, 11, 2024, 'PAGADO'),
('3456789012', 50.00, 11, 2024, 'PENDIENTE'),
('4567890123', 50.00, 11, 2024, 'PAGADO'),
('5678901234', 50.00, 11, 2024, 'PENDIENTE'),
('6789012345', 50.00, 11, 2024, 'PAGADO'),
('7890123456', 50.00, 11, 2024, 'PENDIENTE'),
('8901234567', 50.00, 11, 2024, 'PAGADO'),
('9012345678', 50.00, 11, 2024, 'PAGADO'),
('0123456789', 50.00, 11, 2024, 'PENDIENTE');