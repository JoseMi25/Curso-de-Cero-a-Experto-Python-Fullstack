from models import Curso
from extensions import db 

def obtener_todos():
    """
    Lógica de Negocio: Recupera todos los cursos. (FASE 4)
    """
    cursos = Curso.query.all()
    return cursos

def obtener_curso_por_id(id_curso):
    """
    Lógica de Negocio: Recupera un solo curso por su clave primaria (ID).
    Utiliza .get_or_404() para manejar automáticamente el error si no existe.
    """
    # .get_or_404() es un método de Flask-SQLAlchemy que busca por PK 
    # y lanza un error 404 si no encuentra el registro.
    curso = Curso.query.get_or_404(id_curso)
    return curso

def agregar_curso(nombre, instructor, duracion):
    """
    Lógica de Negocio: Crea un nuevo objeto Curso. (FASE 5)
    """
    nuevo_curso = Curso(
        nombre=nombre, 
        instructor=instructor, 
        duracion=duracion
    )
    db.session.add(nuevo_curso)
    db.session.commit()
    return nuevo_curso

def editar_curso(curso, nombre, instructor, duracion):
    """
    Lógica de Negocio: Actualiza un objeto Curso existente.
    """
    # 1. Modificar los atributos del objeto Curso ya cargado
    curso.nombre = nombre
    curso.instructor = instructor
    curso.duracion = duracion

    # 2. Hacer commit a la sesión para guardar los cambios
    # SQLAlchemy es lo suficientemente inteligente para saber que debe hacer un UPDATE.
    db.session.commit()
    return curso

def eliminar_curso(id_curso):
    """
    Lógica de Negocio: Busca un curso por ID y lo elimina.
    """
    # 1. Obtener el curso (get_or_404 ya maneja el caso de no encontrado)
    curso = obtener_curso_por_id(id_curso)

    # 2. Eliminar de la sesión
    db.session.delete(curso)

    # 3. Confirmar la eliminación
    db.session.commit()

    return curso.nombre