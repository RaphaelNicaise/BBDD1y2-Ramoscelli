CREATE TABLE clientes(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    email VARCHAR(100)
);

CREATE TABLE auditoria_email_clientes(
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    email_cliente VARCHAR(100),
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id)
);

DELIMITER // --recordar cambiar el delimitador para crear el trigger
CREATE TRIGGER auditar_email_clientes_trigger
AFTER UPDATE ON clientes
FOR EACH ROW
BEGIN
    IF OLD.email <> NEW.email THEN
        INSERT INTO auditoria_email_clientes (id_cliente, email_cliente)
        VALUES (NEW.id, NEW.email);
    END IF;
END //

