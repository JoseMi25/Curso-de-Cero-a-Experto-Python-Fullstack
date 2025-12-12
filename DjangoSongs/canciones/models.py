from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Cancion(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    artista = models.CharField(max_length=200, verbose_name="Artista")
    popularidad = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        help_text="Puntuación del 1 al 10",
        verbose_name="Popularidad"
    )

    class Meta:
        db_table = 'cancion' # Nombre exacto en la BD
        verbose_name = 'Canción'
        verbose_name_plural = 'Canciones'

    def __str__(self):
        return f"{self.titulo} - {self.artista}"