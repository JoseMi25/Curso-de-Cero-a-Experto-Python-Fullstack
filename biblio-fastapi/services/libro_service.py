from sqlalchemy.orm import Session
from models.libro import Libro
import schemas

def listar_libros(db: Session):
    """
    Obtiene todos los registros de la tabla 'libros'.
    """
    return db.query(Libro).all()

def crear_libro(db: Session, datos: schemas.LibroCreate):
    """
    Crea un nuevo registro en la base de datos.
    """
    nuevo_libro = Libro(**datos.model_dump())
    db.add(nuevo_libro)
    db.commit()
    db.refresh(nuevo_libro)
    return nuevo_libro

def obtener_libro_por_id(db: Session, id: int):
    """
    Busca un libro específico por su llave primaria.
    """
    return db.query(Libro).filter(Libro.id == id).first()

def actualizar_libro(db: Session, id: int, datos: schemas.LibroUpdate):
    """
    Actualiza los campos de un libro existente.
    """
    libro_db = db.query(Libro).filter(Libro.id == id).first()
    
    if not libro_db:
        return None
    
    for key, value in datos.model_dump().items():
        setattr(libro_db, key, value)
    
    db.commit()
    db.refresh(libro_db)
    
    return libro_db

# Función para eliminar un libro
def eliminar_libro(db: Session, id: int):
    """
    Elimina un libro de la base de datos por su ID.
    
    :param db: Sesión de BD.
    :param id: ID del libro a eliminar.
    :return: El objeto eliminado si existía, o None si no se encontró.
    """
    # 1. Buscamos el libro
    libro = db.query(Libro).filter(Libro.id == id).first()
    
    # 2. Si no existe, retornamos None
    if not libro:
        return None
    
    # 3. Borramos el registro
    db.delete(libro)
    
    # 4. Confirmamos la transacción
    db.commit()
    
    return libro