from flask import Flask, render_template

from database.conn_database import client_db
from database.seed import seed_data

from routes.productos import productos_bp
from routes.proveedores import proveedores_bp
#from routes.movimientos import movimientos_bp

app = Flask(__name__)

seed_data(client_db)

@app.route('/')
def home():
    return render_template('home.html')


app.register_blueprint(productos_bp, url_prefix='/productos')
app.register_blueprint(proveedores_bp, url_prefix='/proveedores')


@app.route('/movimientos')
def movimientos():
    return render_template('movimientos.html')

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=5000)