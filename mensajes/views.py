from email import message
from django.shortcuts import render
from mensajes.forms import *
from mensajes.models import *

def nuevo_comentario(request,):
       
        if request.method == "POST":
                miFormulario = Formcomentarios(request.POST)
               

                if miFormulario.is_valid():
                        data = miFormulario.cleaned_data

                        comentario = comentarios (Nombre=data["Nombre"],email=data["email"],fecha=data["fecha"],comentario=data["comentario"] )
                        
                        comentario.save()                 
                        return render(request, "mensajes/consultar_mensajes.html")
                        #return render(request, "mensajes/consultar_mensajes.html",{"mensaje":"Su comentario se ha guardado con éxito. Muchas gracias!"})
        else:         
                miFormulario = Formcomentarios()

        return render(request, "mensajes/nuevo_mensaje.html",{"form":miFormulario})


def consultar_comentario(request):
        
       
        comentario= comentarios.objects.all()
        print(comentario)
        if comentario:   
                print(comentario)
                return render(request, "mensajes/consultar_mensajes.html",{"comentarios":comentario})               
        else:
                return render(request, "mensajes/consultar_mensajes.html", {"comentario": "No se encontraron comentarios"})   

  
