## Salimos del bucle cuando i es igual a 3

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

"""
Internet
"""

"""def main():
    print("SUMA DE NÚMEROS")
    numero = int(input("Escriba un número: "))
    suma = 0
    while numero >= 0:
        suma += numero
        numero = int(input("Escriba otro número: "))
    print()
    print(f"La suma de los números positivos introducidos es {suma}.")


if __name__ == "__main__":
    main()
"""

#Continue:

"""
La instrucción continue da la opción de omitir la parte de un bucle en la que se activa
 una condición externa, pero continuar para completar el resto del bucle. Es decir, la 
 iteración actual del bucle se interrumpirá, pero el programa volverá a la parte superior 
 del bucle.
"""


#Veamos un ejemplo:

print("Continue")

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#Pass:
  
"""
Cuando se activa una condición externa, la instrucción pass permite manejar la condición 
sin que el bucle se vea afectado de ninguna manera; todo el código continuará leyéndose a 
menos que se produzca la instrucción break u otra instrucción.

"""

print("Pass 1")

#Ejemplo 1
n = 0
while n < 10:
    n += 1
    if n == 2:
        pass
    print('n vale' , n)

print("Pass 2")

#Ejemplo 2
n = 0
while n < 10:
    n += 1
    if n == 2:
        pass
        print('n vale' , n)

print("#### - ¿Qué pasó en este ejemplo? - ####")
c = -3
while c < 10:
    c += 1
    if c == 2:
        pass
    print('c vale', c)

print("#### -  - ####")


print("#### - Corrección - ####")
c = -3
while c < 10:
    c += 1
    if c == 2:
        pass
        print('c vale', c)

#For: 
        
"""Se utiliza para recorrer los elementos de un objeto iterable (lista, tupla…) y ejecutar
 un bloque de código, o sea, tiene un número predeterminado de veces que itera. 
"""

""" EJEMPLO"""

lista = [0,1,2,3,4,5,6,7,8,9,10]
for num in lista:
    print('Soy un valor de la lista y valgo', num)
    num *= 5
    print('Soy un valor de la lista y ahora valgo', num)

"""MODIFICANDO LA LISTA"""
indice = 0
numeros = [0,1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
    numeros[indice] *= 5
    indice += 1
print(numeros)

#Enumerate: 
"""
La función incorporada enumerate(lista/tupla_de_valores) toma como argumento un objeto
 iterable y retorna otro cuyos elementos son tuplas de dos objetos:
"""
#Ejemplo:
numeros = [0,1,2,3,4,5,6,7,8,9,10]
for indice, numero in enumerate(numeros):
    numeros[indice] *= 5

#Si quisiéramos recorrer un string:

texto = 'Hola Mundo, estoy usando for en Python'
for letra in texto:
    print(letra)
texto2 = ''
for letra in texto:
    texto2 = letra * 2
print(texto2)

#For-break-continue-pass

print("#### -  - ####")


print("#### - Ejemplo - ####")
for numero in range(10):
    if numero == 2:
        continue
    elif numero == 8:
        break
    else:
        print("Se terminó de iterar y numero vale: ", numero)


