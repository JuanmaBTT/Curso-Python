""" Actividad en Clase: Desafío listas.

Descripción de acividad individual:

Dada dos listas Lista1 y Lista2 debes realiza las siguientes tareas:

1) Añade a la Lista1 el int 456789 y luego el string "Hola Mundo".
2) Luego añade a la Lista2 el string "Hola y Adios" y luego el int 5555.
3) Genera una Lista3 con todos los elementos de la Lista1 sin considerar el último elemento
4) Genera una Lista4 con todos los elementos de la Lista2 menos el primero y el último elemento.
5) Finalmente, genera una Lista5 con los elementos de la Lista4 y de la Lista3"""

lista_1 = [1,2,3]
lista_1.append (456789)
lista_1.append ("Hola Mundo")
print(lista_1)
lista_2 = [3,3,3,3]
lista_2.append ("Hola y Adios")
lista_2.append (5555)
print(lista_2)
lista1.pop ()
lista_3=lista1
print(lista_3)
lista_4 = lista2 [1:5]
print(lista_4)
lista_5 = lista_3 + lista_4
print (lista_5)

""" Solución Profesor"""

lista_1 = [1, "hola"]
lista_2 = [2, "chau"]

# a) Añade a la lista_1 el <int> 456789
# y luego el <str> "Hola Mundo"

lista_1.append(456789)
lista_1.append("Hola Mundo")
print(f"{lista_1=}")

# b) Añade a la lista_2 el <str> "Hola y adiós",
# y luego el <int> 5555

lista_2.append("Hola y adios")
lista_2.append(5555)
print(f"{lista_2=}")

# c) Genera una lista_3 con todos los elementos
# de la lista_1 sin considerar el último elemento
lista_3 = lista_1[:-1]
# lista_3 = lista_1.pop()
print(f"{lista_3=}")

# d) Genera una lista_4 con todos los elementos
# de la lista_2 menos el primero y el último elemento
lista_4 = lista_2[1:-1]
print(f"{lista_4=}")

# e) Genera una lista_5 con los elementos de la lista_4
# y de la lista_3
lista_5 = lista_4 + lista_3
# lista_5 = lista_4.extend(lista_3)
# print(f"{lista_4=}")
print(f"{lista_5=}")
# lista_5 = lista_4.extend(lista_3)
# print(f"{lista_4=}")
print(f"{lista_5=}")