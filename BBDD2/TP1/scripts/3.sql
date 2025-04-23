-- Crear la base de datos y usarla
CREATE DATABASE banco;
USE banco;

-- Crear la tabla de cuentas
CREATE TABLE Cuentas(
    id_cuenta INT PRIMARY KEY,
    nombre VARCHAR(50),
    saldo DECIMAL(10,2)
);

-- Insertar una cuenta de ejemplo
INSERT INTO Cuentas(id_cuenta, nombre, saldo)
VALUES (1, 'santiago', 1000.00);

-- Verificar inserción
SELECT * FROM Cuentas;

-- --------------------------
-- TRANSACTION A (en pestaña 1) con READ COMMITTED
-- --------------------------

-- Primero establecer el nivel de aislamiento
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

-- Luego iniciar la transacción
START TRANSACTION;

-- Ver saldo actual
SELECT saldo FROM Cuentas WHERE id_cuenta = 1;

-- Restar $200
UPDATE Cuentas SET saldo = saldo - 200 WHERE id_cuenta = 1;

-- No hacer COMMIT todavía (para simular concurrencia)
-- COMMIT;

-- --------------------------
-- TRANSACTION B (en pestaña 2) con READ COMMITTED
-- --------------------------

-- Primero establecer el nivel de aislamiento
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

-- Luego iniciar la transacción
START TRANSACTION;

-- Ver saldo actual
SELECT saldo FROM Cuentas WHERE id_cuenta = 1;

-- Restar $300
UPDATE Cuentas SET saldo = saldo - 300 WHERE id_cuenta = 1;

-- No hacer COMMIT todavía (para simular concurrencia)
-- COMMIT;

-- --------------------------
-- TRANSACTION A (en pestaña 1) con SERIALIZABLE
-- --------------------------

-- Primero establecer el nivel de aislamiento
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;

-- Luego iniciar la transacción
START TRANSACTION;

-- Ver saldo actual
SELECT saldo FROM Cuentas WHERE id_cuenta = 1;

-- Restar $200
UPDATE Cuentas SET saldo = saldo - 200 WHERE id_cuenta = 1;

-- No hacer COMMIT todavía (para simular concurrencia)
-- COMMIT;

-- --------------------------
-- TRANSACTION B (en pestaña 2) con SERIALIZABLE
-- --------------------------

-- Primero establecer el nivel de aislamiento
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;

-- Luego iniciar la transacción
START TRANSACTION;

-- Ver saldo actual
SELECT saldo FROM Cuentas WHERE id_cuenta = 1;

-- Restar $300
UPDATE Cuentas SET saldo = saldo - 300 WHERE id_cuenta = 1;

-- No hacer COMMIT todavía (para simular concurrencia)
-- COMMIT;