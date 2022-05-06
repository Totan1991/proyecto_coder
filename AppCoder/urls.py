from unicodedata import name
from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView




urlpatterns = [
   # path('', views.inicio),
    path('reservas/', views.reservas,name="reserva"),
    path('/', views.inicio, name="inicio"),
    path('inicio/', views.inicio, name="inicio"),
    path('pages/', views.pages,name="pages"),
   # path('habitaciones', ),
   # path('registro/', cliente),
   # path('contacto/', contactos),
   # path('parametros/<nombre>', parametro_por_url),
   path('buscar_reserva/', views.PagReserva,name="PagReserva"),
   path('busqueda_reserva/', views.busqueda_reserva,name="buscarreserva"),
   path('accounts/login/', views.login_request,name="Login"),
   path('accounts/signup/', views.signup,name="signup"),
   path('suites/', views.suites,name="suites"),
   path('nuevo_comentario/', views.nuevo_comentario,name="nuevo_comentarios"),
   path('borrar_reserva/<id_reserva>/', views.borrarReserva,name="borrar_reserva"),
   path('actualizar_reserva/<id_reserva>/', views.actualizarReserva,name="actualizar_reserva"),
   path('consultar_comentarios/', views.consultar_comentarios,name="consultar_comentarios"),
   path('accounts/profile/', views.profile,name="profile"),
   path('accounts/logout/', LogoutView.as_view(template_name='AppCoder/logout.html'), name = 'logout'),


]

