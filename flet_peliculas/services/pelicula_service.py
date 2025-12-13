from database import get_db
from models.pelicula import Pelicula

def obtener_todos():
    """Obtiene todas las películas de la base de datos"""
    db = next(get_db())
    try:
        peliculas = db.query(Pelicula).all()
        return peliculas
    finally:
        db.close()

# Función para guardar una nueva película
def crear_pelicula(titulo, director, puntuacion):
    if not titulo or not director:
        raise ValueError("El título y director son obligatorios")
    if not isinstance(puntuacion, int) or not (1 <= puntuacion <= 10):
        raise ValueError("La puntuación debe ser un entero entre 1 y 10")

    db = next(get_db())
    try:
        nueva_peli = Pelicula(titulo=titulo, director=director, puntuacion=puntuacion)
        db.add(nueva_peli)
        db.commit()
        db.refresh(nueva_peli)
        return nueva_peli
    finally:
        db.close()

# Función para buscar una película por su ID
def obtener_por_id(id_pelicula):
    db = next(get_db())
    try:
        # filter(Pelicula.id == id_pelicula) es el WHERE id = X en SQL
        pelicula = db.query(Pelicula).filter(Pelicula.id == id_pelicula).first()
        return pelicula
    finally:
        db.close()

# Función para actualizar una película existente
def actualizar_pelicula(id_pelicula, titulo, director, puntuacion):
    if not titulo or not director:
        raise ValueError("El título y director son obligatorios")
    
    db = next(get_db())
    try:
        pelicula = db.query(Pelicula).filter(Pelicula.id == id_pelicula).first()
        if pelicula:
            pelicula.titulo = titulo
            pelicula.director = director
            pelicula.puntuacion = puntuacion
            db.commit()
            db.refresh(pelicula)
            return pelicula
        return None
    finally:
        db.close()

# Función para eliminar una película
def eliminar_pelicula(id_pelicula):
    db = next(get_db())
    try:
        # 1. Buscamos la película
        pelicula = db.query(Pelicula).filter(Pelicula.id == id_pelicula).first()
        
        # 2. Si existe, la borramos
        if pelicula:
            db.delete(pelicula)
            db.commit()
            return True
        return False
    finally:
        db.close()

# Bloque de prueba
if __name__ == "__main__":
    # Intenta buscar el ID 1 (asegurate de que exista en tu BD)
    peli = obtener_por_id(1)
    if peli:
        print(f"✅ Encontrada: {peli.titulo} - Director: {peli.director}")
    else:
        print("❌ No se encontró la película con ID 1")     

    