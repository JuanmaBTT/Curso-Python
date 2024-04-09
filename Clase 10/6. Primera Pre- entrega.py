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
almacenamiento_clientes: list[dict[str,str]] = []

def menu ():
    ###Mestra las distintas opciones a seleccionar.
    print("\n","**"*5+"Por favor, indique la opción que desea realizar."+"**"*5,"\n")
    print("1- Crear nueva cuenta.")
    print("2- Iniciar sesión.")
    print("3- Salir.")
    print("4- Ver almacenamiento Clientes.")



def seleccion_cliente ():
    ### Indica la opción que el cliente desea seleccionar:
    while True:
        try: 
            seleccion = int(input("¿Que opción desea seleccionar?"))
            if seleccion>4 or seleccion==0:
                raise NameError  # levantamos un error de forma manual  
        except ValueError:
            print("Debes introducir números, no caracteres que no lo sean")
        except NameError:
            print("No existe dicha opción,por favor, vuelva a intentarlo.")    
        else:
            print(f'Se ha seleccionado la opción {seleccion}')
            break
    ### Ejecución del comando:
    
    if seleccion==1:
        crear_cuenta()
    elif seleccion==2:
        iniciar_sesion()
    elif seleccion==3:
        print("Hasta Luego!")
    elif seleccion==4:
        print(almacenamiento_clientes)
    else : print("Dato erroneo.")


def crear_cuenta ():
            print("Para Crear Cuenta debes brindarme algunos datos:")
            usuario=input("¿Podrías indicarme tu documento de identidad?")
            password=input("¿Podrías indicarme el la contraseña?")
            cuenta = {"cedula": usuario, "password": password}
    ### Lugar donde almaceno miembros del club y passwords:


#"Usuario ya existente ❌"

"""
def condicionantes_usuario(usuario,cuenta):
    while True:
        for cuenta in almacenamiento_clientes:
            if usuario in cuenta["cedula"]:
                almacenamiento_clientes.append(cuenta)
            print(almacenamiento_clientes)
            print("Usuario creado con éxito! ✅")
        else : "Usuario ya existente ❌"
"""
def iniciar_sesion ():
        intentos=3
    ### Sección Usuario:    
        print("Para Iniciar Sesión debes brindarme algunos datos:")
        while intentos>0:
            usuario=input("¿Podrías indicarme tu documento de identidad?")
            password=input("¿Podrías indicarme el la contraseña?")
            cuenta = {"cedula": usuario, "password": password}
            for cuenta in almacenamiento_clientes:
                if usuario in cuenta["cedula"]:
                    return "Usuario valido ✅"
            else : print("Usuario no encontrado ❌")
            break
    ### Sección Password:
        while intentos>0:
            cuenta = {"cedula": usuario, "password": password}
            for cuenta in almacenamiento_clientes:
                if password in cuenta["password"]:
                    return "Contraseña correcta ✅"
            else : print("La contraseña no es válida ❌")
            intentos-=1
            print(f'La cantidad de intentos restantes son {intentos}')
            break


def main():
    while True:
        menu()
        seleccion = seleccion_cliente()

main()



"""
def main ():
    menu()
    seleccion= seleccion_cliente()
    cuenta=crear_cuenta(seleccion)
    resultado(almacenamiento_clientes,cuenta)

main()
"""
"""
def registro ():
    if seleccion==1:

""" 


    
"""Crear un programa que permita emular el registro y almacenamiento de usuarios en una base de datos. Crear el programa utilizando el concepto de funciones, diccionarios, bucles y condicionales."""
