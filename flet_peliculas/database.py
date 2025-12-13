import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

# Obtener credenciales
user = os.getenv("DB_USER")
password = os.getenv("DB_PASS")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

# Construir URL de conexión para MySQL
# Estructura: mysql+pymysql://usuario:password@host:puerto/nombre_db
DATABASE_URL = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}"

# Crear el motor de conexión (Engine)
# echo=True permite ver las consultas SQL en la consola (útil para depurar)
engine = create_engine(DATABASE_URL, echo=True)

# Configurar la sesión para interactuar con la BD
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base para crear los modelos (tablas)
Base = declarative_base()

# Función para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Bloque de prueba de conexión
if __name__ == "__main__":
    try:
        with engine.connect() as connection:
            print("✅ ¡Conexión exitosa a la base de datos MySQL!")
    except Exception as e:
        print(f"❌ Error al conectar: {e}")