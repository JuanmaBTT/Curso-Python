# La siguiente matriz (o lista con listas anidadas) debe cumplir una condición:
# en cada fila el cuarto elemento siempre debe ser el resultado de sumar los tres primeros.
# ¿Eres capaz de agregar un elemento más a las listas anidadas con sumas,
# utilizando la técnica del slicing?
# ✨ Ayuda: La función llamada sum() devuelve una suma de todos los elementos de la lista.
# Partirás de:
#
# matriz = [
#     [1, 5, 1],
#     [2, 1, 2],
#     [3, 0, 1],
#     [1, 4, 4],
# ]
#
# Debes llegar a:
#
# matriz = [
#     [1, 5, 1, 7],
#     [2, 1, 2, 5],
#     [3, 0, 1, 4],
#     [1, 4, 4, 9]
# ]

matriz = [
     [1, 5, 1],
     [2, 1, 2],
     [3, 0, 1],
     [1, 4, 4],
 ]

print(matriz[0])

print(matriz[0][0]+matriz[0][0])

ultimo_campo_matriz = (matriz[0][0]+matriz[0][1]+matriz[0][2])
print(ultimo_campo_matriz)
ultimo_campo_matriz = sum(matriz[0])
print(ultimo_campo_matriz)

""" Una forma de hacerlo es append a matriz [X] e imprimir la X, 
otra es crear una variable sumando la X original y la sumatoria."""

#matriz[0].append(ultimo_campo_matriz)
#print(matriz[0])

matriz_listada = matriz[0]+[ultimo_campo_matriz]
print(matriz_listada)

#Forma larga de hacerlo

ultimo_campo_matriz_0 = sum(matriz[0])
ultimo_campo_matriz_1 = sum(matriz[1])
ultimo_campo_matriz_2 = sum(matriz[2])
ultimo_campo_matriz_3 = sum(matriz[3])
matriz_listada_0 = matriz[0]+[ultimo_campo_matriz_0]
matriz_listada_1 = matriz[1]+[ultimo_campo_matriz_1]
matriz_listada_2 = matriz[2]+[ultimo_campo_matriz_2]
matriz_listada_3 = matriz[3]+[ultimo_campo_matriz_3]

matriz_nueva = [
    [matriz_listada_0]+
    [matriz_listada_1]+
    [matriz_listada_2]+
    [matriz_listada_3]
]
from pprint import pprint

pprint(matriz_nueva,width=20)