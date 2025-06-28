# personas/views.py
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Persona

class PersonaListView(ListView):
    model = Persona
    fields = ['nombres', 'apellidos', 'edad', 'donador']
class PersonaDetailView(DetailView):
    fields = ['nombres', 'apellidos', 'edad', 'donador']
    model = Persona