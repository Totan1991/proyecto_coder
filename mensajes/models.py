from django.db import models

class comentarios(models.Model):
    Nombre = models.CharField(max_length=250)
    email = models.EmailField()
    fecha = models.DateField()
    comentario = models.CharField(max_length=3000)