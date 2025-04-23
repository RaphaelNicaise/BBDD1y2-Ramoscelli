drop index idx_precio_categoria on productos;

explain SELECT * FROM productos
WHERE precio > 1400 AND stock >499;



CREATE INDEX idx_precio ON productos(precio);
explain SELECT * FROM productos
WHERE precio > 1400 AND stock >499;

CREATE INDEX idx_categoria ON productos(categoria_id);
explain SELECT * FROM productos
WHERE precio > 1400 AND stock >499;



CREATE INDEX idx_precio_stock ON productos(precio, stock);
explain SELECT * FROM productos
WHERE precio > 1400 AND stock >499;

SHOW INDEXES FROM productos;