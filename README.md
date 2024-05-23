# Página Web Moradita

>Orientada a la venta de artículos y accesorios para el hogar.
>Tiene 3 Apps principales: Clientes, About(Sobre Nosotros) y Productos (en la cual está Categoría Productos y Productos).
>Tiene múltiples formularios: Para los usuarios corrientes el registrarse y loguearse.
>Para el admin, además de ellos, tiene CRUDE en Categoría de Productos, Productos, "Sobre Nosotros" y también se puede listar, borrar y editar clientes, además de agregar países para que los clientes indiquen como propios.Esto fue uno de los avances vs la versión pasada que indiqué: "Se pueden generar formularios en las 3 apps. Para el proyecto final imagino los formularios puedan estar visibles solo para X rol, Ejemplo: Admin/SuperUser" y así lo hice.
>En Categoría de Productos se pueden crear categorías así como buscar, editar o borrar. Por ejemplo: si buscamos limpieza se obtiene dicha categoría y la descripción. También pueden probar con Productos, About o Clientes.
>En el navbar añadí el logo de Whatsapp para que, en caso de clickear allí, la página derive a mi contacto y así poder concretar la venta. Antes estaba como un botón en la página principal y entiendo esto es una sustancial mejora porque siempre está visible para el cliente.
>Otra sustancial mejora que se realizó es que en la página principal ya no están más los productos, sino las categorías y a su vez relacioné los productos a esas categorías, por lo que se generan secciones automáticamente ante la creación tanto de Categorías como de Prodcutos. En las Categorías si se selección "Más Info" dirige a los artículos de dicha categoría y si a los artículos se le selecciona "Más info" figura el precio, así como una descripción de la referencia.
>Por último depure prácticamente todo lo que estaba en Python y no se estaba utilizando para dejar lo más prolijo el backend y no solo enfocarme en el frontend.
>Creo que quedó muy buena la página y estoy muy orgulloso por el tiempo y pasión que le dedique a la misma.

Ojalá que les guste!!



# Comandos

`mkdir nueva_carpeta`
> Crea una carpeta llamada nueva_carpeta

`ls`
> Muestra la lista de archivos

`cd nueva_carpeta`
> Cambia de carpeta

`pwd`
> Muestra la ruta actual

`python -m venv .venv`
> Crea un entorno virtual llamado .venv

`source .venv/bin/activate`
> Activa el entorno virtual en Linux o Mac

`.\venv\Scripts\activate`
> Activa el entorno virtual en Windows

`pip list`
> Muestra la lista de paquetes disponibles en el entorno virtual

`pip install django`
> Instala Django

`django-admin startproject config .`
> Crea un proyecto en el directorio actual

`python manage.py runserver`
> Ejecuta el servidor

`python manage.py startapp app`
> Crea una nueva aplicación llamada app

`python manage.py makemigrations`
> Crea las migraciones, que son archivos Python encargados de la base de datos

`python manage.py migrate`
> Ejecuta las migraciones, para que se realicen los cambios en la base de datos

`python manage.py createsuperuser`
> Crea un usuario administrador para acceder a 127.0.0.1:8000/admin

## Crea archivos de Requisito: requirements.txt

`pip freeze >> requirements.txt`
`pip install -r requirements.txt`
