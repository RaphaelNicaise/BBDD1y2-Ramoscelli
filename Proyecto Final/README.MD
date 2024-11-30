
### DBML
![Database Schema](images/dbdiagram.png)

### Levantar Proyecto

1. **Clonando el repositorio, te vas a encontrar con la carpeta Proyecto Final, entra en ella.**
```bash
cd '.\Proyecto Final\'
```

2. **Correr en MySQL, los 3 scripts que se encuentran en la carpeta [SQL](sql)**:
    - 1. schema.sql
    - 2. procedures.sql
    - 3. testingdata.sql

3. **Crear un entorno virtual:**
```bash
python -m venv venv
```

4. **Activar el entorno virtual:**
```bash
.\venv\Scripts\Activate
```

5. **Instalar las dependencias**:
```bash
pip install -r requirements.txt
```

6. **En el archivo [Database.py](database.py), modificar las credenciales de la base de datos:**
```python
self.conn = mysql.connector.connect(
        host=tu_host,
        user=tu_user,
        password=tu_password,
        database="biblioteca",
        port=tu_port,
)
```

7. **Por ultimo correr la aplicacion:**
```bash
py app.py
```

