# personas/views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy
from .models import Persona

class PersonaListView(ListView):
    model = Persona
    fields = ['nombres', 'apellidos', 'edad', 'donador']
class PersonaDetailView(DetailView):
    fields = ['nombres', 'apellidos', 'edad', 'donador']
    model = Persona
class PersonaDeleteView(DeleteView):
    model = Persona
    success_url = reverse_lazy('personas:persona-list')