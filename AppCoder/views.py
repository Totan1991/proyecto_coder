from faulthandler import disable
from inspect import formatargvalues
from datetime import datetime
import re
from django.http import HttpResponse
from django.shortcuts import redirect, render
from AppCoder.models import *
from AppCoder.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm  
from django.core.files.storage import FileSystemStorage
from django.views.generic.edit import CreateView, UpdateView, DeleteView

@login_required(login_url='http://127.0.0.1:8000/AppCoder/accounts/login/')
def reservas(request):
        
        if request.method == "POST":
                miFormulario = nueva_reserva(request.POST, request.FILES)

                if miFormulario.is_valid():

                        data = miFormulario.cleaned_data
                        print(data)

                        reservar = reserva (nombre_cliente_reserva=data['nombre_cliente_reserva'], qde_adultos_reserva=data['qde_adultos_reserva'], qde_menores_reserva=data['qde_menores_reserva'], fecha_entrada=data['fecha_entrada'], fecha_salida=data['fecha_salida'], tipo_habitacion_reserva=data['tipo_habitacion_reserva'], email_cliente_reserva=data['email_cliente_reserva'], documento=data['documento'])
                        
                        reservar.save()                 

                        return render(request, "AppCoder/base.html",{"mensaje":f"Se ha registrado su reserva con éxito!"})
        else:         
                miFormulario = nueva_reserva()

        return render(request, "AppCoder/reservas.html",{"miFormulario":miFormulario})



def inicio(request):
        if request.user.is_authenticated:
                try:
                        avatares = Avatar.objects.filter(user=request.user.id)
                        return render(request, "AppCoder/inicio.html",{"url":avatares[0].imagen.url})
                except IndexError:
                        avatares = 'null'
                        return render(request, "AppCoder/inicio.html")
                
               # return render(request, "AppCoder/inicio.html",{"url":avatares[0].imagen.url})

        else:
                return render(request, "AppCoder/inicio.html")


def PagReserva(request):
        return render(request, "AppCoder/pages.html")        


@login_required(login_url='http://127.0.0.1:8000/AppCoder/accounts/login/')
def pages(request):
       
        #data =request.GET.get('email_cliente_reserva')
        #print(data)
        #if data:
                id_reserva= reserva.objects.all()
                #if id_reserva:   
                #        print(id_reserva)
               # return render(request, "AppCoder/pages.html",{"email_cliente_reserva":data,"id_reserva":id_reserva})               
                return render(request, "AppCoder/pages.html",{"id_reserva":id_reserva})               
               
                #else:
               # return render(request, "AppCoder/pages.html", {"id_reserva": "No se encontraron reservas con su email"})   
        
       # elif data=="":    
        
        #        return render(request, "AppCoder/pages.html", {"id_reserva": "No se ingresó el email a buscar"})    

        #else:      
        #        return render(request, "AppCoder/pages.html")


def login_request(request):

        if request.method =="POST":
                form= AuthenticationForm(request, data = request.POST)
                if form.is_valid():
                        usuario = form.cleaned_data.get('username')
                        contra = form.cleaned_data.get('password')

                        user = authenticate(username=usuario, password=contra)

                        if user is not None:
                                login(request, user)
                                print(usuario)
                                return render(request,"AppCoder/inicio.html", {"mensaje":f"Bienvenido {user} a la pagina del hotel Proyecto CoderHouse!"})
                        else:
                                form = AuthenticationForm()
                                return render(request,"AppCoder/inicio.html", {'form':form},{'mensaje':f"Usuario y/o contraseña incorrecta. Intente nuevamente."})
                                
                else:
                        form = AuthenticationForm()
                        return render(request,"AppCoder/login.html", {'form':form,'mensaje':f"Usuario y/o contraseña incorrecta. Intente nuevamente."})                                

        form = AuthenticationForm()
        return render(request,"AppCoder/login.html", {'form':form})


def suites(request,):

        return render(request,"AppCoder/suites.html")


#def pages(request):
  #      return render(request, "AppCoder/pages.html")


def signup(request):  
    if request.method == 'POST':  
        
        form = CustomUserCreationForm(request.POST)  
        if form.is_valid():  
             
                username=form.cleaned_data['username']
                form.save()  
                return render(request,'AppCoder/inicio.html',{"mensaje":"Se ha creado su usuario con éxito."})
    else:  

        form = CustomUserCreationForm()  
        
    return render(request, 'AppCoder/signup.html', {"form":form})  





def nuevo_comentario(request,):
       
        if request.method == "POST":
                miFormulario = Formcomentarios(request.POST)
               

                if miFormulario.is_valid():
                        data = miFormulario.cleaned_data

                        comentario = comentarios (email_contacto=data["email_contacto"],tipo_habitacion=data["tipo_habitacion"],comentario=data["comentario"] )
                        
                        comentario.save()                 

                        return render(request, "AppCoder/nuevo_comentario.html",{"mensaje":"Su comentario se ha guardado con éxito. Muchas gracias!"})
        else:         
                miFormulario = Formcomentarios()

        return render(request, "AppCoder/nuevo_comentario.html",{"form":miFormulario})





def consultar_comentarios(request):
        
        data =request.GET.get('Tipo_Habitacion')
        print(data)
        if data:
                comentario= comentarios.objects.filter(tipo_habitacion__icontains=data)
                print(comentario)
                if comentario:   
                        print(comentario)
                        return render(request, "AppCoder/consultar_comentarios.html",{"Tipo_Habitacion":data,"comentarios":comentario})               
                else:
                        return render(request, "AppCoder/consultar_comentarios.html", {"comentario": "No se encontraron comentarios"})   
        
        elif data=="":    
        
                return render(request, "AppCoder/consultar_comentarios.html", {"comentario": "No se ingresó el nombre a buscar"})    

        else:      
                return render(request, "AppCoder/consultar_comentarios.html")

                
@login_required(login_url='http://127.0.0.1:8000/AppCoder/accounts/login/')
def profile(request):
    
    usuario = request.user
    print(usuario.password)
    if request.method == "POST":
        formulario = UserEditForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            usuario.email = data["email"]
            usuario.password1 = data["password1"]
            usuario.password2 = data["password2"]
            usuario.last_name = data["last_name"]
            usuario.first_name = data["first_name"]
            print(usuario.password)

            usuario.save()

            return redirect("inicio")
        else:
            formulario = UserEditForm(initial={"email": usuario.email})  
            return render(request,  "AppCoder/editar_usuario.html", {"form": formulario, "errors": ["Datos inválidos. Intente nuevamente."]})

    else:
        formulario = UserEditForm(initial={"email": usuario.email})  
        return render(request,  "AppCoder/editar_usuario.html", {"form": formulario})


def borrarReserva(request, id_reserva):
        try:
                res = reserva.objects.get(id_reserva=id_reserva)
                res.delete()
                reservas = reserva.objects.all()
                contexto = {"reservas":reservas}
                return render(request, "AppCoder/consultar_reserva.html")

        except:
                return render(request, "AppCoder/consultar_reserva.html")


def actualizarReserva(request, id_reserva):

        res = reserva.objects.get(id_reserva=id_reserva)
        if request.method == "POST":
                formulario = nueva_reserva(request.POST, request.FILES)
                print(formulario.is_valid())
                
                if formulario.is_valid():
                        informacion = formulario.cleaned_data
                        print(informacion['documento'])
                        res.id_reserva = id_reserva
                        res.nombre_cliente_reserva = informacion['nombre_cliente_reserva']
                        res.qde_adultos_reserva = informacion['qde_adultos_reserva']
                        res.qde_menores_reserva = informacion['qde_menores_reserva']
                        res.fecha_entrada = informacion['fecha_entrada']
                        res.fecha_salida = informacion['fecha_salida']
                        res.tipo_habitacion_reserva = informacion['tipo_habitacion_reserva']
                        res.email_cliente_reserva = informacion['email_cliente_reserva']
                        res.save()
                        return render(request, "AppCoder/inicio.html")
                else:
                        informacion = formulario.cleaned_data
                        print(informacion['documento'])
                        return render(request, "AppCoder/inicio.html")             

 
        else:
                
                formulario = nueva_reserva(initial = {"id_reserva":res.id_reserva,"nombre_cliente_reserva": res.nombre_cliente_reserva,"qde_adultos_reserva":res.qde_adultos_reserva,"qde_menores_reserva":res.qde_menores_reserva,"fecha_entrada":res.fecha_entrada,"fecha_salida":res.fecha_salida,"tipo_habitacion_reserva":res.tipo_habitacion_reserva,"email_cliente_reserva":res.email_cliente_reserva,"documento":res.documento})

                return render(request, 'AppCoder/actualizar_reserva.html',{"formulario":formulario,"id_reserva":id_reserva})


def verReserva(request, id_reserva):
        res = reserva.objects.get(id_reserva=id_reserva)
        if request.method == "POST":
                formulario = nueva_reserva(request.POST)
                if formulario.is_valid():
                        informacion = formulario.cleaned_data
                        res.id_reserva = id_reserva
                        res.nombre_cliente_reserva = informacion["nombre_cliente_reserva"]
                        res.qde_adultos_reserva = informacion["qde_adultos_reserva"]
                        res.qde_menores_reserva = informacion["qde_menores_reserva"]
                        res.fecha_entrada = informacion["fecha_entrada"]
                        res.fecha_salida = informacion["fecha_salida"]
                        res.tipo_habitacion_reserva = informacion["tipo_habitacion_reserva"]
                        res.email_cliente_reserva = informacion["email_cliente_reserva"]
                        res.save()
                        return render(request, "AppCoder/inicio.html")
 
        else:
                
                formulario = nueva_reserva(initial = {"id_reserva":res.id_reserva,"nombre_cliente_reserva": res.nombre_cliente_reserva,"qde_adultos_reserva":res.qde_adultos_reserva,"qde_menores_reserva":res.qde_menores_reserva,"fecha_entrada":res.fecha_entrada,"fecha_salida":res.fecha_salida,"tipo_habitacion_reserva":res.tipo_habitacion_reserva,"email_cliente_reserva":res.email_cliente_reserva,"documento":res.documento})

                return render(request, 'AppCoder/consultar_reserva.html',{"formulario":formulario,"id_reserva":id_reserva})




@login_required()
def cargar_imagen(request):

    if request.method == "POST":

        formulario = AvatarFormulario(request.POST,request.FILES)

        if formulario.is_valid():

            usuario = request.user

            avatar = Avatar.objects.filter(user=usuario)

            if len(avatar) > 0:
                avatar = avatar[0]
                avatar.imagen = formulario.cleaned_data["imagen"]
                avatar.save()

            else:
                avatar = Avatar(user=usuario, imagen=formulario.cleaned_data["imagen"])
                avatar.save()
            
        return redirect("inicio")
    else:

        formulario = AvatarFormulario()
        return render(request, "appcoder/cargar_imagen.html", {"form": formulario})