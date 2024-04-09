""" A partir de una variable llamada tupla, imprimir por pantalla de forma ordenada, lo siguiente

tupla = (5, 12, 7, 37, 8, 86, 19, 7, -783, 87, 188, 7, 9, 12, 7, 3982)
# 1- El último ítem de tupla
# 2- El número de ítems de tupla
# 3- La posición donde se encuentra el ítem 87 de tupla
# 5- Un ítem que haya en la posición 8 de tupla
# 4- Una lista con los últimos tres ítems de tupla
# 6- El número de veces que el ítem 7 aparece en tupla """

tupla = (5, 12, 7, 37, 8, 86, 19, 7, -783, 87, 188, 7, 9, 12, 7, 3982)
print(tupla[-1])
print(len(tupla))
print(tupla.index(87))
print(tupla[8])
print(tupla[-3:])
print(tupla.count(7))


