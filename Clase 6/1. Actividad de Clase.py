"""
Descripción de la actividad. 

Escribir un programa que indique la generación correspondiente para un año de nacimiento indicado. 
Trabajarán con el notebook de clase Clase_4.ipynb

Importante: Para los años que no pertenezcan a ninguna generación, se deberá colocar: “No existe generación asociada”
"""
año_de_nacimiento=input("¿En que año naciste?").strip()

if año_de_nacimiento.isdigit():
    print(año_de_nacimiento)
    año_de_nacimiento= int(año_de_nacimiento)
    if año_de_nacimiento >= 1920 and año_de_nacimiento <= 1940:
        print("Generación Silenciosa")
    elif año_de_nacimiento >= 1946 and año_de_nacimiento <= 1964:
        print("Baby Boomer")
    elif año_de_nacimiento >= 1965 and año_de_nacimiento <= 1979:
        print("Generación X")
    elif año_de_nacimiento >= 1980 and año_de_nacimiento <= 2000:
        print("Generación Y")
    elif año_de_nacimiento >= 2001 and año_de_nacimiento <= 2010:
        print("Generación Z")
    else:
        print("Sin generación definida")
else:
    print("Debe ingresar dígitos 🔴")
    año_de_nacimiento=input("¿En que año naciste?").strip()

    if año_de_nacimiento.isdigit():
        print(año_de_nacimiento)
        año_de_nacimiento= int(año_de_nacimiento)
        if año_de_nacimiento >= 1920 and año_de_nacimiento <= 1940:
            print("Generación Silenciosa")
        elif año_de_nacimiento >= 1946 and año_de_nacimiento <= 1964:
            print("Baby Boomer")
        elif año_de_nacimiento >= 1965 and año_de_nacimiento <= 1979:
            print("Generación X")
        elif año_de_nacimiento >= 1980 and año_de_nacimiento <= 2000:
            print("Generación Y")
        elif año_de_nacimiento >= 2001 and año_de_nacimiento <= 2010:
            print("Generación Z")
        else:
            print("Sin generación definida")

###Otra Forma
            
generacion_silenciosa = range(1920, 1941)
baby_boomer = range(1946, 1965)
generacion_x = range(1965, 1980)
generacion_y = range(1980, 2001)
generacion_z = range(2001, 2011)

entrada = input("Año: ").strip()

if entrada.isdigit():
    año = int(entrada)
    if año in generacion_silenciosa:
        mensaje = "Eres de la Generación Silenciosa"
    elif año in baby_boomer:
        mensaje = "Eres un Baby Boomer"
    elif año in generacion_x:
        mensaje = "Eres de la Generación X"
    elif año in generacion_y:
        mensaje = "Eres de la Generación Y"
    elif año in generacion_z:
        mensaje = "Eres de la Generación Z"
    else:
        mensaje = "No existe generación asociada"
else:
    print("Debe ingresar dígitos 🔴")

print(mensaje)