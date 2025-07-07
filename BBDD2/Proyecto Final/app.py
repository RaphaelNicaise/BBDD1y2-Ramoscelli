from flask import Flask, render_template

from routes.productos import productos_bp
from routes.proveedores import proveedores_bp
from routes.movimientos import movimientos_bp

from database.conn_database import client_db

from models.producto import obtener_productos   

app = Flask(__name__)

app.register_blueprint(productos_bp, url_prefix='/api')
app.register_blueprint(proveedores_bp, url_prefix='/api')
app.register_blueprint(movimientos_bp, url_prefix='/api')



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/agregarproducto')
def agregar_producto():
    proveedores = list(client_db['proveedores'].find({}, {"_id": 1, "nombre": 1}))
    for p in proveedores:
        p['_id'] = str(p['_id'])
    return render_template('agregar_producto.html', proveedores=proveedores)

@app.route('/productos')
def listar_productos():
    productos = obtener_productos()
    
    for p in productos: 
        p['_id'] = str(p['_id'])
        if 'proveedorId' in p:
            p['proveedorId'] = str(p['proveedorId'])
        p['precio'] = float(p['precio'])  

    return render_template('productos.html', productos=productos)
    
    
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=5000)