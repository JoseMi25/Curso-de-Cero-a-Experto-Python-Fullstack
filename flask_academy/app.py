import os
from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
from extensions import init_extensions
from models import Curso 
from forms import CursoForm # Importamos el formulario
from services.curso_service import obtener_curso_por_id, obtener_todos, eliminar_curso as servicio_eliminar_curso, editar_curso as servicio_editar_curso, agregar_curso as servicio_agregar_curso


# Cargar variables de entorno desde el archivo .env
load_dotenv()

def create_app():
    app = Flask(__name__)

    # --- Configuración de Flask ---
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    # --- Configuración de Base de Datos MySQL (FASE 2) ---
    DB_USER = os.getenv('DB_USERNAME')
    DB_PASS = os.getenv('DB_PASSWORD')
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_NAME = os.getenv('DB_NAME')

    # Construcción de la URI de conexión a MySQL con pymysql como driver
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    # Desactivamos una advertencia de SQLAlchemy que no es necesaria en este proyecto
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # --- Inicialización de Extensiones (FASE 2) ---
    init_extensions(app) # Inicializa db y migrate

    # --- Rutas de la Aplicación ---

    @app.route('/')
    def index():
        """Ruta principal: Llama al servicio para obtener la lista de cursos."""

        # 1. Llamada a la capa de servicios para obtener los datos.
        cursos = obtener_todos()

        # 2. Renderizar la plantilla, pasando la lista de cursos a través de 'cursos'
        return render_template('index.html', cursos=cursos)
    
    @app.route('/agregar', methods=['GET', 'POST'])
    def agregar_curso():
        """Ruta para mostrar y procesar el formulario de creación de cursos."""
        form = CursoForm()

        # Comprueba si el formulario fue enviado y si los datos son válidos
        if form.validate_on_submit():
            # Extracción de datos validados
            nombre = form.nombre.data
            instructor = form.instructor.data
            duracion = form.duracion.data

            # Llamada a la capa de servicios para la lógica de inserción
            servicio_agregar_curso(nombre, instructor, duracion)

            # Mensaje de éxito (se implementará un mecanismo de flash más adelante, por ahora solo redireccionamos)
            print(f"Curso '{nombre}' agregado exitosamente.")

            # Redireccionar al index para ver el curso recién agregado
            return redirect(url_for('index'))

        # Si es GET o la validación falló, muestra el formulario
        return render_template('agregar_curso.html', form=form, en_agregar=True)
    
    @app.route('/editar/<int:id_curso>', methods=['GET', 'POST'])
    def editar_curso(id_curso):
        """
        Ruta para editar un curso existente.
        <int:id_curso> define un parámetro en la URL que es un entero.
        """
        # 1. Obtener el objeto Curso desde el servicio (maneja 404 si no existe)
        curso = obtener_curso_por_id(id_curso)
        form = CursoForm(obj=curso) # Instancia el formulario, precargando los datos del objeto 'curso'

        # 2. Manejar la petición POST (Envío de formulario)
        if form.validate_on_submit():
            nombre = form.nombre.data
            instructor = form.instructor.data
            duracion = form.duracion.data

            # Llamada al servicio para actualizar
            servicio_editar_curso(curso, nombre, instructor, duracion)

            print(f"Curso '{nombre}' actualizado exitosamente.")

            # Redireccionar al index
            return redirect(url_for('index'))

        # 3. Manejar la petición GET (Mostrar formulario)
        # Como usamos form = CursoForm(obj=curso), los campos ya están precargados.
        # También pasamos el objeto curso a la plantilla para mostrar el nombre en el título.
        return render_template('editar_curso.html', form=form, curso=curso)
    
    @app.route('/eliminar/<int:id_curso>', methods=['POST'])
    def eliminar_curso(id_curso):
        """Ruta para eliminar un curso."""

        # Solo permitimos la eliminación si la petición es POST (enviada desde el modal)
        if request.method == 'POST':

            nombre_curso = servicio_eliminar_curso(id_curso)

            # Mensaje de éxito
            flash(f"Curso '{nombre_curso}' eliminado exitosamente.", 'danger')

            # Redireccionar al index
            return redirect(url_for('index'))

        # Si alguien intenta acceder por GET, lo redireccionamos
        return redirect(url_for('index'))
    
    return app


# Inicialización de la aplicación
if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', debug=True)