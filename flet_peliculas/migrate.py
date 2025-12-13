import os
import sys
from sqlalchemy import text
from database import engine

def run_migrations():
    print("🚀 Iniciando proceso de migración...")

    # 1. Limpiar estado de migraciones previas (opcional, útil en dev inicial)
    # Esto asegura que si borraste la tabla manual, Alembic no se confunda
    try:
        with engine.connect() as connection:
            # Verificamos si existe la tabla de control de versiones
            connection.execute(text("DROP TABLE IF EXISTS alembic_version"))
            connection.commit()
            print("🧹 Tabla 'alembic_version' limpiada/verificada.")
    except Exception as e:
        print(f"⚠️  Advertencia al limpiar alembic_version: {e}")

    # 2. Generar nueva migración
    # Equivalente a: alembic revision --autogenerate -m "Inicial"
    print("📦 Generando archivo de migración...")
    result_rev = os.system('alembic revision --autogenerate -m "Migracion Inicial"')
    
    if result_rev != 0:
        print("❌ Error al generar la revisión. Verifica tus modelos.")
        return

    # 3. Aplicar cambios a la BD
    # Equivalente a: alembic upgrade head
    print("🔄 Aplicando cambios a la base de datos...")
    result_upg = os.system('alembic upgrade head')

    if result_upg == 0:
        print("✅ ¡Migración exitosa! Tablas creadas correctamente.")
    else:
        print("❌ Error al aplicar la migración.")

if __name__ == "__main__":
    run_migrations()