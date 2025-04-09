# TP1 Bases de Datos 2

#### Participantes:
- [Raphael Nicaise]("")
- [Santiago Segal]("")
- [Abner Grgurich]("")
- [Nicolas Cordano]("")

> ℹ️ Para algunos puntos se requiere el uso de una base de datos, por eso aprovechamos el poder la nube, y levantamos una base de datos en AWS. En este caso, utilizamos Amazon RDS para crear una base de datos MySQL, y mediante un RDBMS, en nuestro caso DBEaver, conectamos a la base de datos y ejecutamos los scripts.


## 1.
Teniendo una tabla intermedia que relaciona a los alumnos y las materias mediante sus respectivos ID:
<img src="assets/tablasp1.png" alt="Description of image">

Una posible violacion de la integridad referencial ocurre en el caso que eliminemos a un alumno de la tabla alumnos. En este caso, la tabla intermedia quedaria con un registro que no tiene un alumno asociado. Esto porque la tabla intermedia depende de la tabla alumnos para su existencia.

Para resolver esto podemos hacer lo siguiente al crear la tabla (o aplicarle alter table):
```sql
    CREATE TABLE tabla_intermedia (
    id INT AUTO_INCREMENT,
    id_alumno INT,
    id_materia INT,
    PRIMARY KEY (id),
    FOREIGN KEY (id_alumno) REFERENCES Alumnos(id_alumno) ON DELETE CASCADE,
    FOREIGN KEY (id_materia) REFERENCES Materias(id_materia)
);

```

Le agregamos una constraint al campo id_alumno (fk de alumnos) `ON DELETE CASCADE`, el cual hace que si detecta que se elimina un registro de la tabla alumnos, elimine todos los registros de la tabla intermedia que tengan ese id_alumno, resolviendo asi el problema.



## 2.

## 3.

## 4.
Primero debemos crear una tabla en nuestra base de datos en AWS e ingresarle datos, yo decidi crear un script simple para crear 100.000 registros en csv y despues insertarlos a la tabla.

```sql
CREATE TABLE datos (
    id INT,
    palabra VARCHAR(10)
)
```

Creamos archivo `datos_100k.csv`:
```python
import pandas as pd
import random

palabras = ['abcd1', 'efgh2', 'sdfsd3', 'jahif4']

data = {
    'id': range(1, 100001),
    'palabra': [random.choice(palabras) for _ in range(100000)]
}

df = pd.DataFrame(data)

df.to_csv('datos_100k.csv', index=False)
```
- Los insertamos con la herramienta de import data from csv y ya estarian los 100.000 registros listos.

<img src="assets/dbeaverp4.png">

- Ahora si, ejecutamos la siguiente query sin index:
```sql
EXPLAIN SELECT * FROM datos WHERE palabra = 'efgh2';
```
Salida:
| Tiempo de Ejecucion        | type     | rows     |
|---------------|---------------|---------------|
| 0.50s       | All    | 100.000    |


Ahora creamos un index sobre la columna palabra:
```sql
CREATE INDEX idx_palabra ON datos (palabra);
```
Y ejecutamos la misma query:
```sql
EXPLAIN SELECT * FROM datos WHERE palabra = 'efgh2';
```
Salida:
| Tiempo de Ejecucion        | type     | rows     |
|---------------|---------------|---------------|
| 0.001s       | ref    | 44792   |

> ✅ El tiempo de ejecucion bajo considerablemente, y el tipo de busqueda cambio a ref, lo que indica que ahora se esta utilizando el index para buscar los registros.

### 5.

### 6.

### 7.

Creamos un usuario analista y le damos permisos de solo lectura a la base de datos:
```sql
CREATE USER 'analista'@'%' IDENTIFIED BY 'analista123';
GRANT SELECT ON database_tp1.* TO 'analista'@'%';
FLUSH PRIVILEGES; -- esto es importante para que los cambios tengan efecto
```
Ejecutamos esta consulta para ver que permisos tiene:
```sql
SELECT User,Select_priv,Insert_priv  FROM mysql.user user WHERE user.`User` LIKE 'analista'
```
> ✅ Tiene permisos de SELECT pero no de INSERT, lo que indica que no puede modificar la base de datos.

Testiemos esto:
```sql
INSERT INTO datos (id, palabra) VALUES (100001, 'test');
```

> ❗ ERROR 1142 (42000): INSERT command denied to user 'analista'@'%' for table 'clientes'


### 8.
Vamos a crear la tabla Clientes y Auditoria Clientes:
```sql
CREATE TABLE clientes(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    email VARCHAR(100)
)

CREATE TABLE auditoria_email_clientes(
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    email_cliente VARCHAR(100),
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id)
)
```

En este ejemplo queremos registrar cuando un cliente actualiza su mail, procedemos a crear el trigger sobre la tabla clientes:
```sql
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
```
> ℹ️ La validacion (OLD.email <> NEW.email) la ponemos ya que el trigger se ejecutaria tambien si se cambia el nombre u otro campo, con eso aseguramos que solo se ejecute si el email cambia.

<image src="assets/dbeaverp8.png">

> ✅ Ahora cada vez que se actualice el email de un cliente, se insertara un registro en la tabla auditoria_email_clientes con el id del cliente y el nuevo email.

### 9.

