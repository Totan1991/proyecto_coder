"""proyecto_coder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include
from django import views
from AppCoder.views import inicio
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from mensajes.views import nuevo_comentario

#from proyecto_coder.AppCoder.models import *
#from proyecto_coder.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    #path('inicio/', inicio),
    #path('reserva/', reserva ),
    #path('habitaciones/', habitaciones),
    #path('registro/', cliente),
    #path('contacto/', contactos),
    #path('parametros/<nombre>', parametro_por_url),
    path('AppCoder/',include('AppCoder.urls')),
    path('',inicio),
    path('mensajes/',include('mensajes.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)