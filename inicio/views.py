from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def another(request):
    return HttpResponse(f"Usuario: {request.user} | ¿Autenticado? {request.user.is_authenticated}")

def myHomeView(request, *args, **kwargs):
    my_context = {
        "myText": "Esto es sobre nosotros",
        "myNumber": 123
    }
    return render(request, "home.html", my_context)

def myHomeView(request, *args, **kwargs):
    my_context = {
        "myText": "Esto es sobre nosotros",
        "myNumber": 123,
        "myList": [33, 44, 55, 12, 101] 
    }
    return render(request, "home.html", my_context)