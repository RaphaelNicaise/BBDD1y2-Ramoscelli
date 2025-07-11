# Proyecto Final - BBDD2

#### Participantes:
- [Raphael Nicaise](https://github.com/RaphaelNicaise)
- [Santiago Segal](https://github.com/Santucho12)
- [Abner Grgurich](https://github.com/Abner2646)
- [Nicolas Cordano](https://github.com/NACXIIX)


# Sistema de Inventario de Tienda
[`Consigna del proyecto`](docs/consigna.md) <<<


Tecnologias utilizadas:

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Pymongo](https://img.shields.io/badge/Pymongo-336791?style=for-the-badge&logo=pymongo&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)

### Deploy del proyecto con `docker-compose`:

El proyecto está dockerizado y se inicia fácilmente con `docker-compose`. Al ejecutar el comando, se levantan dos contenedores: uno para MongoDB y otro para la webapp desarrollada en Flask (definido por un Dockerfile). La webapp se conecta a la base de datos usando Pymongo en los modelos, y las rutas importan estos modelos para interactuar con la base de datos.

Al iniciar los contenedores, se ejecuta automáticamente un [script](/BBDD2/Proyecto%20Final/database/seed.py) que crea la base de datos, las colecciones necesarias y carga los datos iniciales. Si la aplicación detecta que no hay datos, vuelve a ejecutar el script para asegurar que siempre existan datos mínimos.

Para iniciar el proyecto:

```bash
docker-compose up
```

La webapp estará disponible en [localhost:5000](http://localhost:5000) y la base de datos se puede conectar usando la siguiente connection string:

```
mongodb://localhost:27017
```
### Estructura del proyecto:
```bash
Proyecto Final/
│   app.py
│   docker-compose.yml
│   Dockerfile
│   README.md
│   requirements.txt
├───database/
│   │   conn_database.py
│   │   seed.py
│   └───querys/
│           buscar_productos_con_stock_bajo.mongodb.js
│           eliminar_todo.mongodb.js
│           get_movimientos.mongodb.js
│           get_movimientos_por_fechas_mongodb.js
│           get_productos.mongodb.js       
│           init.mongodb.js
├───docs/
│       consigna.md
├───models/
│       model_movimiento.py
│       model_producto.py
│       model_proveedor.py
├───routes/
│       movimientos.py
│       productos.py
│       proveedores.py
├───static/
│       styles.css
├───templates/
│       base.html
│       editar_prod.html
│       home.html
│       movimientos.html
│       productos.html
│       proveedores.html
│       stock.html
```

- [`app.py`](app.py): Archivo Inicial de Flask
- [`docker-compose.yml`](docker-compose.yml): Config docker-compose para deployar
- [`Dockerfile`](Dockerfile): Dockerfile para la webapp flask
- [`requirements.txt`](requirements.txt): Requerimientos para el contenedor de Python
- [`database/conn_database.py`](database/conn_database.py): Conexión a la base de datos MongoDB
- [`database/seed.py`](database/seed.py): Script para inicializar la BBDD
- [`database/querys/`](database/querys/): Querys posteriormente usadas en pymongo
- [`docs/consigna.md`](docs/consigna.md): Consigna del proyecto
- [`models/`](models/): Modelos con lógica que traen los datos de la BBDD mediante consultas
- [`routes/`](routes/): Rutas de la webapp
- [`static/styles.css`](static/styles.css): Estilos CSS
- [`templates/`](templates/): Templates HTML de la webapp


### Ejemplo de uso de las funciones a implementar (ademas del CRUD):
Dar click en la imagen para ver el video de demostración:

[![Video de demostración](https://img.youtube.com/vi/l8z3X7C1F3A/0.jpg)](https://www.youtube.com/watch?v=l8z3X7C1F3A)




