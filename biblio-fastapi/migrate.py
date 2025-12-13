import os

def run_migrations():
    print("🔄 Generando migración automática...")
    
    # CORRECCIÓN:
    # 1. Usamos comillas dobles "..." para el mensaje (Windows lo requiere).
    # 2. Usamos un mensaje sin espacios "Creacion_inicial" para evitar cualquier error de argumentos.
    cmd_revision = 'alembic revision --autogenerate -m "Creacion_inicial"'
    
    result = os.system(cmd_revision)
    
    if result == 0:
        print("✅ Migración generada correctamente.")
        print("🚀 Aplicando cambios a la base de datos...")
        os.system("alembic upgrade head")
        print("✅ Base de datos actualizada con éxito.")
    else:
        print("❌ Error al generar la migración. Revisa tu configuración.")

if __name__ == "__main__":
    run_migrations()