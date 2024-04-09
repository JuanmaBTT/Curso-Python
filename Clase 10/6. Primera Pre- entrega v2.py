def menu ():
    while True:
    ###Muestra las distintas opciones a seleccionar.
        print("\n","**"*5+"Por favor, indique la opción que desea realizar."+"**"*5,"\n")
        print("1- Crear nueva cuenta.")
        print("2- Iniciar sesión.")
        print("3- Salir.")
    ### Indica la opción que el cliente desea seleccionar:
        seleccion = input("Seleccione una opción: ")
        try: 
            seleccion = int(seleccion)
            if seleccion>3 or seleccion==0:
                raise NameError  # levantamos un error de forma manual  
        except ValueError:
                print("Debes introducir números, no caracteres que no lo sean")
        except NameError:
                print("No existe dicha opción,por favor, vuelva a intentarlo.")    
        else:
                print(f'Se ha seleccionado la opción {seleccion}')
                break
                ### Ejecución del comando:
    while True:
        if seleccion==1:
            crear_cuenta()
        elif seleccion==2:
            iniciar_sesion()
        elif seleccion==3:
            print("Hasta Luego!")
            break
        else : print("Dato erroneo.")

def crear_cuenta():
    print("\n","**"*5+" Registro de miembro: ","**"*5)
    while True:
        print("Para Crear Cuenta debes brindarme algunos datos, si quieres ir para atrás marcar 'back':")
        usuario=input("¿Podrías indicarme tu documento de identidad?")
        contraseña=input("¿Podrías indicarme la contraseña?")
        print(contraseña)
        if usuario=='back' or contraseña=='back':
            return crear_cuenta()
        elif contraseña.isdigit():
            print("Error, la contaseña debe contener letras.")
            return crear_cuenta()
        elif len(contraseña)<8:
            print("Error, debe contener al menos 8 carateres")
            return crear_cuenta()
        elif len(contraseña)>18:
            print("Error, debe contener menos de 18 carateres")
            return crear_cuenta()
        elif contraseña == contraseña.upper():
            print("Error, la contaseña debe contener minúsculas")
            return crear_cuenta()
        elif contraseña == contraseña.lower():
            print("Error, la contaseña debe contener mayúsculas")
            return crear_cuenta()
        elif usuario in almacenamiento_clientes:
            print("Error, el usuario ya existe.")
            return crear_cuenta()
        else:
            almacenamiento_clientes[usuario]=contraseña
            print("Registro de usuario y contraseña exitoso ✅")
            almacenamiento()
        menu()


def iniciar_sesion():
    ### Si el usuario desea ingresar al sitio.
    print("\n","**"*5+" Acceso al sitio: ","**"*5)

    oportunidades=3
    # *** Indicar nombre de usuario
    while oportunidades>0:
            print("Para Iniciar Sesión debes brindarme algunos datos, si quieres ir para atrás marcar 'back':")
            usuario=input("¿Podrías indicarme tu documento de identidad?")
            if usuario=='back':
                return menu()
            elif not usuario in almacenamiento_clientes:
                print("No se encontró la cédula ❌")
                break
            print("Cédula válida ✅")
    # *** password
    ### Si pongo el while acá se rompe. while oportunidades>0: Quiero que lo de arriba se repita infinitas veces, pero lo de abajo solo 3
            contraseña=input("¿Podrías indicarme la contraseña?")
            if contraseña=='back':
                return menu()
            if contraseña == almacenamiento_clientes[usuario]:
                    print("Acceso éxitoso al sitio. ¡Bienvenido! ✅")
                    return
            print("No encontró la contraseña ❌")
            oportunidades-=1
            print(f'Te quedan {oportunidades} oportunidades.')
            return
                
# Lugar donde almaceno miembros del club y passwords
almacenamiento_clientes: dict ={}
print(almacenamiento_clientes)

def almacenamiento():
    print(f'La base de datos de usuarios contiene los siguientes datos {almacenamiento_clientes}')

def main():
    seleccion = menu()
    almacenamiento()

main()