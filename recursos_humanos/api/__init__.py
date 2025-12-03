from flask import Blueprint
from flask_restful import Api
from api.empleados import EmpleadoListResource, EmpleadoResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Rutas
api.add_resource(EmpleadoListResource, '/empleados')
api.add_resource(EmpleadoResource, '/empleados/<int:id_empleado>')