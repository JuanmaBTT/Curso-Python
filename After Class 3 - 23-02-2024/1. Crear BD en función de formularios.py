# Crear un programa en Python que permita el registro
# de 3 formularios de personas en una base de datos.
# La base de datos es una lista que contiene diccionarios con las siguientes claves:
# "DNI" (número de identificación personal), "nombre", "edad", y "dirección"
# Para cada uno de los formularios, se debe solicitar al usuario que ingrese
# el DNI, nombre, edad y dirección de la persona correspondiente.
# Los datos ingresados deben ser almacenados en un nuevo diccionario
# y luego agregados a la base de datos.

base_de_datos: list[dict[str, str]] = []  # anotaciones de tipo o type hints

print("FORMULARIO 1")
dni = input("Ingresa DNI: ")
nombre = input("Ingresa nombre: ")
edad = input("Ingresa edad: ")
formulario = {"dni": dni, "nombre": nombre, "edad": edad}
base_de_datos.append(formulario)
print("FORMULARIO 2")
dni = input("Ingresa DNI: ")
nombre = input("Ingresa nombre: ")
edad = input("Ingresa edad: ")
formulario = {"dni": dni, "nombre": nombre, "edad": edad}
base_de_datos.append(formulario)

print("FORMULARIO 3")
dni = input("Ingresa DNI: ")
nombre = input("Ingresa nombre: ")
edad = input("Ingresa edad: ")
formulario = {"dni": dni, "nombre": nombre, "edad": edad}
base_de_datos.append(formulario)

print(base_de_datos)
