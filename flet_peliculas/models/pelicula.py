from sqlalchemy import Column, Integer, String
from database import Base


class Pelicula(Base):
    __tablename__ = "peliculas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(100), nullable=False)
    director = Column(String(100), nullable=False)
    puntuacion = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Pelicula(titulo='{self.titulo}', director='{self.director}')>"
