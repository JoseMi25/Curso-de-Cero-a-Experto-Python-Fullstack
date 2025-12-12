from django.contrib import admin
from .models import Cancion

# Opción 1: Registro simple
# admin.site.register(Cancion)

# Opción 2: Registro con decorador para personalizar la lista (Recomendado)
@admin.register(Cancion)
class CancionAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'artista', 'popularidad')
    search_fields = ('titulo', 'artista')
    list_filter = ('popularidad',)