""" Listas y String: Listas son mutables, pero String o texto NO"""

###Listas:

pares = [0,2,4,5,8,10]
pares[3]=6
print(pares)

### String/Cadena:

""" Asignación por slicing"""
letras = ["a", "b", "c", "d", "e"]
letras[:3] =["A","B","C"]
print(letras)

""" Borrar lista"""
letras = ["a", "b", "c", "d", "e"]
letras=[]
print(letras)

""" Borrar lista"""
letras = ["a", "b", "c", "d", "e"]
letras.clear()
print(letras)

""" Borrar por slicing"""
letras = ["a", "b", "c", "d", "e"]
letras[:3]=[]
print(letras)

# lista de 5 ciudades de latinoamérica
ciudades_latinoamerica = ["Buenos Aires", "São Paulo", "Mexico City", "Lima", "Bogotá"]
print(ciudades_latinoamerica)
cantidad_de_ciudades = len(ciudades_latinoamerica)
print(cantidad_de_ciudades)
print(ciudades_latinoamerica[0])
print(ciudades_latinoamerica[-1])

# más ciudades de latinoamerica
otras_ciudades = [
    "Santiago",
    "Montevideo",
    "Quito",
    "Caracas",
    "San Juan",
]

# concatenar listas
# ciudades_latinoamerica = ciudades_latinoamerica + otras_ciudades
ciudades_latinoamerica += otras_ciudades
print(ciudades_latinoamerica)
print(len(ciudades_latinoamerica))

# Buscando dentro de listas, lista de lista = Matriz

lista_de_listas = [[1,2],["a","b","c"]]
print(lista_de_listas[0][1])

# Tuplas: Son similares a las listas, pero inmutables

tupla = (1,2,3,4)
print(tupla)


# Tuplas únicas

tupla2 = (6,)

print(tupla2)

