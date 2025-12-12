from django.shortcuts import render, redirect
from canciones.services import song_service
from .forms import CancionForm

def index(request):
    canciones = song_service.obtener_todas_las_canciones()
    context = {'canciones': canciones}
    return render(request, 'index.html', context)

def crear_cancion(request):
    if request.method == 'POST':
        form = CancionForm(request.POST)
        if form.is_valid():
            song_service.crear_cancion(form.cleaned_data)
            return redirect('index')
    else:
        form = CancionForm()

    return render(request, 'canciones_form.html', {
        'form': form,
        'titulo_pagina': 'Registrar Canción'
    })

def editar_cancion(request, id):
    cancion = song_service.obtener_cancion_por_id(id)

    if request.method == 'POST':
        form = CancionForm(request.POST, instance=cancion)
        if form.is_valid():
            song_service.actualizar_cancion(cancion, form.cleaned_data)
            return redirect('index')
    else:
        form = CancionForm(instance=cancion)

    return render(request, 'canciones_form.html', {
        'form': form,
        'titulo_pagina': 'Editar Canción'
    })

def eliminar_cancion(request, id):
    # Solo permitimos eliminar si es una petición POST
    if request.method == 'POST':
        song_service.eliminar_cancion(id)
    return redirect('index')