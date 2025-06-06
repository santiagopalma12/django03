# tu_proyecto/urls.py
from django.contrib import admin
from django.urls import path
from inicio.views import myHomeView
from personas.views import personaTestView, personaCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myHomeView, name='home'),
    path('persona/', personaTestView, name='test-persona'), 
    path('persona/', personaTestView, name='test-persona'),
    path('agregar/', personaCreateView, name='create-persona'),
]