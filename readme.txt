#######PARTICIPANTES################
Manuel Sassón
Jhonatan Herrera

El proyecto fue realizado en conjunto, aprovechando el mismo lugar físico pero dividiendo las tareas. Principalmente Manuel se enfocó en las vistas y modelos y Jhonatan
en la parte de los HTML, CCS y Templates, aunque no fue una división estricta. Cada ajuste o mejora se fue compartiendo en para probarla y mejorarla en caso que fuera necesario.

#####OBSERVACIONES#############################
Teniendo en cuenta que tomamos la decision de crear una página para reservas de habitaciones de un hotel, algunos conceptos básicos de la propuesta fueron adaptados para mejorar la usabilidad y demostración de los conceptos adquiridos en el curso, pero siempre manteniendo las funcionalidades requeridas.
Ej: El CRUD lo utilizamos dentro de las propias consultas de reservas, al buscar una reserva se permite editarla o borrarla y en la página “Reservar” se permite crear una nueva reserva

##########ABRIR EL PROYECTO#################

Paso 1: Descargar desde https://github.com/manusasson/proyecto_coder o https://github.com/Totan1991/proyecto_coder los componentes del proyecto
Paso 2: Pegarlos en una carpeta de uso y facil accceso.
Paso 3: Abrir editor de codigo ejemplo VS CODE, abrir una nueva terminal y navegar hasta llegar a la carpeta donde se guardaron los archivos descargados.
Paso 4: Una vez que se llega a la carpeta donde se encuentra el archivo manage.py se debe ejecutar el comando "python manage.py runserver".
Paso 5: Abrir la URL local donde se está  ejecutando el servidor (ejemplo: http://127.0.0.1:8000/)
Una vez abierta la URL estamos dentro del proyecto!

##########FUNCINALIDADES DEL PROYECTO#################

El proyecto consiste en un sitio web donde se puede observar la oferta de habitaciones de un hotel, así como también efectuar reservas y consultar las reservas a nombre del usuario, pudiendo posteriormente modificarlas y/o eliminarlas.

En la página "Inicio" se da la bienvenida al usuario y se da un pequeño detalle de las condiciones y servicios ofrecidos en el hotel.

En la página “Suites” se observan las cuatro categorías de habitaciones con su descripción, imágenes ilustrativas, costo y links a una búsqueda de comentarios de huéspedes anteriores para cada categoría de habitación.

En la página “Reservar”, estando previamente loggueado se permite realizar una reserva completando los datos requeridos en el formulario presente y confirmando la reserva.

En la página “Sus reservas” se puede buscar las reservas realizadas por el usuario, utilizando su email como parámetro de búsqueda, luego pudiendo modificar los datos de las mismas o directamente cancelarla, mediante la opción “Borrar reserva”.

Además, están las páginas de “Login” y “Logout” para registrarse, logguearse y deslogguearse. Cuando el usuario está logueado, en la barra de navegación aparece la opción actualizar los datos del usuario.

Para dejar registro de los comentarios del usuario como huésped, se le permite ir a la página “Suites”, entrar a los links de comentarios y realizar una búsqueda de comentarios según la habitación, teniendo la posibilidad de dejar sus comentarios. Automáticamente, se actualiza la base de datos y ya se puede observar aparecer el mismo en la lista de comentarios esa categoría de habitación.

A su vez, se agregó una aplicación de mensajería (http://127.0.0.1:8000/mensajes/)  a través de la cual el usuario puede dejar comentarios generales sobre el hotel y el servicio, así como refrescar la consulta y ver la lista histórica de comentarios.