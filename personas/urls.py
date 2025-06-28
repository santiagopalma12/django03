# personas/urls.py
from django.urls import path
from .views import (
    PersonaListView,
    PersonaDetailView,
    PersonaCreateView,
    PersonaUpdateView
)
app_name = 'personas'
urlpatterns = [
    path('', PersonaListView.as_view(), name='persona-list'),
    path('create/', PersonaCreateView.as_view(), name='persona-create'),
    path('<int:pk>/', PersonaDetailView.as_view(), name='persona-detail'),
    path('<int:pk>/update/', PersonaUpdateView.as_view(), name='persona-update'),
]
