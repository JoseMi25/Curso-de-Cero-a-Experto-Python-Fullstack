from extensions import db
from datetime import datetime

class Curso(db.Model):
    """
    Modelo para la tabla 'curso'.
    Representa un curso en el portal educativo Flask Academy.
    """
    # Define explícitamente el nombre de la tabla para claridad
    __tablename__ = 'curso' 

    # Columna de clave primaria (PK) y autoincrementable
    id_curso = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # Columna para el nombre del curso, no puede ser nulo, longitud máxima de 100
    nombre = db.Column(db.String(100), nullable=False)

    # Columna para el nombre del instructor
    instructor = db.Column(db.String(100), nullable=False)

    # Columna para la duración del curso (ej. 15.5 horas)
    duracion = db.Column(db.Numeric(precision=4, scale=2), nullable=False)

    # Columna para registrar la fecha y hora de creación del registro
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        """
        Método de representación para debugging, muestra una vista legible del objeto.
        """
        return f"<Curso {self.id_curso}: {self.nombre} - {self.instructor}>"