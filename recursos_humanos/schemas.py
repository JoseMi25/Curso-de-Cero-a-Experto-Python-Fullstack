from marshmallow import fields
from extensions import ma
from models import Empleado

class EmpleadoSchema(ma.SQLAlchemyAutoSchema):
    # Sobrescribimos 'sueldo' para que se convierta a String al generar el JSON
    sueldo = fields.Decimal(as_string=True)

    class Meta:
        model = Empleado
        load_instance = True
        include_fk = True

# Instancias para usar en los controladores
empleado_schema = EmpleadoSchema()
empleados_schema = EmpleadoSchema(many=True)