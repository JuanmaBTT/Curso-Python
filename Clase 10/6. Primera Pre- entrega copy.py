"""

Objetivo
Practicar el concepto de funciones. Preparar la parte lógica para el registro de usuarios.

Consigna

Crear un programa que permita emular el registro y almacenamiento de usuarios en una base de datos. Crear el programa utilizando el concepto de funciones, diccionarios, bucles y condicionales.
Formato

El proyecto debe compartirse utilizando Colab bajo el nombre “Primera pre-entrega+Apellido”.


Se debe entregar
Se debe entregar todo el programa.

Sugerencias
El formato de registro es: Nombre de usuario y Contraseña.
Utilizar una función para almacenar la información y otra función para mostrar la información.
Utilizar un diccionario para almacenar dicha información, con el par usuario-contraseña (clave-valor).
Utilizar otra función para el login de usuarios, comprobando que la contraseña coincida con el usuario.

Adicional
Utilizando los conceptos de la clase 8, guarde la información en un archivo de texto dentro de su Drive."
Ejemplo

Ver video explicativo

"""

"""
seleccion=""
cuenta={"cedula": "", "password": ""}
"""
"""
almacenamiento_clientes= []

while usuario!="":
    print("Para Crear Cuenta debes brindarme algunos datos:")
    usuario=input("¿Podrías indicarme tu documento de identidad?")
    password=input("¿Podrías indicarme el la contraseña?")
    cuenta = {"cedula": usuario, "password": password}
    almacenamiento_clientes.append(cuenta)

    print(almacenamiento_clientes)
"""
"""
def crear_cuenta ():
    while True:
        print("Para Crear Cuenta debes brindarme algunos datos:")
        usuario=input("¿Podrías indicarme tu documento de identidad?")
        password=input("¿Podrías indicarme el la contraseña?")
        cuenta = {"cedula": usuario, "password": password}
        if condicionantes_usuario==True:
            almacenamiento_clientes.append(cuenta)
            print(almacenamiento_clientes)
        elif condicionantes_usuario==False:
            print("Usuario ya existente ❌")

def condicionantes_usuario(usuario):
    for cuenta in almacenamiento_clientes:
        if usuario in cuenta["cedula"]:
            return False
        else : 
            return True
    ### Lugar donde almaceno miembros del club y passwords:
"""
