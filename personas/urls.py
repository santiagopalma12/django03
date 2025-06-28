# personas/urls.py
from django.urls import path
from .views import PersonaListView

app_name = 'personas'

urlpatterns = [
    path('', PersonaListView.as_view(), name='persona-list'),
]