from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class CursoForm(FlaskForm):
    """
    Formulario para crear y editar un curso.
    Utiliza validadores de WTForms para asegurar la integridad de los datos.
    """
    # Campo 'nombre' del curso
    nombre = StringField('Nombre del Curso', validators=[
        DataRequired(message="El nombre es obligatorio."),
        Length(min=3, max=100, message="El nombre debe tener entre 3 y 100 caracteres.")
    ])

    # Campo 'instructor'
    instructor = StringField('Instructor', validators=[
        DataRequired(message="El instructor es obligatorio."),
        Length(min=3, max=100)
    ])

    # Campo 'duracion', se necesita un DecimalField para manejar números flotantes
    duracion = DecimalField('Duración (horas)', places=2, validators=[
        DataRequired(message="La duración es obligatoria."),
        NumberRange(min=0.1, max=1000, message="La duración debe ser un número positivo.")
    ])

    # Botón de envío del formulario
    submit = SubmitField('Guardar Curso')