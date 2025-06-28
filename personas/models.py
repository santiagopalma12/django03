# personas/models.py
from django.db import models
from django.urls import reverse

class Persona(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField()
    donador = models.BooleanField()

    def __str__(self):
        return self.nombres

    def get_absolute_url(self):
        return reverse("personas:persona-detail", kwargs={"pk": self.id})