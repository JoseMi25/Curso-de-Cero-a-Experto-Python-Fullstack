from extensions import db

class Empleado(db.Model):
    __tablename__ = 'empleados'

    # Definición de columnas según tus requerimientos
    idEmpleado = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    departamento = db.Column(db.String(100), nullable=False)
    sueldo = db.Column(db.Numeric(10, 2), nullable=False)

    def __repr__(self):
        return f'<Empleado {self.nombre}>'