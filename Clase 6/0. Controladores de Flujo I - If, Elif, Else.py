comando = "AAAA"

if comando == "ENTRAR":
    print("Bienvenido al sistema")
elif comando == "SALUDO":
    print("¡Hola!")
elif comando == "SALIR":
    print("Saliendo del sistema")
else:
    print("No se reconoce el comando")

print("Fin")

### Ejercicio: Mejorar código.

edad = int(input("Tu edad: "))

if edad < 13:
    print("eres niño")
else:
    if edad < 18:
        print("eres adolescente")
    else:
        if edad < 40:
            print("eres joven, mayor de edad")
        else:
            if edad < 70:
                print("eres mayor de edad, experimentado")
            else:
                if edad < 120:
                    print("Tienes mucha experiencia de vida")
                else:
                    if edad >= 120:
                        print("Quizás haya un problema con tu edad")

### Mejorar código.

edad = int(input("Tu edad: "))

if edad < 0:
    print("Quizás haya un problema con tu edad")
elif edad < 13:
    print("eres niño")
elif edad < 18:
    print("eres adolescente")
elif edad < 40:
    print("eres joven, mayor de edad")
elif edad < 70:
    print("eres mayor de edad, experimentado")
elif  edad < 120:
    print("Tienes mucha experiencia de vida")
elif  edad >= 120:
    print("Quizás haya un problema con tu edad")
else : print ("Caso no encontrado")