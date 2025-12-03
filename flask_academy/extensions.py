from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Inicializamos las extensiones sin asociarlas a la app (Patrón de Extensión)
# Esto permite que sean importadas en otros módulos (como models.py) sin 
# problemas de importaciones circulares, y luego se inicializan en app.py.

db = SQLAlchemy()
migrate = Migrate()

def init_extensions(app):
    """Asocia las extensiones a la instancia de la aplicación Flask."""
    db.init_app(app)
    migrate.init_app(app, db)