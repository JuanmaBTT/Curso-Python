"""
A partir de dos variables llamadas NOMBRE y EDAD, debes crear una variable que almacene si se cumplen todas las siguientes condiciones, encadenando operadores lógicos en una sola línea:

NOMBRE sea diferente de cuatro asteriscos “****”
EDAD sea mayor que 5 y a su vez menor que 20
Que la longitud de NOMBRE sea mayor o igual a 4  pero a la vez menor que 8
EDAD multiplicada por 3 sea mayor que 35


Desde un input conseguir las variables:
nombre = INPUT!!!
edad = INPUT!!!!

"""

nombre = input("¿Cuál es tu nombre?")
edad = int(input("¿Cuál es tu edad?"))

print(nombre!="****" and edad>5 and edad<20 and len(nombre)>=4 and len(nombre)<8 and edad*3>35)


#Otras opciones:

# Ingreso de datos
nombre = input("Nombre: ")
edad = int(input("Edad: "))


# Operaciones
condicion_1 = nombre != "****"
condicion_2 = edad > 5 and edad < 20
condicion_3 = len(nombre) >= 4 and len(nombre) < 8
condicion_4 = (edad * 3) > 35
validacion = condicion_1 and condicion_2 and condicion_3 and condicion_4

# Salida
print(f"Nombre es diferente de '****' : {condicion_1}")
print(f"La edad es mayor a 5 y menor que 20: {condicion_2}")
print(f"La longitud del nombre es mayor o igual que 4 y menor que 8: {condicion_3}")
print(f"La edad multiplicada por 3 es mayor que 35: {condicion_4}")
print(f"Se cumplen todas las condiciones? {validacion}")
# Ingreso de datos
nombre = input("Nombre: ")
edad = int(input("Edad: "))


# Operaciones
validaciones = {
    "condicion_1": nombre != "****",
    "condicion_2": edad > 5 and edad < 20,
    "condicion_3": len(nombre) >= 4 and len(nombre) < 8,
    "condicion_4": (edad * 3) > 35,
}
validar = (
    validaciones["condicion_1"]
    and validaciones["condicion_2"]
    and validaciones["condicion_3"]
    and validaciones["condicion_4"]
)

# Salida
print(f"Nombre es diferente de '****' : {validaciones['condicion_1']}")
print(f"La edad es mayor a 5 y menor que 20: {validaciones['condicion_2']}")
print(f"La longitud del nombre es mayor o igual que 4 y menor que 8: {validaciones['condicion_3']}")
print(f"La edad multiplicada por 3 es mayor que 35: {validaciones['condicion_4']}")
print(f"Se cumplen todas las condiciones? {validar}")