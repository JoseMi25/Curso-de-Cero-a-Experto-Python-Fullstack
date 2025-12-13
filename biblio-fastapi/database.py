import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. Cargar variables de entorno desde el archivo .env
load_dotenv()

# 2. Obtener la URL de conexión
# Si no existe la variable, lanza un error o usa un valor por defecto (aquí confiamos en el .env)
DATABASE_URL = os.getenv("DATABASE_URL")

# 3. Crear el motor de base de datos (Engine)
# Este objeto gestiona la comunicación con MySQL
engine = create_engine(DATABASE_URL)

# 4. Crear la clase SessionLocal
# Será la fábrica para crear sesiones de base de datos en cada petición
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 5. Crear la clase Base
# Todos nuestros modelos (tablas) heredarán de esta clase
Base = declarative_base()

# 6. Dependencia get_db
# Se usará en los endpoints de FastAPI para obtener una sesión y cerrarla automáticamente
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 7. Prueba rápida de conexión (solo si ejecutamos este archivo directamente)
if __name__ == "__main__":
    try:
        # Intentamos conectar
        with engine.connect() as connection:
            print("¡Conexión a la base de datos exitosa! 🚀")
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")