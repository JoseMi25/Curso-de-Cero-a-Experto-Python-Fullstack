from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # URLs de la app empleados
    path('api/', include('empleados.urls')),
]