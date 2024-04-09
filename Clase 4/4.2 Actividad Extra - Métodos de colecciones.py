"""
Consigna

A partir de una lista realizar las siguientes tareas sin modificar la lista original:

Borrar los elementos duplicados
Ordenar la lista de mayor a menor
Eliminar todos los números impares (  for ---- if (%2==1) ---- pop, remove   )
Realizar una suma de todos los números que quedan (sum(lista))
Añadir como primer elemento de la lista la suma realizada insert(0, suma)
Devolver la lista modificada
Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo,
 concuerda con el primer número de la lista
lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]
Nota: Recuerda que para sumar todos los números de una lista puedes usar sum

"""
lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]
print(lista)
lista = set(lista)
print(lista)
lista = list(lista)
print(lista)
lista.sort(reverse=True)
print(lista)
###Copie la lista porque si hacía el remove de la original cuando habían 2 impares seguidos no me lo tomaba
###(se corría 1 lugar en el index y no lo consideraba en la evaluación)
lista_aux = lista.copy()
for num in lista_aux:
    if num % 2 == 1: 
        print(num)
        lista.remove(num)
print(lista)
sum_lista=sum(lista)
print(sum_lista)
lista.insert(0, sum_lista)
print(lista)
print(sum(lista[1:]))
