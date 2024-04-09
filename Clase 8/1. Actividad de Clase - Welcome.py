"""
Escribir una función a la que se le pase una cadena del nombre de una ciudad
 <ciudad> y muestre por pantalla el saludo ¡Le damos la bienvenida a <ciudad>!
"""
def saludar(ciudad):
    print(f"Le damos la bienvenida a {ciudad}!")
ciudad = input("Ingrese el nombre de una ciudad: ")
saludar(ciudad)

#Solcuión Profesor:

def saludar_ciudad_1(nombre):
    mensaje = f"¡Le damos la bienvenida a {nombre}!"
    return mensaje

mensaje = saludar_ciudad_1("Mendoza")
print(mensaje)

#Solcuión Profesor 2:


def saludar_ciudad_2(nombre: str) -> str:
    mensaje = f"¡Le damos la bienvenida a {nombre}!"
    return mensaje

def ingresar_ciudad_2() -> str:
    entrada = input("Ciudad: ")
    return entrada

entrada = ingresar_ciudad_2()
mensaje = saludar_ciudad_2(entrada)
print(mensaje)

#Solcuión Profesor 3:


def saludar_ciudad(nombre: str) -> str:
    mensaje = f"¡Le damos la bienvenida a {nombre}!"
    return mensaje

def ingresar_ciudad() -> str:
    entrada = input("Ciudad: ")
    return entrada

def main():
    entrada = ingresar_ciudad()
    mensaje = saludar_ciudad(entrada)
    print(mensaje)

main()