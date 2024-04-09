print(17 % 2 == 1)
lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]
print(lista[4] % 2 == 1)
index=0
for num in lista:
    if num % 2 == 1:
        print(num,lista[index] % 2 == 1)
print(lista)

lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]
for num in lista:
    if num % 2 == 1: 
        print(num)
        lista.remove(num)
print(lista)