from sqlalchemy import Column, Integer, String
from database import Base

class Libro(Base):
    """
    Modelo SQLAlchemy que representa la tabla 'libros' en la base de datos.
    Hereda de 'Base' para quedar registrado en el ORM.
    """
    __tablename__ = "libros"

    # Definición de columnas
    # id: Llave primaria, se autoincrementa automáticamente
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    # titulo: Título del libro, no puede ser nulo. Definimos un límite de 100 caracteres.
    titulo = Column(String(100), nullable=False)

    # autor: Autor del libro, no puede ser nulo.
    autor = Column(String(100), nullable=False)

    # rating: Calificación del libro (1-5).
    # La validación estricta del rango (1-5) se hará usualmente en los esquemas Pydantic,
    # aunque aquí definimos que sea un entero obligatorio.
    rating = Column(Integer, nullable=False)