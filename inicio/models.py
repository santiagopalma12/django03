from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100, blank=False)  
    edad = models.IntegerField()
    descripcion = models.TextField()
    email = models.EmailField(default="noemail@example.com")
    activo = models.BooleanField(null=True, default=True, blank=True)
    


