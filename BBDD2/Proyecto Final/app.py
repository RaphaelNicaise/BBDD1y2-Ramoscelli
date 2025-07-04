from flask import Flask

from routes.productos import productos_bp
from routes.proveedores import proveedores_bp
from routes.movimientos import movimientos_bp

app = Flask(__name__)

app.register_blueprint(productos_bp)
app.register_blueprint(proveedores_bp)
app.register_blueprint(movimientos_bp)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=5000)