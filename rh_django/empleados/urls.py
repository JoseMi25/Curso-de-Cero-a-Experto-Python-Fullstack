from django.urls import path
from .views import EmpleadoListCreateView, EmpleadoDetailView

urlpatterns = [
    # http://localhost:8080/api/empleados
    path('empleados', EmpleadoListCreateView.as_view(), name='empleado-list-create'),
    
    # http://localhost:8080/api/empleados/1
    path('empleados/<int:pk>', EmpleadoDetailView.as_view(), name='empleado-detail'),
]