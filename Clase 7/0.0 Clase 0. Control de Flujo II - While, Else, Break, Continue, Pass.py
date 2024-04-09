###Solución profe

suma =0
while continuar:
    entrada = input("Ingresa un número ('exit' para terminar): ")
    if entrada == "exit":
        continuar = False
    else:
        if entrada.isdigit():
            numero = int(entrada)
            # suma = suma + numero
            suma += numero
            print(f"La suma parcial es {suma}")
        else:
            print("*** Debes introducir un número ***")

print(f"La suma final es {suma}")

print("PASS")
x = 0
while x < 5:
    x = x + 1
    if x == 3:
        pass
    print(x)

print("CONTINUE")
x = 0
while x < 5:
    x = x + 1
    if x == 3:
        continue
    print(x)

print("BREAK")
x = 0
while x < 5:
    x = x + 1
    if x == 3:
        break
    print(x)

print("LISTAS")
lista = [1, 2, 3, 4, 5, 6]

for elemento in lista:
    print(elemento)

print("TUPLAS")
tupla = (1, 2, 3, 4, 5, 6)

for elemento in tupla:
    print(elemento)

print("CONJUNTOS")
conjunto = {1, 2, 3, 4, 5, 6}

for elemento in conjunto:
    print(elemento)

print("DICCIONARIOS")
diccionario = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f"}

print("**** CLAVES")
for clave in diccionario:
    print(clave)

print("**** CLAVES")
for clave in diccionario.keys():
    print(clave)

print("**** VALORES")
for valor in diccionario.values():
    print(valor)

print("**** CLAVES Y VALORES")
for clave, valor in diccionario.items():
    print(f"Clave: {clave} - Valor: {valor}")

print("CADENAS")
cadena = "Las cadenas..."

for caracter in cadena:
    print(caracter, end="\n")

lista = [1, 2, 3, 4, 5, 6]

for elemento in lista:
    if elemento == 3:
        continue
    if elemento == 5:
        break
    print(elemento)

indice = 0
lista = [1, 2, 3, 4, 5, 6]

for elemento in lista:
    # lista[indice] = lista[indice] * 5
    lista[indice] *= 5
    indice += 1

print(lista)

for n in range(10):
    print(f"n vale {n}")
for n in range(10):
    print(f"n vale {n}")

print()
for n in range(1, 5):
    print(f"n vale {n}")

print()
for n in range(3, 10, 2):
    print(f"n vale {n}")
import random

"""
Escribe un programa que genere un número aleatorio entre 1 y 20,
y le pida al usuario que adivine el número. Si el usuario adivina el número,
el programa debe imprimir "¡Adivinaste el número!"
y terminar. Si el usuario no adivina el número,
el programa debe imprimir "El número es mayor"
o "El número es menor", dependiendo de si el número generado
 es mayor o menor que el número ingresado por el usuario.
El programa debe permitir al usuario intentar adivinar
el número 5 veces.
"""

numero_aleatorio = random.randint(1, 6)
intentos = 0

while intentos < 5:
    entrada = int(input("Adivina el número entre 1 y 6: "))
    intentos += 1
    if entrada == numero_aleatorio:
        print("¡Adivinaste el número!")
        break
    elif entrada < numero_aleatorio:
        print("El número es mayor")
    else:
        print("El número es menor")
else:
    print("Se acabaron tus intentos...")