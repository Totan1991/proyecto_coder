from unicodedata import name
from django.urls import path
from mensajes import views
from django.contrib.auth.views import LogoutView




urlpatterns = [
   # path('', views.inicio),
    path('', views.consultar_comentario,name="messages"),
    path('nuevo_comentario/', views.nuevo_comentario,name="nuevo_mensaje"),
    path('consultar_mensajes/', views.consultar_comentario,name="consultar_mensaje"),
    


]