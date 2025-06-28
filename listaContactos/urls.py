# listaContactos/urls.py

from django.contrib import admin
from django.urls import path, include

# BORRA estas líneas, ya no las necesitas.
# from inicio.views import myHomeView
# from inicio.views import anotherView

urlpatterns = [
    path('admin/', admin.site.urls),

    # ESTA ES LA LÍNEA MÁS IMPORTANTE.
    # Hace que la página de inicio (ruta vacía '')
    # sea manejada por la app 'personas'.
    path('', include('personas.urls')),

    # BORRA estas rutas antiguas.
    # path('', myHomeView, name='PaginaInicio'),
    # path('another', anotherView, name='otra'),

    # La siguiente línea también la puedes borrar si la tienes,
    # porque la de arriba ya la reemplaza.
    # path('personas/', include('personas.urls')),
]