""" Agregar un dato a final"""

pares = [0,2,4,5,8,10]
pares.append(5)
print(pares)

""" Agregar un dato a final con fórmulas y contar cantidad de items en la lista"""

pares = [0,2,4,5,8,10]
pares.append(5*2+2)
print(pares)
print(len(pares))

""" Borrar un dato a final y contar cantidad de items en la lista"""

pares = [0,2,4,5,8,10]
pares.pop()
print(pares)
print(len(pares))


""" Borrar un dato X"""

pares = [0,2,4,5,8,10]
pares.pop(3)
print(pares)
print(len(pares))


""" Contar X"""

pares = [2,2,4,2,8,2]
print(pares.count(2))


""" Buscar X número"""

pares = [2,2,4,2,8,2]
print(pares.index(8))
print(pares.index(4))