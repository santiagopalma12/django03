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
