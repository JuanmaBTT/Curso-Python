# Página Web Moradita
>Orientada a la venta de artículos de hogar.
>Tiene 3 Apps: Clientes, About y Categoría de Productos (en la base es productos).
>Se pueden generar formularios en las 3 apps. Para el proyecto final imagino los formularios puedan estar visibles solo para X rol, Ejemplo: Admin/SuperUser.
>En Categoría de Productos se pueden crear categorías así como buscar. Por ejemplo: si buscamos limpieza se obtiene dicha categoría y la descripción.
>En la página principal se puede seleccionar el botón de "Whatsapp" y deriva a mi número de teléfono.
>En los artículos y se selecciona "Más info" figura el precio, así como una descripción de la referencia.
>En Python hay muchos archivos que no se están utilizando porque si bien aún no los he puesto en práctica para el proyecto final los visualizo, como el CRUDE y por ende ya lo dejé presentado en dicha App. 



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
