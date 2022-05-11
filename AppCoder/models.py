
from distutils.command.upload import upload
from random import choices
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import ImageField


Tipo_habitaciones = (
    ('Standard Suite', 'Standard Suite'), 
    ('Junior Suite', 'Junior Suite'), 
    ('Deluxe Suite', 'Deluxe Suite'),
    ('Presidential Suite', 'Presidential Suite')
)


Tipo_Documento = (
    ('CI', 'CI'), 
    ('Pasaporte', 'Pasaporte'), 
    ('DNI', 'DNI')
)




class reserva(models.Model):

    id_reserva = models.AutoField(primary_key=True)
    nombre_cliente_reserva = models.CharField(max_length=250)
    qde_adultos_reserva = models.IntegerField ()
    qde_menores_reserva = models.IntegerField ()
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    tipo_habitacion_reserva = models.CharField(max_length=50,choices = Tipo_habitaciones)
    email_cliente_reserva = models.EmailField()
    documento = models.ImageField(upload_to ='media/documentos/')

class habitaciones(models.Model):
    numero_habitacion = models.IntegerField(primary_key=True)
    tipo_habitacion = models.CharField(max_length=250)
    camas = models.IntegerField()
    servicios_extras = models.BooleanField()
    
    
class cliente(models.Model):
    id_cliente = models.IntegerField(primary_key=True)
    nombre_cliente = models.CharField(max_length=250)
    nacionalidad_cliente = models.CharField(max_length=250)
    tipo_documento_cliente = models.CharField(max_length=250, choices=Tipo_Documento)
    nro_documento_cliente = models.IntegerField("")
    

class contactos(models.Model):
    id_contacto = models.IntegerField(primary_key=True)
    nombre_contacto = models.CharField(max_length=250)
    nacionalidad_contacto = models.CharField(max_length=250)
    tipo_documento_contacto = models.CharField(max_length=250)
    nro_documento_contacto = models.IntegerField("")
    email_contacto = models.EmailField()
    texto_consulta_contacto = models.CharField(max_length=3000)

class comentarios(models.Model):
    email_contacto = models.EmailField()
    tipo_habitacion = models.CharField(max_length=50,choices = Tipo_habitaciones)
    comentario = models.CharField(max_length=3000)

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)