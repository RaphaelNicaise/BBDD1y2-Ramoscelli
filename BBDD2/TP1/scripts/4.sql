CREATE TABLE datos (
    id INT,
    palabra VARCHAR(10)
)

EXPLAIN SELECT * FROM datos WHERE palabra = 'efgh2';

CREATE INDEX idx_palabra ON datos (palabra);

EXPLAIN SELECT * FROM datos WHERE palabra = 'efgh2';