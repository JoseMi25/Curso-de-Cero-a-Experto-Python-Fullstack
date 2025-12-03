from flask import request
from flask_restful import Resource
from extensions import db
from models import Empleado
from schemas import empleado_schema, empleados_schema

class EmpleadoListResource(Resource):
    def get(self):
        # Devuelve todos los empleados en formato JSON
        empleados = Empleado.query.all()
        return empleados_schema.dump(empleados)

    def post(self):
        # Recibe JSON, valida y crea un nuevo empleado
        data = request.get_json()
        try:
            nuevo_empleado = empleado_schema.load(data)
            db.session.add(nuevo_empleado)
            db.session.commit()
            return empleado_schema.dump(nuevo_empleado), 200
        except Exception as e:
            return {'message': 'Error al crear empleado', 'error': str(e)}, 400

class EmpleadoResource(Resource):
    def get(self, id_empleado):
        # Busca por ID o devuelve 404 si no existe
        empleado = Empleado.query.get_or_404(id_empleado)
        return empleado_schema.dump(empleado)

    def put(self, id_empleado):
        empleado = Empleado.query.get_or_404(id_empleado)
        data = request.get_json()

        # Actualización parcial
        if 'nombre' in data:
            empleado.nombre = data['nombre']
        if 'departamento' in data:
            empleado.departamento = data['departamento']
        if 'sueldo' in data:
            empleado.sueldo = data['sueldo']

        db.session.commit()
        return empleado_schema.dump(empleado)

    def delete(self, id_empleado):
        empleado = Empleado.query.get_or_404(id_empleado)
        db.session.delete(empleado)
        db.session.commit()
        return {'mensaje': 'Empleado eliminado con éxito'}, 200