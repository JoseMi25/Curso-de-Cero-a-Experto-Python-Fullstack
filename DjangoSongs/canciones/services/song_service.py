from django.shortcuts import get_object_or_404
from canciones.models import Cancion

def obtener_todas_las_canciones():
    return Cancion.objects.all().order_by('-id')

def crear_cancion(datos):
    cancion = Cancion(**datos)
    cancion.save()
    return cancion

def obtener_cancion_por_id(id_cancion):
    return get_object_or_404(Cancion, pk=id_cancion)

def actualizar_cancion(cancion_actual, nuevos_datos):
    cancion_actual.titulo = nuevos_datos['titulo']
    cancion_actual.artista = nuevos_datos['artista']
    cancion_actual.popularidad = nuevos_datos['popularidad']
    cancion_actual.save()
    return cancion_actual

def eliminar_cancion(id_cancion):
    cancion = get_object_or_404(Cancion, pk=id_cancion)
    cancion.delete()