from dataclasses import fields
from datetime import datetime,time
from distutils.util import change_root
import email
from random import choices
from secrets import choice
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  
from django.forms.forms import Form  




class Formcomentarios(forms.Form):
    Nombre = forms.CharField(max_length=250)
    email = forms.EmailField( required=False)
    fecha = forms.DateField( required=False)
    comentario = forms.CharField(max_length=3000)

