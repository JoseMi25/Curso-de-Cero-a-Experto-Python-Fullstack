from flask import Flask
from extensions import db, ma, migrate, cors
from api import api_bp

def create_app():
    app = Flask(__name__)

    # --- CONFIGURACIÓN BASE DE DATOS ---
    # CAMBIA 'root:admin' por tu usuario y contraseña real de MySQL
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin@localhost:3306/recursos_humanos_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar extensiones con la app
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)

    # Registrar el Blueprint con el prefijo /api
    app.register_blueprint(api_bp, url_prefix='/api')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=8080)