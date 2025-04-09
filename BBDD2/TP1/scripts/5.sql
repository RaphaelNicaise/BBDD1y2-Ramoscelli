CREATE TABLE ventas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    producto VARCHAR(100),
    cantidad INT,
    fecha DATE
);

CREATE VIEW resumen_mensuales AS
SELECT producto, YEAR(fecha) AS anio, MONTH(fecha) AS mes, SUM(cantidad) AS total
FROM ventas
GROUP BY producto, anio, mes;

INSERT INTO ventas (producto, cantidad, fecha) VALUES
('Laptop', 3, '2024-01-15'),
('Laptop', 2, '2024-01-20'),
('Laptop', 5, '2024-02-10'),
('Mouse', 10, '2024-01-05'),
('Mouse', 7, '2024-02-07'),
('Mouse', 3, '2024-02-28'),
('Teclado', 4, '2024-01-12'),
('Teclado', 6, '2024-03-03'),
('Monitor', 2, '2024-01-25'),
('Monitor', 4, '2024-03-10');

SELECT producto, SUM(total_vendido) AS total
FROM resumen_mensual
GROUP BY producto
ORDER BY total DESC
LIMIT 5;