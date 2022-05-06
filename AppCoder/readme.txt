##########ABRIR EL PROYECTO#################

Paso 1: Descargar desde https://github.com/manusasson/proyecto_coder los componentes del proyecto Paso 2: Pegarlos en una carpeta de uso y facil accceso. Paso 3: Abrir editor de codigo ejemplo VS CODE, abrir un nuevo terminal y navegar hasta la carpeta donde se guardaron los archivos descargados. Paso 4: Una vez que con el terminal llegamos dentro carpeta donde se encuentra el archivo manage.py ejecutar el comando "python manage.py runserver". Paso 5: Abrir la URL local donde se esta ejecutando el server ejemplo: http://127.0.0.1:8000/ Una vez abierta esa URL estamos dentro del proyecto!

##########FUNCINALIDADES DEL PROYECTO#################

El proyecto consiste en un sitio web donde se pueden efectuar reservas en un hotel y consultar las reservas efectuadas a nombre de una persona. En la página "Home" se da la bienvenida al usuario. En la página "Reservar" se puede completar un formulario con los datos requeridos para la reserva y al ejecutar el botón "Enviar" se guardan los mismos en la base de datos del hotel. A su vez, la página "Consultar Reserva" permite buscar las reservas efectuadas a nombre de una persona y presentar los datos de las mismas.

Las páginas "Reservar" y "Consultar Reserva" heredan el template de home y agregan los formularios de carga o búsqueda según corresponda.

Para efectuar tanto reservas, consultas de reservas y crear comentarios sobre las habitaciones, es necesario estar logueado, el cual sera direccionado en caso que no lo este.

Para registrarse es dentro del sitio: http://127.0.0.1:8000/AppCoder/register/

Una vez logueado, en la barra de navegacion aparece la opcion que permite la edicion del usuario: Nombre, Email, Apellido, Contraseña, ETC.

Las clases creadas detrás del sitio son: "reserva", "clientes", "habitaciones" y "contactos". Las mismas mantienen atributos informativos de las datos alojados en ellas. Los métodos creados son: "reservas", "inicio", "PagReserva" y "busqueda_reserva".