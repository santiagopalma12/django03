# personas/views.py
from django.shortcuts import render
from .models import Persona
from .forms import PersonaForm

def personaTestView(request):
    obj = Persona.objects.get(id=1)
    context = {
        'objeto': obj
    }
    return render(request, "personas/descripcion.html", context)

def personaCreateView(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            form = PersonaForm()
    else: 
        form = PersonaForm()
    
    context = { 'form': form }
    return render(request, "personas/personasCreate.html", context)

def searchForHelp(request):
    return render(request, "personas/search.html")

