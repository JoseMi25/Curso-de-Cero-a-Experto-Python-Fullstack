from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_cors import CORS

# Inicializamos las instancias vacías.
# Se vincularán a la "app" más tarde en app.py
db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
cors = CORS()