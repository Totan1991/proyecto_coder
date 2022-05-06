from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
from django.shortcuts import render
from AppCoder.models import *



#def Inicio(request):
#    return HttpResponse("<h1>Inicio</h1>")


#def primer_vista(request):
#    return HttpResponse("Hola desde Django")

#def parametro_por_url (request, nombre):
#    return HttpResponse (f"tu nombre es {nombre}")

#def inicio(request):
#    archivo = open(r"C:\Users\user\Desktop\Curso Python\coderhouse\proyecto\proyecto_coder\repositorio_git\index.html","r")
#    plantilla = Template(archivo.read())

#    archivo.close()
#    context = Context()
#    documento = plantilla.render(context)
#    return HttpResponse(documento)


#def NuevoCliente(request):

 #   return HttpResponse("viewsregistro")

#def nuevo_cliente