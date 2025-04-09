CREATE USER 'analista'@'%' IDENTIFIED BY 'analista123';
GRANT SELECT ON database_tp1.* TO 'analista'@'%';
FLUSH PRIVILEGES; -- esto es importante para que los cambios tengan efecto

SELECT User,Select_priv,Insert_priv  FROM mysql.user user WHERE user.`User` LIKE 'analista';

INSERT INTO datos (id, palabra) VALUES (100001, 'test');