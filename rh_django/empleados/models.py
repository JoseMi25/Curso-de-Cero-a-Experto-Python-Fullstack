from django.db import models

class Empleado(models.Model):
    idEmpleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, blank=False, null=False)
    departamento = models.CharField(max_length=100, blank=False, null=False)
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'empleado' # Nombre específico de la tabla en MySQL

    def __str__(self):
        return self.nombre