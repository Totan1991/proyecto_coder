from dataclasses import fields
from datetime import datetime,time
from distutils.util import change_root
from random import choices
from secrets import choice
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  
from django.forms.forms import Form  
from AppCoder.models import Tipo_Documento, Tipo_habitaciones


current_date =datetime.now()

class nueva_reserva(forms.Form):
  
    nombre_cliente_reserva = forms.CharField(required=True,max_length=250)
    qde_adultos_reserva = forms.IntegerField(required=True)
    qde_menores_reserva = forms.IntegerField(required=True)
    fecha_entrada = forms.DateField(required=True)
    fecha_salida = forms.DateField(required=True)
    tipo_habitacion_reserva = forms.CharField(max_length=50, widget=forms.Select(choices= Tipo_habitaciones))
    email_cliente_reserva = forms.EmailField(required=True)
    documento = forms.ImageField()



class nuevo_cliente(forms.Form):
    
    #id_cliente = forms.IntegerField()
    nombre_cliente = forms.CharField(max_length=250)
    nacionalidad_cliente = forms.CharField(max_length=250)
    tipo_documento_cliente = forms.CharField(max_length=50, widget=forms.Select(choices= Tipo_Documento))
    nro_documento_cliente = forms.IntegerField()
    email_cliente = forms.EmailField()

  

class nueva_consulta_de_contacto(forms.Form):

    #id_contacto = forms.IntegerField()
    nombre_contacto = forms.CharField(max_length=250)
    nacionalidad_contacto = forms.CharField(max_length=250)
    nro_documento_contacto = forms.IntegerField()
    email_contacto = forms.EmailField()
    texto_consulta_contacto = forms.CharField(max_length=3000)



class CustomUserCreationForm(UserCreationForm):  
   email=forms.EmailField()
   password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
   password2= forms.CharField(label="Repetir la Contraseña", widget=forms.PasswordInput)

   class Meta:
       model = User
       fields= ['username','email','password1','password2']
       help_text = {k:"" for k in fields}

class Formcomentarios(forms.Form):
    email_contacto = forms.EmailField()
    tipo_habitacion =forms.CharField(max_length=50, widget=forms.Select(choices= Tipo_habitaciones))
    comentario = forms.CharField(max_length=3000)


class UserEditForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Password 1', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password 2', widget=forms.PasswordInput)

    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = User
        fields = ['first_name','last_name','email', 'password1', 'password2']
        help_text = { k: "" for k in fields}


    
class AvatarFormulario(forms.Form):

    imagen = forms.ImageField()