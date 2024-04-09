# Los conjuntos son una colección de datos, desordenados, mutables

# y sin elementos repetidos. No aceptan elementos como las listas

 

conjunto = {1, 2, 3, 4, 5}

print(type(conjunto))

otro_conjunto = {"Hola", "cómo ", "estás", 23, True, False, 0.5, (23, 32)}

print(otro_conjunto)

longitud = len(otro_conjunto)

print(longitud)

conjunto_vacio = set()

print(conjunto_vacio)

conjunto_range = set(range(10))

print(conjunto_range)

mi_lista = list(otro_conjunto)

mi_lista.append("Adios")

print(mi_lista)

mi_nuevo_conjunto = set(mi_lista)

print(mi_nuevo_conjunto)

 

conjunto_de_letras = {"a", "b", "c", "d"}

# print(conjunto_de_letras[:2]) # no se admite slicing en conjuntos

 

conjunto_de_numeros = {"hola", False, 10, 20, 30, 40}

conjunto_de_numeros.pop()

conjunto_de_numeros.add(50)

conjunto_de_numeros.add(10)

conjunto_de_numeros.add(20)

conjunto_de_numeros.add(30)

conjunto_de_numeros.add(40)

conjunto_de_numeros.add(50)

conjunto_de_numeros.add(60)

print(conjunto_de_numeros)

conjunto_de_numeros.discard(60)

print(conjunto_de_numeros)

conjunto_de_numeros.discard(60)

print(conjunto_de_numeros)