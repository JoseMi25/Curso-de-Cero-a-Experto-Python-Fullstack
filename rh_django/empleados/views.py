from rest_framework import generics
from .models import Empleado
from .serializers import EmpleadoSerializer

# GET (listar) y POST (crear)
class EmpleadoListCreateView(generics.ListCreateAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

# GET (detalle), PUT (actualizar) y DELETE (eliminar) por ID
class EmpleadoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    lookup_field = 'pk' # Busca por clave primaria (idEmpleado)