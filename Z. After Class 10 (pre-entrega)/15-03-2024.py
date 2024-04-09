def registrar_miembro():
    """Registra nuevos miembros para el club"""
    print()
    print("*** Registro de miembro")
    email = input("Email: ")
    password = input("Password: ")
    formulario = {"email": email, "password": password}
    miembros_del_club.append(formulario)
    print("✅ Registro exitoso")

def acceder_al_club():
    """Realiza el acceso al club"""
    print()
    print("*** Acceso al club")
    
    # *** email
    email = input("Email: ")
    hay_email = False
    for formulario in miembros_del_club:
        if email in formulario["email"]:
            print("✅ Email correcto")
            hay_email = True
            break
    if not hay_email:
        print("❌ No encontré el email")
        return
   
    # *** password
    password = input("Password: ")
    hay_password = False
    for formulario in miembros_del_club:
        if email in formulario["email"] and password in formulario["password"]:
            print("✅ Acceso al club. ¡Bienvenido!")
            hay_password = True
            break
    if not hay_password:
        print("❌ No encontré el password")
        return
# Lugar donde almaceno miembros del club y passwords
miembros_del_club: list[dict] = []
print(miembros_del_club)
# Menú principal
while True:
    print()
    print("*** Bienvenido al sistema de acceso al club ***")
    print("1. Registrarse como miembro")
    print("2. Acceder al club")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        registrar_miembro()
    elif opcion == "2":
        acceder_al_club()
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Vuelva a intentar.")