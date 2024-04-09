def saludar_1 ():
    print("Saludo desde la función")
saludar_1()

def saludar(nombre):   # nombre es un parámetro
    longitud = len(nombre)
    print("=" * longitud)
    print(f"{nombre}")
    print("=" * longitud)


saludar("Ignacio Marcos Jorge")  # lo que envío se llama argumento

def saludar_con_nombre_1(nombre):
    saludando = print(f"¡le damos la bienvenida a {nombre}!")
    return saludando
saludar_con_nombre_1("Jorge")

def saludar_con_nombre(nombre):
    saludando = f"¡le damos la bienvenida a {nombre}!"
    return saludando   # si no hay return es como escribir return, o return None
    print("adiós")  # no se ejecuta

respuesta = saludar_con_nombre("Jorge")
print(respuesta)

def suma(numero_1, numero_2):
    return numero_1 + numero_2


# print(suma(100, 50))
respuesta = suma(100, 50)
print(respuesta)
def sumar(numero_1: int, numero_2: int) -> int:  # anotaciones de tipo o type hints
    """Esta función suma dos números"""
    return numero_1 + numero_2


# print(sumar(100, 50))
respuesta = sumar(100, 50)
print(respuesta)

def prueba():
    variable_local = "1. no ven de afuera🥴" 
    print(variable_local)
    print(variable_global)

def prueba_2():
    variable_local = "2. no ven de afuera🥴🥴" 
    print(variable_local)
    print(variable_global)


variable_global = 1000
print(variable_global)

prueba()
prueba_2()
print()